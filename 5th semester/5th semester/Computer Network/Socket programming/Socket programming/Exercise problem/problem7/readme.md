 sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    """
 | Parameter                  | Meaning                                                            |
| -------------------------- | ------------------------------------------------------------------ |
| `socket.IPPROTO_IP`        | We are setting an **IP-level** option                              |
| `socket.IP_ADD_MEMBERSHIP` | Tell the OS to **join a multicast group**                          |
| `mreq`                     | Contains **which multicast group** and **which network interface** |
    """



    sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_MULTICAST_TTL,
    2
)

TTL = 1 → normally local subnet
TTL = 2 → can cross limited routing hops


sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_MULTICAST_LOOP,
    1
)


1 means:

Allow the sender to receive its own multicast message.


In Python, __init__ means the constructor/initializer method of a class.

self means the current object.