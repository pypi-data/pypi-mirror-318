from pyspark.sql import DataFrame
from pyspark.sql.functions import concat_ws, sha1, col, current_timestamp, lit

def add_business_key_and_id(df: DataFrame, key_fields: list, delimiter: str = ":") -> DataFrame:
    """
    Adds a 'BusinessKey' column by concatenating specified fields and generates
    a unique 'Id' column based on the SHA-1 hash of the 'BusinessKey'.

    Parameters:
    - df (DataFrame): The input DataFrame.
    - key_fields (list): List of field names to use for generating the BusinessKey.
    - delimiter (str): Delimiter to use when concatenating key fields. Default is ":".

    Returns:
    - DataFrame: The DataFrame with added 'BusinessKey' and 'Id' columns.
    """
    # Create the BusinessKey column
    df = df.withColumn("business_key", concat_ws(delimiter, *[col(field) for field in key_fields]))
    
    # Generate the Id column based on the BusinessKey
    df = df.withColumn("id", sha1(col("business_key")))
    
    return df


from pyspark.sql import DataFrame
from pyspark.sql.functions import col, to_timestamp, row_number
from pyspark.sql.window import Window


def dedupe_latest(dataframe: DataFrame, sort_field: str = "inserted_time_utc_raw") -> DataFrame:
    """
    Deduplicates the DataFrame by the `business_key` field, keeping the latest record based on `sort_field`.

    :param dataframe: Input PySpark DataFrame.
    :param sort_field: Field to sort by for deduplication, defaults to 'inserted_time_utc_raw'.
    :return: Deduplicated PySpark DataFrame.
    :raises ValueError: If 'business_key' field is missing.
    """
    if "business_key" not in dataframe.columns:
        raise ValueError("The DataFrame must contain a 'business_key' column.")

    # Convert sort_field to timestamp if it is a string
    if sort_field in dataframe.columns:
        if dataframe.schema[sort_field].dataType.simpleString() == "string":
            dataframe = dataframe.withColumn(
                "_sort_key", to_timestamp(col(sort_field)).alias("_sort_key")
            )
        else:
            dataframe = dataframe.withColumn("_sort_key", col(sort_field))
    else:
        raise ValueError(f"Sort field '{sort_field}' does not exist in the DataFrame.")

    # Define a window specification
    window_spec = Window.partitionBy("business_key").orderBy(col("_sort_key").desc())

    # Add a row number column and filter only the first row for each business_key
    deduped_df = dataframe.withColumn("row_number", row_number().over(window_spec))
    deduped_df = deduped_df.filter(col("row_number") == 1).drop("row_number", "_sort_key")

    return deduped_df