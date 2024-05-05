import json

from pyspark.sql import SparkSession



from utility.general_utility import flatten

def read_file(type: str,
              path: str,
              spark: SparkSession,
              row,
              schema: str = 'NOT APPL',
              multiline: bool = True,
              ):