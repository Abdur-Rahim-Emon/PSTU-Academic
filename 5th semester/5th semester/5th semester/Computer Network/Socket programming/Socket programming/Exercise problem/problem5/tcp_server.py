import socket

HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Arbitrary non-privileged port

def run_tcp_server():
    # Create TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   #reuse the port after terminating the program it still allocate for the port to avoid it used this line code
   #Says the option belongs to the socket level
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_socket.bind((HOST, PORT))
    server_socket.listen(1) # listening only one client
    
    print(f"--- TCP Server Started on {HOST}:{PORT} ---")
    print("Waiting for client connection... (Press Ctrl+C to exit)\n")

    try:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
        print("Waiting for client to send a message...\n")

        while True:
            # 1. Receive message from client
            data = conn.recv(1024)
            if not data:
                break
            print(f"Client: {data.decode('utf-8')}")

            # 2. Type response and send (Triggers on "Enter")
            reply = input("Server: ")
            conn.sendall(reply.encode('utf-8'))
            print("Waiting for client reply...\n")

    except KeyboardInterrupt:
        print("\n[+] TCP Server closed by user (Ctrl+C).")
    finally:
        if 'conn' in locals(): # conn creates or not so that skip error
            conn.close()
        server_socket.close()

if __name__ == "__main__":
    run_tcp_server()