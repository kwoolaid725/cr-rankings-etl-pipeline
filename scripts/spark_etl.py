from pyspark.sql import SparkSession
from pyspark.sql.functions import (upper, size, countDistinct, sum, dense_rank, col,
                                   lit, regexp_extract,
                                   concat_ws, count, isnan,
                                   when, avg, round, coalesce)
from pyspark.sql.window import Window
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType
import logging
import sys

sys.path.append('/')



# create spark session state
def spark_session():
    appName = "spark etl pipeline"
    spark = SparkSession.builder \
        .appName(appName) \
        .getOrCreate()

    return spark




if __name__ == "__main__":
    logging.info("spark_etl is Started ...")
    main()