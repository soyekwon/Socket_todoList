import socket


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

todoList = ["컴네 플젝", "DB report"]

# 무한루프를 돌면서 
while True:

    # 클라이언트가 보낸 데이터 수신, 최대 1024
    data = client_socket.recv(1024)

    # 빈 문자열을 수신하면 루프 중지
    if not data:
        break

    request_data = data.decode().split()
    print(request_data)
    method = request_data[0]
    
    todos = "\n"

    for i in range(len(todoList)):
        todos += todoList[i]
        todos += "\n"

    if method == "GET":
        response_data = "{} 200 OK\n\nTodoList: {}".format(method, todos)
    elif method == "POST":
        new_todo = request_data[19].split(':')[1]  # 추가할 todo 내용
        if new_todo == "":  # no_content 이면 
            response_data = "{} 204 No Content\n".format(method)
        else:
            todoList.append(new_todo)  # todo 추가
            response_data = "{} 201 Created\n".format(method)
    elif method == "PUT":
        update_todo = request_data[19].split(':')[1]  #  수정할 todo 내용
        idx = int(request_data[20])  # 수정할 index 
        if todoList[idx-1] == update_todo: # 입력한 todo와 원래 todo와 같은 내용이면
            response_data = "{} 304 Not Modified because of same content\n".format(method)
        else:
            todoList[idx-1] = update_todo  # todo list 수정
            response_data = "{} 202 Accepted\n".format(method)
    elif method == "DELETE":
        idx = int(request_data[19].split(':')[1])  #  수정할 todo 내용
        if idx > len(todoList):  # index의 범위를 벗어나면 
            response_data = "{} 400 Bad Request because of out of index\n".format(method)
        else:
            del todoList[idx-1]
            response_data = "{} 200 OK\n".format(method)
    else:  # other method 입력하면
        response_data = "{} 405 Method Not Allowed\n".format(method)
    # 받은 문자열을 다시 클라이언트로 전송(에코) 
    print(response_data)
    client_socket.send(response_data.encode())
    print("데이터를 클라이언트에게 보냈습니다.")


# 소켓을 닫습니다.
client_socket.close()
server_socket.close()