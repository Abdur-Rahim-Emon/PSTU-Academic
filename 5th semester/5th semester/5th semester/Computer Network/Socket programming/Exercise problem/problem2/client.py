import socket
import os

HOST = '127.0.0.1'
PORT = 65432
BUFFER_SIZE = 1000

def request_file(raw_filename):
    # Strip quotes if the user pasted a path with quotes
    clean_filename = raw_filename.strip("'\"")
    output_filename = f"downloaded_{os.path.basename(clean_filename)}"

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
        print(f"[CLIENT] Connected to server at {HOST}:{PORT}")

        # Send path string to server
        client_socket.sendall(clean_filename.encode('utf-8'))
        print(f"[CLIENT] Requesting '{clean_filename}'...")

        error_occurred = False

        with open(output_filename, 'wb') as f:
            while True:
                chunk = client_socket.recv(BUFFER_SIZE)
                if not chunk:
                    break
                
                if chunk.startswith(b"ERROR:"):
                    print(f"[CLIENT] Server error: {chunk.decode('utf-8')}")
                    error_occurred = True
                    break

                f.write(chunk)

        # Cleanup outside of the file block to avoid Windows file locks
        if error_occurred:
            if os.path.exists(output_filename):
                os.remove(output_filename)
        else:
            print(f"[CLIENT] Download complete! File saved as '{output_filename}'.")

    except ConnectionRefusedError:
        print("[CLIENT] Could not connect to the server. Is server.py running?")
    except Exception as e:
        print(f"[CLIENT] Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    file_to_download = input("Enter the filename or path to download: ").strip()
    if file_to_download:
        request_file(file_to_download)
    else:
        print("Filename cannot be empty.")