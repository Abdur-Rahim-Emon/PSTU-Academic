import socket

HOST = '127.0.0.1'
PORT = 5000
OUTPUT_FILE = 'received_tcp_file.txt'
#OUTPUT_FILE = r'F:\5th semester\Computer Network\Socket programming\Exercise problem\problem8\received_tcp_file.txt'
#for any location 

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket: #SOCK_STREAM = TCP PROTOCOL AF_INET= IPV4 ADDRESS
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"TCP FTP Server listening on {HOST}:   {PORT}...")

    conn, addr = server_socket.accept() #conn =new socket used to communicate with the client

    print(f"Client connected from: {addr}")

    with conn, open(OUTPUT_FILE, 'wb') as f: # with used here for that automatically cloese resources when finished
    # w= write( creates a new file or overwrite an existing one) b= binary model
        while True:
            # Receive up to 100 bytes at a time
            data = conn.recv(100)
            if not data:
                break  # Connection closed by client

            f.write(data)
            f.flush()  # Force write data to disk immediately
            print(f"Received {len(data)} bytes. Sending ACK...")

            # Send acknowledgment back to client
            conn.sendall(b"ACK")

    print(f"Transfer completed! File saved as '{OUTPUT_FILE}'.")