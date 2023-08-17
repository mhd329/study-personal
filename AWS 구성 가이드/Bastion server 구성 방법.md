# Bastion server를 구성하는 방법

<br>

- 목적
  - Public EC2 환경과 Private RDS로 분리된 환경을 구성한다.
  - Bastion server를 구성하여 Private RDS 환경에 접근할 수 있게 한다.

<br>

## 순서

<br>

1. VPC를 생성하기 위해 VPC 메뉴로 들어간다.
2. 새로운 VPC를 생성한다.
   1. IPv4 CIDR 블록은 `10.0.0.0/16` 과 같은 형식으로 한다.
   2. 슬래시 뒤의 숫자가 커지면 사용할 수 있는 범위가 작아지기 때문에 16정도가 좋다.
3. VPC 설정 편집에서 DNS 호스트 이름 활성화에 체크해준다.
4. 서브넷을 만들기 위해 서브넷 메뉴로 들어간다.
5. 생성 버튼을 누르고 만들었던 VPC를 선택한다.
   1. Public subnet과 Private subnet을 생성한다.
   2. 