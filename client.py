import socket
from urllib import response


HOST = '127.0.0.1'  # 서버의 주소
PORT = 9999  # 서버에서 지정해 놓은 포트 번호

# 소켓 객체 생성(주소 체계 -> IPv4, SOCK_STREAM -> TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))  # 지정한 HOST와 PORT를 사용하여 서버와 연결

while True:
    print("")
    print("==============================================  SoyE Todo List  ==============================================")
    print("1. list 불러오기(get) ", "2. todo 추가(post) ", "3. todo 수정(put) ", "4. todo 삭제(delete)", "5. header 요청(head)", "6. 종료")
    num = int(input("input number: "))
    todo = ""

    if num == 1:
        request_data = 'GET / HTTP/1.1\r\nHost: 127.0.0.1:9999\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36\r\nConnection: keep-alive\r\nContent-Length:{}\r\nmessage:{}'
    elif num == 2:
        todo = input("Add todo: ")
        request_data = 'POST / HTTP/1.1\r\nHost: 127.0.0.1:9999\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36\r\nConnection: keep-alive\r\nContent-Length:{}\r\nmessage:{}'
    elif num == 3:
        todo_num = input("Input update todo number: ")
        todo = input("Input update todo: ")
        todo += " "
        todo += todo_num
        request_data = 'PUT / HTTP/1.1\r\nHost: 127.0.0.1:9999\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36\r\nConnection: keep-alive\r\nContent-Length:{}\r\nmessage:{}'
    elif num == 4:
        todo = input("Input delete todo number:")
        request_data = 'DELETE / HTTP/1.1\r\nHost: 127.0.0.1:9999\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36\r\nConnection: keep-alive\r\nContent-Length:{}\r\nmessage:{}'
    elif num == 5:
        request_data = 'HEAD / HTTP/1.1\r\nHost: 127.0.0.1:9999\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36\r\nConnection: keep-alive\r\nContent-Length:{}\r\nmessage:{}'
    elif num == 6:
        break

    request_data = request_data.format(len(todo), todo)
    client_socket.send(request_data.encode('utf-8'))  # 데이터 전송
    data = client_socket.recv(1024)  # 데이터 수신

    print("")

    if num == 1:
        response_data = data.decode().split("\r\n\r\n")[1].split("\r\n")  # response message에서 body부분 추출
        status_code = response_data[0].split(':')[1].lstrip()  # body에서 status code 추출
        print("status code: ", end="")
        print(status_code)
        todo_list = response_data[1].split(':')[1].lstrip()   # body에서 todolist 추출
        print("")
        print("todo list: ")
        print(todo_list)
    elif num == 5:
        response_data = data.decode().split("\r\n\r\n")[0]
        print(response_data)
    else:
        status_code = data.decode().split("\r\n\r\n")[1].split(":")[1]  # body에서 status code 추출
        print("status code: ", end="")
        print(status_code)


# 소켓을 닫습니다.
client_socket.close()
