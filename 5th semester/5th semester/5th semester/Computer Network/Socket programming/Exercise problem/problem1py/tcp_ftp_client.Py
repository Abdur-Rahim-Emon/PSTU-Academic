import socket

HOST = '127.0.0.1'
PORT = 5000
INPUT_FILE = 'send_tcp_file.txt' 
TIMEOUT_SECONDS = 2.0  # Timeout for waiting for an ACK

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    client_socket.settimeout(TIMEOUT_SECONDS)  # Set timeout for socket read

    with open(INPUT_FILE, 'rb') as f:
        while True:
            # Read 100-byte chunk (or less for the last unit)
            chunk = f.read(100)
            if not chunk:
                break  # End of file reached

            ack_received = False

            # Retransmission loop
            while not ack_received:
                try:
                    print(f"Sending chunk of {len(chunk)} bytes...")
                    client_socket.sendall(chunk)

                    # Block until ACK is received or socket times out
                    ack = client_socket.recv(1024)
                    if ack == b"ACK":
                        print("ACK received for current chunk.\n")
                        ack_received = True

                except socket.timeout:
                    print("--> Timeout! ACK not received. Retransmitting chunk...")

    print("File transfer finished successfully.")