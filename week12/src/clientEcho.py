import socket
import sys

import canchatServer  # pyright: ignore[reportImplicitRelativeImport]

HOST = sys.argv[-1] if len(sys.argv) > 1 else "161.246.52.26"
PORT = canchatServer.PORT

if __name__ == "__main__":
    while True:
        sock = None
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
            print(f"\nConnected to {HOST}:{PORT}")
            print("Type message, enter to send, 'q' to quit")
            msg = input()
            if msg == "q":
                break
            canchatServer.send_msg(sock, msg)  # Blocks until sent
            print(f"Sent message: {msg}")
            msg = canchatServer.recv_msg(sock)
            # Block until
            # received complete
            # message
            print("Received echo: " + msg)
        except ConnectionError:
            print("Socket error")
            break
        finally:
            if sock:
                sock.close()
            print("Closed connection to server\n")
