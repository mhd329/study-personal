# DB 복제(Replication)

요청 부하 설계에 대해서, 서버의 부하 분산 외에도 DBMS 서버의 부하도 신경을 써야한다.

이 경우 DBMS 서버를 이중화하여 부하를 해결할 수 있다.

---

### DB Replication

- Replication은 복제를 뜻하며 DB Replication은 두 대 이상의 DBMS에 데이터를 나눠서 저장하는 방식이다.
- 사용하기 위해 최소 Master / Slave 구성을 취해야 한다.

- Master DBMS
  - 서버로부터 데이터 등록, 수정, 삭제 요청시 바이너리 로그(Binarylog)를 생성하여 Slave DBMS로 전달한다.
  - 주로 웹서버가 요청한 데이터의 등록, 수정, 삭제를 하는 용도로 사용된다.
- Slave DBMS
  - Master DBMS로부터 전달받은 바이너리 로그를 데이터로 반영하게 된다.
  - 주로 데이터를 불러오고 읽는 용도로 사용된다.

---

### Replication의 사용 목적

1. 백업
   - Master: 데이터 원본 서버
   - Slave: 백업 서버
     - 서버의 등록, 수정, 삭제 query를 Master에 반영하고 Master에서 같은 query를 발생시켜 Slave로 전달한다.
       - Master가 변경되는 즉시 Slave로 변경사항이 전달된다.
       - 이를 활용해 DB백업을 할 수 있으며 Master에 장애가 생길 경우 Slave로 변경할 수 있다.
2. DB부하 분산
   - 한 대의 DB로 감당할 수 없을때 Replication으로 여러대의 서버를 만들 수 있다.
   - DB CRUD 작업에서 Master는 C, U, D의 용도로 두고 Slave는 R 전용으로 둔다.

---

### Replication 사용시 주의사항

- 상호 호환성을 위해 Master-Slave 버전의 일치를 신경써야 한다.
- 부득이 버전이 다를 경우, Slave가 상위버전이어야 한다.
  - 메인 DB인 Master의 버전이 더 높아야 하지 않나? 라고 생각했는데, 공식문서를 찾아보니 Slave가 상위여야 된다고 설명하고 있다. 그런데 이유에 대한 자료는 찾기가 힘들다.

참조 : https://mariadb.com/kb/en/database-version-on-master-slave-replication/

참조 2 : https://mariadb.com/kb/en/setting-up-replication/#versions