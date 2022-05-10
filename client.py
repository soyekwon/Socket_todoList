import socket

# HOST = '172.30.1.46'
HOST = '127.0.0.1'  # 서버의 주소 localhost
PORT = 9999  # 서버에서 지정해 놓은 포트 번호

# 소켓 객체 생성(주소 체계 -> IPv4, SOCK_STREAM -> TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 지정한 HOST와 PORT를 사용하여 서버와 연결
client_socket.connect((HOST, PORT))

while True:
    print("")
    print("")
    print("==============================================  SoyE Todo List  ========================================")
    print("| 1. todo list 불러오기(GET) ", "2. 추가(POST) ", "3. 수정(PUT) ", "4. 삭제(DELETE)", "5. header 요청(HEAD)", "6. 종료")
    num = int(input("| input number: "))
    todo = ""

    if num == 1:
        # request message 생성
        request_data = "GET / HTTP/1.1\r\nHost: 127.0.0.1/\r\nContent-Type: text/html\r\nConnection: keep-alive\r\nContent-Length: {}\r\n\r\n message:{}"
    elif num == 2:
        todo = input("| Add todo (공백없이 입력): ")
        request_data = "POST / HTTP/1.1\r\nHost: 127.0.0.1/\r\nContent-Type: text/html\r\nConnection: keep-alive\r\nContent-Length: {}\r\n\r\n message:{}"
    elif num == 3:
        todo_num = input("| Input update todo number: ")
        todo = input("| Input update todo (공백없이 입력): ")
        todo += " "
        todo += todo_num
        request_data = "PUT / HTTP/1.1\r\nHost: 127.0.0.1/\r\nContent-Type: text/html\r\nConnection: keep-alive\r\nContent-Length: {}\r\n\r\n message:{}"
    elif num == 4:
        todo = input("| Input delete todo number:")
        request_data = "DELETE / HTTP/1.1\r\nHost: 127.0.0.1/\r\nContent-Type: text/html\r\nConnection: keep-alive\r\nContent-Length: {}\r\n\r\n message:{}"
    elif num == 5:
        request_data = request_data = "HEAD / HTTP/1.1\r\nHost: 127.0.0.1/\r\nContent-Type: text/html\r\nConnection: keep-alive\r\nContent-Length: {}\r\n\r\n message:{}"
    elif num == 6:
        break

    request_data = request_data.format(len(todo), todo)  # request message fomatting
    client_socket.send(request_data.encode('utf-8'))  # 데이터 전송

    print("|")

    data = client_socket.recv(1024)  # 데이터 수신
    response_data_header = data.decode().split("\r\n\r\n")[0]  # response message에서 header부분 추출

    if num == 1:
        date = response_data_header.split("\r\n")[4].split(":")[1].split(" ")  # header에서 date 추출
        month = date[3].strip()  # date에서 월 추출
        day = date[2].strip()  # date에서 일 추출
        day_of_week = date[1].strip()  # date에서 요일 추출
        response_data_body = data.decode().split("\r\n\r\n")[1].split("\r\n")  # response message에서 body부분 추출
        status_code = response_data_body[0].split(':')[1].lstrip()  # body에서 status code 추출
        todo_list = response_data_body[1].split(':')[1].lstrip().split("\n")   # body에서 todolist 추출

        print("| status code: ", end="")
        print(status_code)
        print("| ")
        # todolist command line UI ...
        print("| ------- " + day_of_week + "day, " + month + " " + day + todo + " |todo list| -------------")
        for i in range(len(todo_list)):
            print("| ", i+1, todo_list[i])
        print("| -----------------------------------------------")

    elif num == 5:  # HEAD method
        response_data_header_list = response_data_header.split("\r\n")
        for i in range(len(response_data_header_list)):
            print("|", response_data_header_list[i])  # response message header 정보 출력 
    else:
        status_code = data.decode().split("\r\n\r\n")[1].split(":")[1]  # body에서 status code 추출
        print("| status code: ", end="")
        print(status_code)
    print("========================================================================================================")


# 소켓을 닫습니다.
client_socket.close()
print("| 연결이 끊어졌습니다.")
