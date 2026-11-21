import socket

VALID_OPERATORS = {'*', '/', '%', '+', '-'}

def run_client(host='127.0.0.1', port=65432):
    """Prompts user for input and connects to the Remote Calculator Server."""
    print("=== Remote Calculator Client ===")
    
    try:
        # Input Validation
        num1 = int(input("Enter first integer: "))
        
        op = input("Enter operation (*, /, %, +, -): ").strip()
        while op not in VALID_OPERATORS:
            print("Invalid operator! Please choose from: *, /, %, +, -")
            op = input("Enter operation (*, /, %, +, -): ").strip()

        num2 = int(input("Enter second integer: "))

        # Package payload as "num1,op,num2"
        payload = f"{num1},{op},{num2}"

        # Connect and send to server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            client_socket.sendall(payload.encode('utf-8'))

            # Receive result from server
            response = client_socket.recv(1024).decode('utf-8')
            
            print("--------------------------------")
            print(f"Result from Server: {response}")
            print("--------------------------------")

    except ValueError:
        print("\nError: Invalid input. Please enter valid integer numbers.")
    except ConnectionRefusedError:
        print("\nError: Could not connect to server. Ensure 'server.py' is running.")

if __name__ == "__main__":
    run_client()