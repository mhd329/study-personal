# VPC 구성

<br>

1. VPC를 생성하기 위해 VPC 메뉴로 들어간다.
2. 새로운 VPC를 생성한다.
   1. IPv4 CIDR 블록은 `10.0.0.0/16` 과 같은 형식으로 한다.
   2. 슬래시 뒤의 숫자가 커지면 사용할 수 있는 범위가 작아지기 때문에 16정도가 좋다.
3. VPC 설정 편집에서 DNS 호스트 이름 활성화에 체크해준다.
4. 서브넷을 만들기 위해 서브넷 메뉴로 들어간다.
5. 생성 버튼을 누르고 만들었던 VPC를 선택한다.
   - public subnet과 private subnet을 생성한다.
   - public 2개, private 4개를 생성한다.
     1. public-subnet-a1
        ap-northeast-2a
        10.0.1.0/24
     2. public-subnet-c1
        ap-northeast-2c
        10.0.2.0/24
     3. private-subnet-a1
        ap-northeast-2a
        10.0.3.0/24
     4. private-subnet-c1
        ap-northeast-2a
        10.0.4.0/24
     5. private-subnet-a2
        ap-northeast-2a
        10.0.5.0/24
     6. private-subnet-c2
        ap-northeast-2c
        10.0.6.0/24
6. 인터넷 게이트웨이를 만들기 위해 인터넷 게이트웨이 메뉴로 들어간다.
   - 서로 소통하기 위한 통로를 만드는 작업이다.
7. 생성한 다음 방금 만든 VPC에 연결을 한다.
8. Route table을 구성하기 위해 라우팅 테이블 메뉴로 간다.
9. 방금 만든 VPC를 사용하는 라우팅 테이블이 자동으로 생성되어있다.
   1. public subnet 라우팅 테이블로 구성한다.
   2. 서브넷 연결 편집을 통해 두 개의 public subnet에 모두 적용해준다.
   3. 라우팅 편집을 해준다.
      1. 외부에서 들어오는 IP는 `0.0.0.0/0` 으로써 모든 IP를 의미한다.
      2. 연결을 받아들이는 대상은 인터넷 게이트웨이를 선택하고 방금 만든 IGW를 선택한다.
10. 새로운 라우팅 테이블을 구성한다.
    1. private subnet 라우팅 테이블로 두 개를 구성한다.
    2. 서브넷 연결 편집을 통해 하나의 테이블당 두 개의 private subnet에 적용해준다.
       - a1, c1과 a2, c2 그룹을 두 개의 테이블에 분리해서 적용해준다.
    3. 외부와 직접적으로 통신하지 않기 때문에 IGW 설정은 생략한다.
11. 