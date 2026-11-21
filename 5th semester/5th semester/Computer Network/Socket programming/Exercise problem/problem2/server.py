import socket
import threading
import time
import os

HOST = '127.0.0.1'
PORT = 65432
BUFFER_SIZE = 1000
SLEEP_TIME = 0.2

def handle_client_file_transfer(client_socket, raw_filename):
    thread_name = threading.current_thread().name
    
    # Strip quotes (' and ") and normalize directory slashes for the OS
    filename = os.path.normpath(raw_filename.strip("'\""))
    print(f"[{thread_name}] Handling request for file: '{filename}'")

    try:
        # Check if the file exists at the given path
        if not os.path.isfile(filename):
            print(f"[{thread_name}] Error: File '{filename}' not found.")
            client_socket.sendall(b"ERROR: File not found")
            return

        # Read and send file chunks
        with open(filename, 'rb') as f:
            total_bytes_sent = 0
            while True:
                chunk = f.read(BUFFER_SIZE)
                if not chunk:
                    break
                
                client_socket.sendall(chunk)
                total_bytes_sent += len(chunk)
                time.sleep(SLEEP_TIME)

        print(f"[{thread_name}] Successfully sent '{filename}' ({total_bytes_sent} bytes).")

    except Exception as e:
        print(f"[{thread_name}] Connection error: {e}")
    finally:
        client_socket.close()
        print(f"[{thread_name}] Socket closed.")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"[SERVER] File server listening on {HOST}:{PORT}...")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"\n[SERVER] New connection from {client_address}")

            # Read requested file path from client
            filename = client_socket.recv(1024).decode('utf-8').strip()

            client_thread = threading.Thread(
                target=handle_client_file_transfer,
                args=(client_socket, filename)
            )
            client_thread.start()

    except KeyboardInterrupt:
        print("\n[SERVER] Server shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()