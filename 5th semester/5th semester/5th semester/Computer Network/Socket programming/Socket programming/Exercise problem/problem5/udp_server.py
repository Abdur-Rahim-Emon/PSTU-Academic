import socket

HOST = '127.0.0.1'
PORT = 65433
MAX_BUFFER = 1000  # Max 1000 characters per message

def run_udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))

    print(f"--- UDP Server Listening on {HOST}:{PORT} ---")
    print("Waiting for incoming datagram... (Press Ctrl+C to exit)\n")

    try:
        while True:
            # 1. Receive up to 1000 characters from client
            data, client_addr = server_socket.recvfrom(MAX_BUFFER)
            print(f"Client ({client_addr[0]}:{client_addr[1]}): {data.decode('utf-8')}")

            # 2. Type response (Truncate if user inputs >1000 characters)
            reply = input("Server: ")[:MAX_BUFFER]
            server_socket.sendto(reply.encode('utf-8'), client_addr)
            print("Waiting for client reply...\n")

    except KeyboardInterrupt:
        print("\n[+] UDP Server closed by user (Ctrl+C).")
    finally:
        server_socket.close()

if __name__ == "__main__":
    run_udp_server()