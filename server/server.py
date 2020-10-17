import socket

HOST = "127.0.0.1"

PORT = 9999  # 1 - 65535

# 주소 체계(address family)로 IPv4 (socket.AF_INET = IPv4),
# 소켓 타입으로 TCP (socket.SOCK_STREAM = TCP)
# socket.SOCK_DGRAM = UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 포트 사용중이라 연결할 수 없다는
# WinError 10048 에러 해결를 위해 필요합니다.
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind 함수는 소켓을 특정 네트워크 인터페이스와 포트 번호에 연결하는데 사용됩니다.
# HOST는 hostname, ip address, 빈 문자열 ""이 될 수 있습니다.
# 빈 문자열이면 모든 네트워크 인터페이스로부터의 접속을 허용합니다.
server_socket.bind((HOST, PORT))
# 서버가 클라이언트의 접속을 허용하도록 합니다.
server_socket.listen()
# accept 함수에서 대기하다가 클라이언트가 접속하면 새로운 소켓을 리턴합니다.
client_socket, addr = server_socket.accept()

# 접속한 클라이언트의 주소입니다.
print("Connected by", addr)

while True:

    data = client_socket.recv(1024)

    if not data:
        break

    print("Received from", addr, data.decode())

    client_socket.sendall(data)

client_socket.close()
server_socket.close()
