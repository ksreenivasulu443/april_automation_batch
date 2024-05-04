import datetime
import sys

import pandas as pd
import openpyxl
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import collect_set
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from utility.read_utility import read_file, read_db, read_snowflake
from utility.validation_lib import count_check, duplicate_check, uniqueness_check, records_present_only_in_source, \
    null_value_check, data_compare, name_check, column_range_check, column_value_reference_check, schema_check

project_path = os.getcwd()

postgre_jar = project_path + "/jars/postgresql-42.2.5.jar"
snow_jar = project_path + "/jars/snowflake-jdbc-3.14.3.jar"

jar_path = postgre_jar+','+snow_jar

template_path = project_path + '/config/Master_Test_Template.xlsx'
test_cases = pd.read_excel(template_path)

print ("test_cases",test_cases)

cwd = os.getcwd()
#print(cwd)
# user = os.environ.get('USER')
# print(user)
result_local_file = cwd+'\Execution_detailed_summary.txt'
print("result_local_file",result_local_file)

Out = {
    "validation_Type": [],
    "Source_name": [],
    "target_name": [],
    "Number_of_source_Records": [],
    "Number_of_target_Records": [],
    "Number_of_failed_Records": [],
    "column": [],
    "Status": [],
    "source_type": [],
    "target_type": []
}
run_test_case = test_cases.loc[(test_cases.execution_ind == 'Y')]

# validation = (run_test_case.groupBy('source', 'source_type',
#                                     'source_db_name', 'source_schema_path', 'source_transformation_query_path',
#                                     'target', 'target_type', 'target_db_name','target_schema_path',
#                                     'target_transformation_query_path',
#                                     'key_col_list', 'null_col_list','exclude_columns',
#                                     'unique_col_list','dq_column','expected_values','min_val','max_val').
#               agg(collect_set('validation_Type').alias('validation_Type')))
#
# print (validation)

validations = validation.collect()
print("*"*50)
print(f"Execution has started")
print("*"*50)