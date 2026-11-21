import socket
import time

HOST = '127.0.0.1'
PORT = 6000
INPUT_FILE = 'send_udp_file.txt'  # Ensure this file exists before running

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    print("Sending file line-by-line over UDP...")

    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            clean_line = line.rstrip('\r\n')
            
            # Send single line as a datagram
            client_socket.sendto(clean_line.encode('utf-8'), (HOST, PORT))
            print(f"Sent line: {clean_line}")

            time.sleep(0.01)  # Brief delay to prevent packet drop on local buffer

    # Send EOF marker so server knows when to stop listening
    client_socket.sendto(b"__EOF__", (HOST, PORT))

    print("File transfer finished successfully.")