# Board - Server - Locust

- 설치, 실행 방법 <br>
  - Locust 설치: pip install locust 
  - 실행: locust -f AddPosts.py, 혹은  locust -f "C:\경로전체\Board-Server-Locust\venv\AddPost.py"
<br><br>
- 8090으로 들어간 후
  host 는 http://127.0.0.1:8080, localhost 로 실행해준다. 
<br><br>
- 시나리오
  - stress test: 50명의 동시 사용자가 5분간 초당 50번 호출, 사용자를 50씩 늘려 테스트한다.(최대 500명)
  - spike test: 50명의 유저에서 시작, 접속자수가 초당 50씩 늘어난다. 접속자수가 1000이 될 때 까지 실행.
  - endurance test: 초당 100명이 10분간 접속한다.




자세한 설명과 테스트 방법 : https://wonder-why.tistory.com/189, https://wonder-why.tistory.com/190

<참고, 기존 Board-Server 를 run 하고 실행해야한다. >