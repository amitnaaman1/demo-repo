import socket

def start_server():
    host = '127.0.0.1'  # Server IP address
    port = 12345       # Server port number

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(1)

    print("Server listening on {}:{}".format(host, port))

    while True:
        # Wait for a client to connect
        client_socket, addr = server_socket.accept()

        print("Connected to client: {}".format(addr))

        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        print("Received message from client: {}".format(data))

        # Process the data or perform any necessary operations

        # Send a response back to the client
        response = "Message received: {}".format(data)
        client_socket.send(response.encode('utf-8'))

        # Close the connection with the client
        client_socket.close()


# Start the server
start_server()
