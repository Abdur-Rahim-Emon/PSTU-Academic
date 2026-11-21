import socket

HOST = '127.0.0.1'
PORT = 65433
MAX_BUFFER = 1000  # Max 1000 characters per message

def run_udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_addr = (HOST, PORT)

    print(f"--- UDP Client Ready to send to {HOST}:{PORT} ---")
    print("Type your message (Press Ctrl+C to exit).\n")

    try:
        while True:
            # 1. Type message (Truncate if user inputs >1000 characters)
            msg = input("Client: ")[:MAX_BUFFER]
            client_socket.sendto(msg.encode('utf-8'), server_addr)

            # 2. Wait for reply before allowing another send
            print("Waiting for server reply...\n")
            data, _ = client_socket.recvfrom(MAX_BUFFER)
            print(f"Server: {data.decode('utf-8')}")

    except KeyboardInterrupt:
        print("\n[+] UDP Client closed by user (Ctrl+C).")
    finally:
        client_socket.close()

if __name__ == "__main__":
    run_udp_client()