import base64
import sys
import yaml
# pip3 install pyyaml

"""
########################################
yaml structure
########################################
apiVersion: v1
items:
- apiVersion: v1
  data:
    allowed-headers: Kg==
    allowed-max-age: MzYwMA==
    key: base64 Value

########################################
# USAGE: 
########################################
python3 kubernetes-secret-decoder.py secrets.yaml
Key: allowed-headers
Decoded Value: *
---
Key: allowed-max-age
Decoded Value: 3600
---
Key: allowed-methods
Decoded Value: GET, PUT, POST, DELETE, PATCH, OPTIONS
---
Key: api-base-path
Decoded Value: https://example.io
---
Key: aws-access-key-id
Decoded Value: AAAAAAAA
---
Key: aws-region
Decoded Value: us-east-2
"""

# Get the file path from command-line arguments
file_path = sys.argv[1]

# Load the YAML file
with open(file_path) as f:
    data = yaml.safe_load(f)

# Extract the properties under 'data'
items = data.get('items', [])
for item in items:
    data_dict = item.get('data', {})
    for key, value in data_dict.items():
        # Decode the base64-encoded value
        decoded_value = base64.b64decode(value).decode('utf-8')

        # Print the key and decoded value
        print(f"Key: {key}")
        print(f"Decoded Value: {decoded_value}")
        print("---")
