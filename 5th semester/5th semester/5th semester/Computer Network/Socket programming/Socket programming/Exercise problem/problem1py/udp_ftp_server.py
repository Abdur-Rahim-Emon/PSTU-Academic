import socket
HOST = '127.0.0.1'
PORT = 6000
OUTPUT_FILE = 'received_udp_file.txt'

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))
    print(f"UDP FTP Server listening on {HOST}:{PORT}...")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        while True:
            data, addr = server_socket.recvfrom(1024) # 1024 bytes up to can  recieve  data means the txt file chunk recieved
            line = data.decode('utf-8')

            # Check for custom End-Of-File marker
            if line == "__EOF__":
                print("EOF signal received. File transfer complete!")
                break

            f.write(line + '\n')
            f.flush()  # Force write data to disk immediately
            print(f"Received line: {line}")

    print(f"File saved as '{OUTPUT_FILE}'.")