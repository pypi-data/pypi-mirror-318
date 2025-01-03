import socket, re

class MeowDB:
    """
    A class to interact with the MeowDB in-memory database server.

    Attributes:
        host (str): The hostname of the server.
        port (int): The port number of the server.
        socket (socket.socket): The socket connection to the server.
    """

    def __init__(self, host='localhost', port=6969):
        """
        Initializes the MeowDB client and connects to the server.

        Args:
            host (str): The hostname of the server (default is 'localhost').
            port (int): The port number of the server (default is 6969).
        """
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def create(self, key, value) -> bool:
        """
        Creates a new key-value pair in the database.

        Args:
            key (str): The key to create.
            value (str): The value associated with the key.

        Returns:
            bool: True if the creation was successful, otherwise raises an exception.
        """
        try:
            command = f"create {key} {value}"
            self.socket.sendall(command.encode())
            response = self.receive_response()
            if response == key:
                return True
            raise Exception("Create could not be completed: " + response)
        except Exception as err:
            raise Exception("Create could not be completed: " + str(err))

    def insert(self, key, value) -> bool:
        """
        Inserts or updates a key-value pair in the database.

        Args:
            key (str): The key to insert or update.
            value (str): The value associated with the key.

        Returns:
            bool: True if the insertion or update was successful, otherwise raises an exception.
        """
        try:
            command = f"insert {key} {value}"
            self.socket.sendall(command.encode())
            response = self.receive_response()
            if response == key:
                return True
            raise Exception("Insert could not be completed: " + response)
        except Exception as err:
            raise Exception("Insert could not be completed: " + str(err))
        
    def select(self, key) -> str:
        """
        Retrieves the value associated with a key.

        Args:
            key (str): The key to retrieve.

        Returns:
            str: The value associated with the key, or None if the key is not found.
        """
        try:
            command = f"select {key}"
            self.socket.sendall(command.encode())
            response = self.receive_response()
            if response.lower == f"key[{key}]::not found":
                return None
            return response
        except Exception as err:
            raise Exception("Select could not be completed: " + str(err))
 
    def update(self, key, value) -> bool:
        """
        Updates the value associated with a key.

        Args:
            key (str): The key to update.
            value (str): The new value associated with the key.

        Returns:
            bool: True if the update was successful, otherwise raises an exception.
        """
        try:
            command = f"update {key} {value}"
            self.socket.sendall(command.encode())
            response = self.receive_response()
            if response == key:
                return True
            raise Exception("Update could not be completed: " + response)
        except Exception as err:
            raise Exception("Update could not be completed: " + str(err))
    
    def delete(self, key) -> bool:
        """
        Deletes a key-value pair from the database.

        Args:
            key (str): The key to delete.

        Returns:
            bool: True if the deletion was successful, otherwise raises an exception.
        """
        try:
            command = f"delete {key}"
            self.socket.sendall(command.encode())
            response = self.receive_response()
            if response == key:
                return True
            elif response == f"key[{key}]::not found":
                return False
            else:
                raise Exception("Delete could not be completed: " + response)
        except Exception as err:
            raise Exception("Delete could not be completed: " + str(err))
    
    def hello(self) -> str:
        """
        Sends a hello command to the server.

        Returns:
            str: The response from the server.
        """
        try:
            command = "hello"
            self.socket.sendall(command.encode())
            return self.receive_response()
        except Exception as err:
            raise Exception("Hello could not be completed: " + str(err))

    def receive_response(self) -> str:
        """
        Receives a response from the server.

        Returns:
            str: The response from the server.
        """
        try:
            response = self.socket.recv(1024).decode().strip()
            return response
        except Exception as err:
            raise Exception("Response could not be received: " + str(err))
        
    def close(self):
        """
        Closes the socket connection to the server.
        """
        self.socket.close()
