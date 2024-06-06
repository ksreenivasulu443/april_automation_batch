import pandas as pd
input_data = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'salary': [70000, 80000, 90000]
})

expected_output = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'salary': [77000, 88000,99000]
})

def example_transformation(input_data):
    input_data['salary'] = input_data['salary'] * 1.1
    return input_data
transformed_data=example_transformation(input_data)
transformed_data['salary']=transformed_data['salary'].astype(int)

print(transformed_data.dtypes)
print(expected_output.dtypes)

if transformed_data.equals(expected_output):
    print("Data transformation validation successful!")
else:
    print("Data transformation validation failed!")
    # Print differences if validation fails
    print("Differences:")
    print(transformed_data.compare(expected_output))