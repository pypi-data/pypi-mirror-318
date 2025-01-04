import json
from pyspark.sql.functions import lit, current_timestamp, sha1, concat_ws, col, trim
from notebookutils import mssparkutils

def _reorder_columns_with_metadata(df, metadata_fields):
    """
    Reorders a DataFrame so that metadata columns appear at the start.

    Parameters:
    - df (DataFrame): The input PySpark DataFrame.
    - metadata_fields (list): List of metadata columns to appear at the start.

    Returns:
    - DataFrame: A DataFrame with reordered columns.
    """

    # Make sure we are dealing with a list
    if not isinstance(metadata_fields, list):
        metadata_fields = list(metadata_fields)

    # Identify metadata and non-metadata columns
    metadata_cols = [col for col in metadata_fields if col in df.columns]
    other_cols = [col for col in df.columns if col not in metadata_cols]

    # Combine metadata columns with the remaining columns
    reordered_cols = metadata_cols + other_cols

    # Reorder the DataFrame
    return df.select(reordered_cols)

def write_table_with_metafields(df, table_name, mode, skip_key):
    """
    Writes a DataFrame to a Delta table with standard metadata fields,
    using the BusinessKey as the primary identifier for upserts.

    Parameters:
    - df (DataFrame): The PySpark DataFrame to be written.
    - table_name (str): The name of the Delta table (saved under 'Tables/{table_name}').
    - mode (str): The write mode. Examples: "overwrite", "append", "upsert" (mandatory).

    Behavior:
    - Validates the presence of the "BusinessKey" column in the DataFrame.
    - If the table doesn't exist, creates it (for upsert mode).
    - Includes or updates specific metadata fields based on the write mode.

    Returns:
    - None: The function writes the DataFrame to the specified Delta table.
    """
    # Fetch Notebook Utilities Information
    fabric_job_id = mssparkutils.env.getJobId()

    # Extract the notebook name from the context
    notebook_name = notebookutils.runtime.context['currentNotebookName']

    # Validate required columns
    required_columns = ["business_key"]
    for col_name in required_columns:
        if col_name not in df.columns:
            raise ValueError(f"Missing required column: {col_name}")

    # Filter out rows with NULL or blank BusinessKey
    df = df.filter((col("business_key").isNotNull()) & (trim(col("business_key")) != ""))

    # Default source system to the notebook name
    if "id" not in df.columns:
        df = df.withColumn("id", sha1(col("business_key")))

    # If all rows are filtered, raise an exception
    if df.count() == 0:
        raise ValueError("The DataFrame contains no valid rows after filtering BusinessKey.")

    # Metadata fields to exclude from row_hash
    metadata_fields_list = [
        "id",
        "business_key",
        "inserted_time_utc",
        "updated_time_utc",
        "inserted_by_run_id",
        "updated_by_run_id",
        "processed_by",
        "row_hash"
    ]
    metadata_fields = set(metadata_fields_list)

    # Metadata fields not to update
    metadata_exclude_in_update = {
        "inserted_time_utc",
        "inserted_by_run_id"
    }

    # Add metadata fields for all modes
    if "inserted_by_run_id" not in df.columns:
        df = df.withColumn("inserted_by_run_id", lit(fabric_job_id))
    if "processed_by" not in df.columns:
        df = df.withColumn("processed_by", lit(notebook_name))
    if "inserted_time_utc" not in df.columns:
        df = df.withColumn("inserted_time_utc", current_timestamp())
    if "updated_time_utc" not in df.columns:
        df = df.withColumn("updated_time_utc", lit(None).cast("timestamp"))
    if "updated_by_run_id" not in df.columns:
        df = df.withColumn("updated_by_run_id", lit(None).cast("string"))
    # Compute row_hash (excluding metadata fields)
    business_columns = [col_name for col_name in df.columns if col_name not in metadata_fields]
    business_columns = sorted(business_columns)
    if "row_hash" not in df.columns:
        df = df.withColumn("row_hash", sha1(concat_ws("-", *[col(c) for c in business_columns])))

    # Reorder columns
    df = _reorder_columns_with_metadata(df,metadata_fields_list)

    # Save or Merge DataFrame
    table_path = f"Tables/{table_name}"
    if mode == "overwrite":
        # Overwrite the entire table
        df.write.mode("overwrite").format("delta").save(table_path)
    elif mode == "append":
        # Append new rows
        df.write.mode("append").format("delta").save(table_path)
    elif mode == "upsert":
        # Check if the table exists
        from delta.tables import DeltaTable
        try:
            delta_table = DeltaTable.forPath(spark, table_path)
            table_exists = True
            print("Table exists...")
        except Exception:
            table_exists = False

        if not table_exists:
            # If the table doesn't exist, treat as a new insert
            print(f"Table '{table_name}' does not exist. Creating it as a new table.")
            df.write.mode("overwrite").format("delta").save(table_path)
        else:

            # Determine the min and max of the skip_key for data skipping
            skip_key_min = df.selectExpr(f"min({skip_key}) as min_{skip_key}").collect()[0][0]
            skip_key_max = df.selectExpr(f"max({skip_key}) as max_{skip_key}").collect()[0][0]

            # Merge condition using business_key
            merge_condition = (
                f"target.business_key = source.business_key AND "
                f"target.{skip_key} >= '{skip_key_min}' AND target.{skip_key} <= '{skip_key_max}'"
            )

            # Perform the merge
            delta_table.alias("target").merge(
                df.alias("source"),
                merge_condition
            ).whenMatchedUpdate(
                condition="source.row_hash != target.row_hash",  # Skip updates if hash matches
                set={
                    "updated_time_utc": current_timestamp(),
                    "updated_by_run_id": lit(fabric_job_id),
                    **{col: f"source.{col}" for col in df.columns if col not in metadata_exclude_in_update}
                }
            ).whenNotMatchedInsert(
                values={
                    **{col: f"source.{col}" for col in df.columns}
                }
            ).execute()
    else:
        raise ValueError(f"Unsupported write mode: {mode}")

    # Log success (optional)
    print(f"DataFrame written successfully to {table_path} in {mode} mode.")
    print(f"Run ID: {fabric_job_id}, Source System: {notebook_name}")
