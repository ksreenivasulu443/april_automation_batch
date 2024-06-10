# import pyspark
from pyspark.sql import SparkSession

from pyspark.sql.functions import col,upper, lower, length, concat, initcap, explode, substring, instr,concat_ws, expr

data = [("Rahul","Smith","USA","C"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL"),
    ("ramesh","Smith","USA","CA"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL"),
    ("rahul","Smith","USA","A"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL"),
    ("Jamessadhfsadhgasfghashgfashdgfghsadfa","Smith","USA","CA"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","K"),
    ("Maria","Jones","USA","FL")
  ]
columns = ["firstname","lastname","country","state_name"]
df = spark.createDataFrame(data = data, schema = columns)
df.show(n=5,truncate=25)

df.select(df.firstname, df.lastname).show(5)
df.select(col('firstname'), col('lastname')).show(2)
df.select(df['firstname'], df['lastname'], df['country'], df['state_name']).show(2)
df.select(upper('firstname').alias('fn'), initcap('lastname').alias('ln')).show(5)
df.select(df.colRegex("`^.*name*`")).show(2)
df.select("*").show(2)
df.select("*").filter(" firstname = 'Rahul' ").show()
df.select("*").filter("(firstname = 'Rahul' or lastname ='Rose') and state_name = 'NY' ").show()
df.select((concat(upper(df.firstname),lower(df['lastname']), df.state_name)).alias("FullName"), length(col("state_name")).alias("State_num_letters")).filter("length(state_name) >=2 ").display()
df.select((concat_ws(" ",upper(df.firstname),lower(df['lastname']), df.state_name)).alias("FullName"), length(col("state_name")).alias("State_num_letters")).filter("length(state_name) >=2 ").display()
print("df.columns",df.columns)
print("df.columns[0]",df.columns[0])

selected_with_case = df.select(
    "score",
    "grade",
    expr(
        """
        CASE
            WHEN score >= 90 THEN 'A'
            WHEN score >= 80 THEN 'B'
            WHEN score >= 70 THEN 'C'
            WHEN score >= 60 THEN 'D'
            ELSE 'F'
        END AS grade_letter
        """
    )
)

filtered_df = df.filter(df["Name"].isin(["Alice", "Bob"]))
filtered_df = df.filter((df["Name"].startswith("A")) & (df["Age"] < 40))
