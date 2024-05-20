import csv
import random
from faker import Faker

# Initialize Faker for generating fake data
fake = Faker()

# Function to generate random 8-digit numeric identifier
def generate_identifier():
    return random.randint(10000000, 99999999)

# Function to generate random surname
def generate_surname():
    return fake.last_name()

# Function to generate random given name
def generate_given_name():
    return fake.first_name()

# Function to generate random middle initial (may return an empty string)
def generate_middle_initial():
    return random.choice(['', random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')])

# Function to generate random suffix (may return an empty string)
def generate_suffix():
    return random.choice(['', random.choice(['Jr.', 'Sr.', 'III', 'IV'])])

# Function to generate random primary street number
def generate_primary_street_number():
    return random.randint(1, 9999)

# Function to generate random primary street name
def generate_primary_street_name():
    return fake.street_name()

# Function to generate random city
def generate_city():
    return fake.city()

# Function to generate random state
def generate_state():
    return fake.state_abbr()

# Function to generate random zipcode
def generate_zipcode():
    return random.randint(10000, 99999)

# Function to generate random email
def generate_email():
    return fake.email()

# Function to generate random 10-digit phone number starting with 9
def generate_phone():
    return int('9' + ''.join(random.choices('0123456789', k=9)))

# Function to generate random birthmonth
def generate_birthmonth():
    return fake.month_name()

# Generate test data for 100 records
test_data = []
for _ in range(100):
    record = {
        "Identifier": generate_identifier(),
        "Surname": generate_surname(),
        "Given Name": generate_given_name(),
        "Middle Initial": generate_middle_initial(),
        "Suffix": generate_suffix(),
        "Primary Street Number": generate_primary_street_number(),
        "Primary Street Name": generate_primary_street_name(),
        "City": generate_city(),
        "State": generate_state(),
        "Zipcode": generate_zipcode(),
        "Primary Street Number Prev": generate_primary_street_number(),
        "Primary Street Name Prev": generate_primary_street_name(),
        "City Prev": generate_city(),
        "State Prev": generate_state(),
        "Zipcode Prev": generate_zipcode(),
        "Email": generate_email(),
        "Phone": generate_phone(),
        "Birthmonth": generate_birthmonth()
    }
    test_data.append(record)

# Define CSV file headers
headers = [
    "Identifier",
    "Surname",
    "Given Name",
    "Middle Initial",
    "Suffix",
    "Primary Street Number",
    "Primary Street Name",
    "City",
    "State",
    "Zipcode",
    "Primary Street Number Prev",
    "Primary Street Name Prev",
    "City Prev",
    "State Prev",
    "Zipcode Prev",
    "Email",
    "Phone",
    "Birthmonth"
]

# Write test data to a CSV file
with open('test_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(test_data)

print("Test data generated successfully and saved to test_data.csv.")





