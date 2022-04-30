import socket
import time

# localhost
HOST = '127.0.0.1'
# 포트 번호
PORT = 9999


# 소켓 객체 생성
# 주소 체계(address family)로 IPv4, SOCK_STREAM -> TCP 사용
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 포트 사용중이라 연결할 수 없다는
# WinError 10048 에러 해결를 위해 필요
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


# host와 port 맵핑
server_socket.bind((HOST, PORT))

# 맵핑된 소켓을 연결 요청 대기 상태로 전환
server_socket.listen()

print("대기중입니다... ")

# accept 함수에서 대기하다가 클라이언트가 접속하면 새로운 소켓을 리턴
client_socket, addr = server_socket.accept()

print(addr, " 에서 연결되었습니다.")


# 무한루프를 돌면서
while True:

    # 클라이언트가 보낸 데이터 수신, 최대 1024
    data = client_socket.recv(1024)

    # 빈 문자열을 수신하면 루프 중지
    if not data:
        break

    f = open("todolist.txt", 'r', encoding="UTF-8")  # todolist.txt 열고
    todoList = []

    while True:
        line = f.readline()  # 파일 읽어서
        if not line:
            break  # 더이상 읽을 line이 없으면 종료
        todoList.append(line)  # todoList 리스트에 append

    f.close()

    request_data = data.decode().split()
    method = request_data[0]

    todos = "\n"

    for i in range(len(todoList)):
        todos += todoList[i]

    if method == "GET":
        response_data = "HTTP/1.1 200 OK\r\nDate: {}\r\nServer: python3(windows10)\r\nConnection: Keep-Alive\r\n\r\nstatus_code: {}\r\ntodo: {}".format(time.ctime(time.time()), "200 OK", todos)
    elif method == "POST":
        new_todo = request_data[-1].split(':')[1]  # 추가할 todo 내용
        if new_todo == "":  # no_content 이면
            response_data = "HTTP/1.1 204 No Content\r\nDate: {}\r\nServer: python3(windows10)\r\nConnection: Keep-Alive\r\n\r\nstatus_code: {}".format(time.ctime(time.time()), "204 No Content")
        else:
            f = open("todolist.txt", 'w', encoding="UTF-8")
            for i in range(len(todoList)):
                f.write(todoList[i])
            f.write("\n")
            f.write(new_todo)
            f.close()
            response_data = "HTTP/1.1 201 Created\r\nDate: {}\r\nServer: python3(windows10)\r\nConnection: Keep-Alive\r\n\r\nstatus_code: {}".format(time.ctime(time.time()), "201 Created")
    elif method == "PUT":
        update_todo = request_data[-2].split(':')[1]  # 수정할 todo 내용
        idx = int(request_data[-1])  # 수정할 index
        if todoList[idx-1] == update_todo:  # 입력한 todo와 원래 todo와 같은 내용이면
            response_data = "HTTP/1.1 304 Not Modified \r\nDate: {}\r\nServer: python3(windows10)\r\nConnection: Keep-Alive\r\n\r\nstatus_code: {}".format(time.ctime(time.time()), "304 Not Modified")
                
        else:
            f = open("todolist.txt", 'w', encoding="UTF-8")
            for i in range(idx-1):
                f.write(todoList[i])
            f.write(update_todo)
            f.write("\n")
            for i in range(idx, len(todoList)):
                f.write(todoList[i])
            f.close()
            response_data = "HTTP/1.1 202 Accepted\r\nDate: {}\r\nServer: python3(windows10)\r\nConnection: Keep-Alive\r\n\r\nstatus_code: {}".format(time.ctime(time.time()), "202 Accepted")
    elif method == "DELETE":
        idx = int(request_data[-1].split(':')[1])  # 수정할 todo 내용
        if idx > len(todoList):  # index의 범위를 벗어나면
            response_data = "HTTP/1.1 400 Bad Request\r\nDate: {}\r\nServer: python3(windows10)\r\nConnection: Keep-Alive\r\n\r\nstatus_code: {}".format(time.ctime(time.time()), "400 Bad Request")
        else:
            del todoList[idx-1]
            f = open("todolist.txt", 'w', encoding="UTF-8")
            for i in range(len(todoList)):
                f.write(todoList[i])
            f.close()
            response_data = "HTTP/1.1 200 OK\r\nDate: {}\r\nServer: python3(windows10)\r\nConnection: Keep-Alive\r\n\r\nstatus_code: {}".format(time.ctime(time.time()), "200 OK")
    elif method == "HEAD":
        response_data = "HTTP/1.1 200 OK\r\nDate: {}\r\nServer: python3(windows10)\r\nConnection: Keep-Alive\r\n\r\nstatus_code: {}".format(time.ctime(time.time()), "200 OK")
    else:  # other method 입력하면
        response_data = "HTTP/1.1 405 Method Not Allowed\r\nDate: {}\r\nServer: python3(windows10)\r\nConnection: Keep-Alive\r\n\r\nstatus_code: {}".format(time.ctime(time.time()), "405 Method Not Allowed")
    # 받은 문자열을 다시 클라이언트로 전송(에코)
    print(response_data)
    client_socket.send(response_data.encode())
    print("데이터를 클라이언트에게 보냈습니다.")


# 소켓을 닫습니다.
client_socket.close()
server_socket.close()
