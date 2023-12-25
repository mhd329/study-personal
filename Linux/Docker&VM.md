# Docker와 VM의 차이

**가상화 기술의 변천사**

------

- VM(Virtual machine)
  - 가상화 기술이 등장하기 이전, 하나의 컴퓨터에서는 오직 하나의 OS만 작동시킬 수 있었다.
  - 이로 인해 자원의 많은 낭비가 생겼다.
  - 이러한 잉여 자원의 효율적인 사용을 위해 하나의 컴퓨터에 여러 개의 OS를 설치해서 활용하는 가상화 기술이 등장했다.
  - 가상화 기술은 기존 운영체제 위에 하드웨어를 에뮬레이션 하고, 그 위에 운영체제를 올리는 것이다.
  - Hypervisor 기반의 가상화 기술이 가장 많이 사용되었다.
  - VM간에는 분리되어있기 때문에 오류가 발생해도 다른 VM에 영향이 없다는 것이 가상화 기술의 장점이다.

> Hypervisor:
> 논리적으로 분할된 어떤 공간에서 독립적인 환경을 구성하고 호스트 OS 커널에서 게스트 OS를 관리하는 기술

------

- Docker

  - 기존 가상화 기술은 각각의 모든 공간에 별도의 게스트 OS를 설치해야 하는 불편함이 있었다.
  - 하드웨어 에뮬레이션 없이, 호스트 OS의 커널만을 공유하고 나머지는 격리되어있는 각각의 프로세스를 만드는 기술이 Docker 이다.
  - 여기에는 리눅스의 namespace가 활용된다.

- Docker Container

  - 리눅스의 네임스페이스 기능으로 격리해놓은 공간(작업단위)

  - 네임스페이스 기능을 사용하기 위해 리눅스라는 호스트 OS 위에서 Docker 엔진이 실행된다.

  - Docker 엔진은 네임스페이스 기능으로 각각의 프로세스를 생성하고(

    Container들을 만들고), 그것들은 Docker Engine을 통해 리눅스 커널을 공유한다.

    - 즉 Container는 하나의 프로세스이고, Docker image는 그 프로세스를 실행하기 위한(==Container를 만들기 위한) 파일 패키지이다.

------



![img](https://blog.kakaocdn.net/dn/bo4OJt/btstCFgZUl5/iyEZt9Ilec347J2x8r80K1/img.jpg)

---

위 그림은 Docker 공식문서에서 설명하고 있는 자료인데, 나는 아래와 같이 이해했다.

![img](https://blog.kakaocdn.net/dn/tBAGL/btstMzz1xy5/2YWKIy1asvLGpIWdKJPUhk/img.png)

- 왼쪽부터 VM / Linux Docker / Windows Docker

---

위와 같은 모습으로 이해했다.



기존의 VM이 위와 같은 방식으로 되었다면, Linux에서의 Docker는 Guest OS를 설치하는 대신, Docker 엔진이 호스트 OS의 커널만 공유해주면서 컨테이너들을 만들어 가는 방식이다.



그리고 Windows 에서 Docker를 사용하려면, 우선 Docker는 Linux 기반 기술이기 때문에 Hypervisor로 에뮬레이션 한 다음 Guest OS로 Linux를 설치해주고, 그 위에 Docker를 설치해서 작동한다.



(정확히는 Linux를 설치하는 게 아니라 Docker만을 구동시키기 위한 리눅스의 필수 기능들만 가져와서 구성하는 것으로 보인다.)

=> [https://answers.microsoft.com/ko-kr/windows/forum/all/windows-%EA%B8%B0%EB%8A%A5/492c8c5c-df88-4644-9f71-2042b9675728](https://answers.microsoft.com/ko-kr/windows/forum/all/windows-기능/492c8c5c-df88-4644-9f71-2042b9675728))