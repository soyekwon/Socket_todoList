> ## **Socket programming project (TCP base)** 

이번 프로젝트는 tcp기반 소켓 통신을 활용하여 다양한 request를 보내고 response를 받는 과정을 진행해보는 프로젝트이다. 내 프로젝트는 소켓 통신을 이용하여 _**Todo List**_를 만들었다. 파일 입출력을 통해 정보를 저장하고 불러오고 수정할 수 있다. 

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
