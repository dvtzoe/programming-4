import socket

import canchatServer  # pyright: ignore[reportImplicitRelativeImport]

HOST = canchatServer.HOST
PORT = canchatServer.PORT


def handle_client(sock: socket.socket, addr: tuple[str, int]) -> None:
    """Receive data from the client via sock and echo it back"""
    try:
        msg = canchatServer.recv_msg(sock)  # Blocks until received
        # complete message
        print("{}: {}".format(addr, msg))
        canchatServer.send_msg(sock, msg)  # Blocks until sent
    except (ConnectionError, BrokenPipeError):
        print("Socket error")
    finally:
        print("Closed connection to {}".format(addr))
        sock.close()


if __name__ == "__main__":
    listen_sock = canchatServer.create_listen_socket(HOST, PORT)
    addr: tuple[str, int] = listen_sock.getsockname()  # pyright: ignore[reportAny]
    print("Listening on {}".format(addr))

    while True:
        client_sock, addr = listen_sock.accept()  # pyright: ignore[reportAny]
        print("Connection from {}".format(addr))
        handle_client(client_sock, addr)
