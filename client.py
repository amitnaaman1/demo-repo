import socket

def start_client():
    host = '127.0.0.1'  # Server IP address
    port = 12345       # Server port number

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))

    # Send a message to the server
    message = "Hello, server!"
    client_socket.send(message.encode('utf-8'))

    # Receive the response from the server
    response = client_socket.recv(1024).decode('utf-8')
    print("Server response: {}".format(response))

    # Close the connection with the server
    client_socket.close()


# Start the client
start_client()
