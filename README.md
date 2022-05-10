> ## **Socket programming project (TCP base)** 

이번 프로젝트는 tcp기반 소켓 통신을 활용하여 다양한 request를 보내고 response를 받는 과정을 진행해보는 프로젝트이다. 
내 프로젝트는 소켓 통신을 이용하여 _**Todo List**_를 만들었다. 파일 입출력을 통해 정보를 저장하고 불러오고 수정할 수 있다. 

> ### 동작환경

![](https://velog.velcdn.com/images/soyekwon/post/6d5e778a-6879-4340-8a7c-289d5e3bb754/image.svg)

server와 client 모두 windows10에서 진행하였다. 

> ### 기능 명세

1. GET 
 - 200 (success) : todolist.txt에서 todolist정보를 읽어온다. 

2. POST
- 201 (created) : todo정보를 todolist.txt에 추가한다. 
- 204 (no content) : 아무 정보 없이(빈 문자열)을 입력하면 204(no content)를 반환한다. 

3. PUT
- 202 (accepted) : 조건에 맞게 입력하면 todolist.txt에 있는 정보를 수정한다. 
- 304 (not modified) : 수정하려는 정보와 입력한 정보가 일치하면 304(not modified)를 반환한다. 

4. DELETE
- 200 (success) : 조건에 맞게 입력하면 todolist.txt에서 입력한 인덱스에 해당하는 정보를 삭제한다.
- 400 (bad request) : 인덱스 범위를 벗어나는 인덱스 값을 입력하면 400(bad request)를 반환한다.
5. HEAD
- 200 (success) : 헤더 정보를 반환한다. 

> ### 실행화면

**command line UI** 
<br><br>
![](https://velog.velcdn.com/images/soyekwon/post/41447fa1-d468-4514-8ea7-ab81c550132e/image.jpg)

**GET 요청** (client.py)
<br><br>
![](https://velog.velcdn.com/images/soyekwon/post/c47a531f-ddcd-4db5-9aa8-87c3cefecb89/image.jpg)

**GET 응답** (server.py) - 200 OK
<br><br>
![](https://velog.velcdn.com/images/soyekwon/post/0c046aac-1890-40f9-a9b5-415631e82994/image.jpg)

**POST 요청** (client.py)
<br><br>
![](https://velog.velcdn.com/images/soyekwon/post/b2baa989-7f10-4e64-b15c-f9d28f2f2ebd/image.jpg)

**POST 응답** (server.py) - 201 Created
<br><br>
![](https://velog.velcdn.com/images/soyekwon/post/a71ca173-72a6-427a-98d6-9de54cd1a229/image.jpg)

**POST 요청** (client.py) - 빈 문자열 입력 
<br><br>
![](https://velog.velcdn.com/images/soyekwon/post/38b21a3a-6b96-471b-829c-8a86f34f8f52/image.jpg)

**POST 응답** (server.py) - 204 No Content
<br><br>
![](https://velog.velcdn.com/images/soyekwon/post/8f016269-938d-4298-b82a-3ada52274bae/image.jpg)

**PUT 요청** (client.py)
<br><br>
![](https://velog.velcdn.com/images/soyekwon/post/1300b495-8974-4d2f-895e-30b54d155354/image.jpg)

**PUT 요청** (client.py) - 같은 내용 입력
<br><br>
![](https://velog.velcdn.com/images/soyekwon/post/3acde27d-2a3d-44a1-adc8-7cf510da3a44/image.jpg)

**PUT 응답** (server.py) - 304 Not Modified
<br><br>
![](https://velog.velcdn.com/images/soyekwon/post/3c1fd06f-4e52-467d-bd79-b59351e34e8d/image.jpg)

**DELETE 요청** (client.py) 
<br><br>
![](https://velog.velcdn.com/images/soyekwon/post/792b4a63-0ac9-4748-aa2b-d4c039a6cdf9/image.jpg)

**DELETE 요청** (client.py) - index 범위를 벗어난 index 입력
<br><br>
![](https://velog.velcdn.com/images/soyekwon/post/ce66dd3e-4350-4acd-a84f-0711f5a65775/image.jpg)

**DELETE 응답** (server.py) - 400 Bad Request
<br><br>
![](https://velog.velcdn.com/images/soyekwon/post/6c221f02-fe87-422b-96c2-f4ce23fb42b9/image.jpg)

**HEAD 요청** (client.py) 
<br><br>
![](https://velog.velcdn.com/images/soyekwon/post/cd5db455-1dc2-477b-b253-5d98a0b3d5c9/image.jpg)

**HEAD 응답** (server.py) - 200 OK
<br><br>
![](https://velog.velcdn.com/images/soyekwon/post/cd7904c1-25cf-449f-b169-7db65918e2ee/image.jpg)

