### 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
| 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT A.* FROM playlist_track AS "A" ORDER BY PlaylistId DESC LIMIT 5;
```

### 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요
| 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
SELECT B.* FROM tracks AS "B" ORDER BY TrackId LIMIT 5;
```

### 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.
| 단, PlaylistId, Name 컬럼을 `PlaylistId` 기준으로 내림차순으로 10개만 출력하세요. 

```sql
SELECT A.PlaylistId, B.Name
FROM playlist_track AS A JOIN tracks AS B
    ON A.TrackId = B.TrackId
ORDER BY A.PlaylistId DESC LIMIT 10;

PlaylistId  Name
----------  -----------------------
18          Now's The Time
17          The Zoo
17          Flying High Again
17          Crazy Train
17          I Don't Know
17          Looks That Kill
17          Live To Win
17          Ace Of Spades
17          Creeping Death
17          For Whom The Bell Tolls
```

### 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 
| 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.

```sql
SELECT A.PlaylistId, B.Name
FROM playlist_track AS A JOIN tracks AS B
    ON A.TrackId = B.TrackId
WHERE A.PlaylistId = 10
ORDER BY B.Name DESC LIMIT 5;

PlaylistId  Name
----------  ------------------------
10          Women's Appreciation
10          White Rabbit
10          Whatever the Case May Be
10          What Kate Did
10          War of the Gods, Pt. 2
```

### 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
SELECT COUNT(*)
FROM tracks A JOIN artists B
    ON A.Composer = B.Name;

COUNT(*)
--------
402
```

### 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
SELECT COUNT(*)
FROM tracks T LEFT JOIN artists A
    ON T.Composer = A.Name;

COUNT(*)
--------
3503
```

### 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.
```plain
1. JOIN 은 서로 다른 테이블끼리 주어진 조건으로 비교하여 그것과 일치하는 컬럼이 있는 경우 그것을 바탕으로 값을 반환한다.

2. tracks 테이블을 기준으로 LEFT JOIN 명령을 수행하면
서로 INNER JOIN 한 것에다가 tracks 의 나머지 값들을 artists 의 행 규칙에 맞게 표시해줘야 하는데
tracks 의 겹쳐지지 않은 나머지 값들은 artists 의 행에 채워질 수 없으므로 규칙에 맞게 표시하려면 NULL 을 채워넣어서라도 보여준다.

3. 따라서 숫자가 달라지는 것은 빈 공간의 수 만큼 NULL 이 추가되어서 그렇다.

4. 
    SELECT COUNT(*)
	FROM tracks T LEFT JOIN artists A
    	ON T.Composer = A.Name
	WHERE A.Name IS NOT NULL;

    COUNT(*)
    --------
    402
NULL 을 계산하지 않게 해주면 숫자가 같게 나온다.
```

### 8. invoice_items 테이블의 데이터를 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
SELECT InvoiceLineId, InvoiceId FROM invoice_items ORDER BY InvoiceId LIMIT 5;

InvoiceLineId  InvoiceId
-------------  ---------
1              1
2              1
3              2
4              2
5              2
```

### 9. invoices 테이블의 데이터를 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT InvoiceId, CustomerId FROM invoices ORDER BY InvoiceId LIMIT 5;

InvoiceId  CustomerId
---------  ----------
1          2
2          4
3          8
4          14
5          23
```

### 10. 각 invoices_item에 해당하는 invoice 데이터를 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.

```sql
SELECT inv_item.InvoiceLineId, inv.InvoiceId
FROM invoice_items AS inv_item JOIN invoices AS inv
    ON inv_item.InvoiceId = inv.InvoiceId
ORDER BY inv_item.InvoiceId DESC LIMIT 5;

InvoiceLineId  InvoiceId
-------------  ---------
2240           412
2239           411
2238           411
2237           411
2236           411
```


### 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.

```
SELECT invoices.InvoiceId, customers.CustomerId
FROM invoices JOIN customers
    ON invoices.CustomerId = customers.CustomerId
ORDER BY invoices.InvoiceId DESC LIMIT 5;

InvoiceId  CustomerId
---------  ----------
412        58
411        44
410        35
409        29
408        25
```

### 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.

```
SELECT invoices_info.InvoiceLineId, invoices_info.InvoiceId, customers.CustomerId
FROM
    (invoice_items JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId) AS
        invoices_info JOIN customers ON invoices_info.CustomerId = customers.CustomerId
ORDER BY invoices_info.InvoiceId DESC LIMIT 5;

InvoiceLineId  InvoiceId  CustomerId
-------------  ---------  ----------
2240           412        58
2239           411        44
2238           411        44
2237           411        44
2236           411        44
```

### 13. 각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.
| 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.
```sql

```

