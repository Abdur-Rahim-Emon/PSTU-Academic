import socket
import random
import time
import os

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999
EOF_MARKER = b"__EOF__"

def start_streaming_server():
    """Starts a connectionless (UDP) streaming server."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))

    print(f"==================================================")
    print(f"[SERVER] UDP Streaming Server Active on {SERVER_IP}:{SERVER_PORT}")
    print(f"==================================================")

    while True:
        # Wait for client request
        data, client_addr = server_socket.recvfrom(1024)
        requested_file = data.decode('utf-8').strip()
        print(f"\n[SERVER] Received request from {client_addr} for: '{requested_file}'")

        # Validate file existence
        if not os.path.exists(requested_file):
            server_socket.sendto(b"ERROR: File not found", client_addr)
            print(f"[SERVER] File '{requested_file}' not found. Error sent.")
            continue

        # Signal ready status to client
        server_socket.sendto(b"OK", client_addr)
        file_size = os.path.getsize(requested_file)
        print(f"[SERVER] Streaming '{requested_file}' ({file_size} bytes)...")

        bytes_sent = 0
        packet_count = 0

        with open(requested_file, "rb") as media_file:
            while True:
                # Generate random payload size between 1000 and 2000 bytes
                chunk_size = random.randint(1000, 2000)
                chunk = media_file.read(chunk_size)

                # End of file reached
                if not chunk:
                    break

                # Send data chunk as UDP datagram packet
                server_socket.sendto(chunk, client_addr)
                bytes_sent += len(chunk)
                packet_count += 1

                # Tiny pacing delay to prevent UDP buffer drop on local loopback
                time.sleep(0.001)

            # Transmit End-Of-File marker packet
            server_socket.sendto(EOF_MARKER, client_addr)

        print(f"[SERVER] Transfer complete: Sent {bytes_sent} bytes in {packet_count} packets.")

if __name__ == "__main__":
    start_streaming_server()