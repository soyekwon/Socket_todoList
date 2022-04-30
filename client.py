import socket


# 서버의 주소
HOST = '127.0.0.1'  
# 서버에서 지정해 놓은 포트 번호
PORT = 9999       


# 소켓 객체 생성
# 주소 체계(address family) -> IPv4, SOCK_STREAM -> TCP 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 지정한 HOST와 PORT를 사용하여 서버와 연결 
client_socket.connect((HOST, PORT))

while True:
	print("==========================================  SoyE Todo List  ==========================================")
	print("1. list 불러오기(get) ", "2. todo 추가(post) ", "3. todo 수정(put) ", "4. todo 삭제(delete)", "5. header 요청(head)", "6. 종료")
	num = int(input("input number: "))
	todo = ""

	if num == 1:
		request_data = 'GET / HTTP/1.1\r\nHost: 127.0.0.1:9999\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36\r\nContent-Length:{}\r\nmessage:{}'
	elif num == 2:
		todo = input("Add todo: ")
		request_data = 'POST / HTTP/1.1\r\nHost: 127.0.0.1:9999\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36\r\nContent-Length:{}\r\nmessage:{}'
	elif num == 3:
		# out of index 일때 에러 추가
		todo_num = input("Input update todo number: ")
		todo = input("Input update todo: ")
		todo += " "
		todo += todo_num
		request_data = 'PUT / HTTP/1.1\r\nHost: 127.0.0.1:9999\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36\r\nContent-Length:{}\r\nmessage:{}'
	elif num == 4:
		todo = input("Input delete todo number:")
		request_data = 'DELETE / HTTP/1.1\r\nHost: 127.0.0.1:9999\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36\r\nContent-Length:{}\r\nmessage:{}'
	elif num == 5:
		request_data = 'HEAD / HTTP/1.1\r\nHost: 127.0.0.1:9999\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36\r\nContent-Length:{}\r\nmessage:{}'
	elif num == 6:
		break

	request_data = request_data.format(len(todo), todo)
	# 데이터 전송
	client_socket.send(request_data.encode('utf-8'))
	# 데이터 수신
	data = client_socket.recv(1024)
	print("")
	print("response message:", end=" ")
	print(data.decode())	


# 소켓을 닫습니다.
client_socket.close()