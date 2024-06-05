import pandas as pd
import json

# Load JSON data into a dictionary
with open(r"D:\ETL_Automation\ReadFiles\multiple_arry.json") as data_file:
    data = json.load(data_file)

# Normalize the JSON data and convert it into a DataFrame
df_list = []
for brand, models in data['cars'].items():
    for model_info in models:
        df_list.append({
            'Car': brand,
            'Model': model_info['model'],
            'Doors': model_info['doors']
        })

df = pd.DataFrame(df_list)

# Print the DataFrame to see the tabular output
print(df.to_markdown(index=False))