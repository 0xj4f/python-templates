import base64
import sys
import yaml


def load_yaml(file_path):
    with open(file_path) as f:
        data = yaml.safe_load(f)
        return data



def main(data):
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


if __name__ == '__main__':
    file_path = sys.argv[1]
    data = load_yaml(file_path=file_path)
    main(data=data)