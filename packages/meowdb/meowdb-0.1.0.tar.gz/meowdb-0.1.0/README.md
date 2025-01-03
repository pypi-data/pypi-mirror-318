# MeowDB Python Library

This library provides a Python interface for the MeowDB in-memory database server.

## Features
- **Create**: Add a new key-value pair to the database.
- **Insert**: Insert or update a key-value pair.
- **Select**: Retrieve the value associated with a key.
- **Update**: Modify the value of an existing key.
- **Delete**: Remove a key-value pair from the database.
- **Hello**: A simple command to test the library connection.

## Installation
You can install this library by copying the `python_lib` directory into your project.

## Usage
```python
from python_lib.meowdb import MeowDB

# Connect to the MeowDB server
db = MeowDB(host='localhost', port=6969)

print(db.hello())  # Test the connection
print(db.create("mykey", "myvalue"))  # Create a new key-value pair
print(db.select("mykey"))               # Retrieve the value for 'mykey'
print(db.update("mykey", "newvalue"))  # Update the value for 'mykey'
print(db.select("mykey"))               # Retrieve the updated value
print(db.delete("mykey"))               # Delete the key-value pair for 'mykey'

# Close the connection when done
db.close()
```

## Command Descriptions
- **create <key> <value>**: Create a new key-value pair.
- **insert <key> <value>**: Insert or update a key-value pair.
- **select <key>**: Retrieve the value associated with a key.
- **update <key> <value>**: Update the value of an existing key.
- **delete <key>**: Delete a key-value pair.
- **hello**: Test the server connection.

## License
This project is licensed under the MIT License.
