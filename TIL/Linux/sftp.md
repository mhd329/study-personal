# mac과 AWS EC2를 sftp로 연결하기

AWS EC2 instance는 ubuntu 22.04 버전으로 생성했다.

------

1. 아래와 같이 VS Code SFTP 확장을 설치한다.
   ![img](https://blog.kakaocdn.net/dn/M9ksg/btsys6fXiYN/uMgDaopLT0psmmwrTVHXQK/img.png)

2. 설치 후 fn + f1을 눌러 config를 연다.
   ![img](https://blog.kakaocdn.net/dn/F18Q8/btsysrkn8rs/HaUUGaLHSIdzN5kVEkWCck/img.png)

3. 자신의 환경에 맞게 설정을 한다.

   ![img](https://blog.kakaocdn.net/dn/rdIJf/btsytZHu5Vr/R2avvBB3N69bCpvKseBYhK/img.png)

   1. name
      임의로 정해도 되는 서버의 이름이다.
      fn + f1을 누르면 나오는 SFTP: List All에서 표시될 이름을 정한다.
   2. host
      EC2 인스턴스의 호스트명을 입력한다.
      EC2 인스턴스의 연결 탭을 누르면 알 수 있는 도메인 네임이다.
   3. protocol
      sftp 방식으로 연결하겠다는 것을 정의한다.
      수정하지 않는다.
   4. port
      해당 번호의 포트를 사용하겠다는 의미이다.
      기본적으로 수정하지 않는다.
   5. username
      유저 네임을 입력한다.
      EC2 인스턴스를 생성할 때 설정된 유저 이름을 입력한다.
      연결하려는 인스턴스의 연결 탭을 누르면 유저 이름을 확인할 수 있다.
   6. remotePath
      로컬과 연결할 서버의 경로이다.
   7. uploadOnSave
      로컬에서 작업하고 저장할 때 변동 사항을 동기화 할 것인지의 여부이다.
      기본적으로 false이며 수정하지 않는다.
   8. useTempFile
      임시 파일을 서버로 업로드 할 것인지의 여부이다.
      파일이 업로드되는 동안 사용자가 웹 페이지에 액세스할 때, 웹 페이지가 중단되는 것을 방지하기 위해 VS Code의 모든 임시 파일을 서버로 업로드 하는 기능이다.
      아직 불완전한 기능이므로 false로 설정한다.
   9. privateKeyPath
      키 페어의 위치를 작성한다.
      반드시 상대 경로로 작성한다.
      만약 ftp를 사용하게 된다면 privateKey로 변경해야 한다.
   10. openSsh
       atomic 파일을 업로드하려면 true로 설정되어야 한다.
       ssh 서버에서만 지원된다.
       true이면 useTempFile도 true로 설정되어야 한다고 공식 문서에서 설명하고 있다.

4. fn + f1을 누르고 List All을 선택한다.

   ![img](https://blog.kakaocdn.net/dn/bRWS3U/btsysoOIJqp/TXA0HZLQ0W4PECiepzk5M0/img.png)

5. 연결을 원하는 서버를 선택한다.

   ![img](https://blog.kakaocdn.net/dn/bmCSll/btsywxcjvRc/oLSBMbhl6BXKDuJ3OKJNh0/img.png)