# 웹 서버 / 웹 애플리케이션 서버

###### 부제 : Django 에서 사전 설정을 하지 않으면 정적 파일을 처리하지 않는 이유

위의 질문에 대해 얘기하자면, Django 자체는 웹 서버가 아니고 웹 애플리케이션 프레임워크 이기 때문이다.

Django 개발 환경에서 간소하게 웹 서버 처럼 동작시킬 수는 있지만, 보안 및 성능 이슈가 있을 수 있기 때문에 권장하지 않는다(라고 공식적으로 얘기하고 있다).



웹 서버와 웹 애플리케이션 서버의 차이를 알기 이전에, 필요한 지식인 정적 컨텐츠와 동적 컨텐츠의 차이에 대해 짚고 넘어가야 한다.

------



정적 페이지(Static pages) 와 동적 페이지 (Dynamic pages) 의 차이



- 정적 페이지
  1. html, css, javascript, image 같은 컴퓨터에 저장되어있는 파일들
  2. 해당되는 요청이 올 때마다 미리 저장되어있던 그대로 반환이 된다.

- 동적 페이지
  1. DB에 따라 달라지거나 서버 내부 로직에 의해 가공된 것들
  2. 해당되는 요청이 오면 조건에 맞게 만들어져서 반환된다.

------

웹 서버와 웹 애플리케이션 서버의 차이는?



- 웹 서버 (Web server) 의 역할
  1. 정적 컨텐츠를 클라이언트에게 전달해준다.
  2. 클라이언트의 요청을 웹 애플리케이션 서버에 전달하고, 웹 애플리케이션이 처리하여 반환한 요청을 다시 클라이언트에게 돌려준다.

- 웹 애플리케이션 서버 (Web Application Server, WAS) 의 역할
  1. 클라이언트로부터 온 동적 컨텐츠 요청을 만들어 반환한다.

------

정말 간략하게 표현하자면,



> 클라이언트 - 웹서버 - 웹 애플리케이션 서버



위와 같은 구조로 표현할 수 있고, 요청의 종류에 따라서 WAS 까지 가는지 혹은 웹서버에서 처리하는지가 결정된다.

위 구조에서 어떤 사람은 웹 서버를 제외한 채,



> 클라이언트 - WAS



위와 같은 구조로 사용하는 경우도 있지만,

그렇게 되면 웹 서버를 분리하여 사용시 (이것을 **리버스 프록시 구조**라고 한다) 얻을 수 있는 다음의 이점들을 얻을 수 없다.



- 리버스 프록시 구조를 통해 얻을 수 있는 이점들
  1. 효율성 강화
     - WAS 는 정적 컨텐츠 처리 같은 사소한 작업까지 하기에는 너무 바쁘다.
     - 웹 서버는 정적 파일(HTML, CSS, JS 등)을 처리하고, 동적인 데이터를 처리하는 WAS는 백엔드 로직을 처리하므로 두 서버를 분리해서 부하를 분산함으로써 성능을 향상시킬 수 있다.
  2. 보안성 강화
     - 웹 서버는 클라이언트와의 통신을 담당하고 WAS는 애플리케이션 로직을 처리하므로, 두 서버를 분리함으로써 보안성이 높아진다.
  3. 확장성 강화
     - 웹 서버와 WAS를 분리함으로써 애플리케이션을 확장하는 데 유연성을 높일 수 있다.
  4. 관리 용이성
     - 각 서버를 독립적으로 관리하는 것으로 서버 운영, 유지 보수, 문제 해결 등을 더욱 쉽게 할 수 있다.

---

웹 서버를 구축하는데 사용되는 프로그램은 대중적으로 다음과 같다.

1. Apache
2. Nginx
3. IIS
   - 참조 : https://ko.hostadvice.com/marketshare/server/