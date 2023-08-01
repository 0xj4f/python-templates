import yaml

# Assuming you have YAML data stored in a file called 'data.yaml'
with open('data.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

# The 'yaml_data' variable now contains the dictionary representation of your YAML data
print(yaml_data)


"""
Another method is loading yaml data as string
"""
yaml_string = """
server: demo.database.windows.net
database: demosql
username: sqladmin
password: XXXXXXXXXXX
"""

# Load YAML data from the string
yaml_data = yaml.safe_load(yaml_string)

# The 'yaml_data' variable now contains the dictionary representation of your YAML data
print(yaml_data)
