import pymongo
import datetime
import tarfile
import os
import shutil

"""
pip3 install pymongo 
"""


# MongoDB connection details
mongo_host = 'your-mongo-host'
mongo_port = 27017
mongo_username = 'your-username'
mongo_password = 'your-password'

# Get current date
current_date = datetime.date.today().strftime('%Y-%m-%d')

# Create a MongoDB client
client = pymongo.MongoClient(host=mongo_host, port=mongo_port, username=mongo_username, password=mongo_password)

# Get a list of all databases
databases = client.list_database_names()

# Create a folder with the current date
folder_name = f'backup_{current_date}'
tar_filename = f'{folder_name}.tar.gz'

# Create the folder
os.makedirs(folder_name)

# Iterate over each database
for db_name in databases:
    # Get the database object
    db = client[db_name]
    
    # Get a list of all collections in the database
    collections = db.list_collection_names()
    
    # Iterate over each collection and export the data
    for collection_name in collections:
        # Export the collection data
        collection_data = list(db[collection_name].find())
        
        # Save the collection data to a file
        file_path = f'{folder_name}/{db_name}_{collection_name}.json'
        with open(file_path, 'w') as file:
            file.write(str(collection_data))
    
# Close the MongoDB connection
client.close()

# Create a tar.gz file of the backup folder
with tarfile.open(tar_filename, 'w:gz') as tar:
    tar.add(folder_name, arcname=os.path.basename(folder_name))

# Remove the backup folder
shutil.rmtree(folder_name)

print('Backup completed successfully.')
