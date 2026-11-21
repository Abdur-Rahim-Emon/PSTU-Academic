import socket

def perform_operation(num1: int, op: str, num2: int) -> str:
    """Performs binary arithmetic operation on two integers."""
    try:
        if op == '+':
            return str(num1 + num2)
        elif op == '-':
            return str(num1 - num2)
        elif op == '*':
            return str(num1 * num2)
        elif op == '/':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            return str(num1 / num2)
        elif op == '%':
            if num2 == 0:
                return "Error: Modulo by zero is not allowed."
            return str(num1 % num2)
        else:
            return f"Error: Unsupported operator '{op}'."
    except Exception as e:
        return f"Error: {str(e)}"

def run_server(host='127.0.0.1', port=65432):
    """Starts the TCP Server to handle remote calculation requests."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Enable immediate address reuse so restarting doesn't cause port errors
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen()
        
        print(f"[SERVER] Calculator Server running on {host}:{port}...")
        print("[SERVER] Press Ctrl + C at any time to shut down the server.\n")

        try:
            while True:
                conn, addr = server_socket.accept()
                with conn:
                    print(f"[SERVER] Connected by {addr}")
                    data = conn.recv(1024).decode('utf-8')
                    
                    if not data:
                        continue

                    try:
                        # Unpack data sent as "num1,op,num2"
                        parts = data.split(',')
                        num1 = int(parts[0])
                        op = parts[1]
                        num2 = int(parts[2])

                        print(f"[SERVER] Received request: {num1} {op} {num2}")
                        result = perform_operation(num1, op, num2)
                    except (ValueError, IndexError):
                        result = "Error: Invalid data format received from client."

                    # Send result back to client
                    conn.sendall(result.encode('utf-8'))
                    print(f"[SERVER] Sent result: {result}\n")

        except KeyboardInterrupt:
            print("\n[SERVER] Shutdown signal (Ctrl + C) received. Closing server...")

if __name__ == "__main__":
    run_server()