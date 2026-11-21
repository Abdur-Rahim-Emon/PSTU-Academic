sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock              → your socket
setsockopt()      → set a socket option
SOL_SOCKET        → option is at socket level
SO_REUSEADDR      → reuse local address
1                 → enable it

Server starts
    ↓
Port 5000 is used
    ↓
Server stops
    ↓
You immediately start it again
    ↓
❌ Address already in use


1. with for the socket

Create the socket, use it inside the with block, and automatically close it when the block finishes.

  f.flush()  # Force write data to disk immediately

  with conn, open(OUTPUT_FILE, 'wb') as f: # with used here for that automatically cloese resources when finished
    # w= write( creates a new file or overwrite an existing one) b= binary model