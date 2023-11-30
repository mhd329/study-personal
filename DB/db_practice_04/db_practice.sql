-- 01
.tables

-- 02
.schema *

SELECT * FROM albums;
SELECT * FROM sqlite_sequence;
SELECT * FROM artists;

SELECT * FROM customers;
SELECT * FROM employees;
SELECT * FROM genres;

SELECT * FROM invoices;
SELECT * FROM invoice_items;
SELECT * FROM media_types;

SELECT * FROM playlists;
SELECT * FROM playlist_track;
SELECT * FROM tracks;

SELECT * FROM sqlite_stat1;

-- 03
SELECT * FROM albums ORDER BY Title DESC LIMIT 5;

-- 04
SELECT COUNT(*) "고객 수" FROM customers;

-- 05
SELECT FirstName "이름", LastName "성"
FROM customers
WHERE Country = "USA"
ORDER BY FirstName DESC
LIMIT 5;

-- 06
SELECT COUNT(*) "송장수" FROM invoices WHERE BillingPostalCode IS NOT NULL;

-- 07
SELECT * FROM invoices WHERE BillingState IS NULL ORDER BY InvoiceDate DESC LIMIT 5;

-- 08
SELECT COUNT(*) FROM invoices WHERE InvoiceDate LIKE "2013-%";
SELECT COUNT(*) FROM invoices WHERE STRFTIME("%Y", "InvoiceDate") = "2013";

-- 09
SELECT CustomerId "고객ID", FirstName "이름", LastName "성" FROM customers WHERE FirstName LIKE "L%" ORDER BY CustomerId;

-- 10
-- 연산 순서를 까먹지 말자.
SELECT COUNT(*) "고객 수", Country "나라" FROM customers GROUP BY Country ORDER BY COUNT(*) DESC LIMIT 5;

-- 11
SELECT ArtistId, COUNT(*) "앨범 수" FROM albums GROUP BY ArtistId ORDER BY COUNT(*) DESC LIMIT 1;

-- 12
SELECT ArtistId, COUNT(*) "앨범 수" FROM albums GROUP BY ArtistId HAVING COUNT(*) >= 10 ORDER BY COUNT(*) DESC;

-- 13
SELECT COUNT(*) "고객 수", Country, State
FROM customers
WHERE State IS NOT NULL
GROUP BY Country, State
ORDER BY COUNT(*), Country DESC
LIMIT 5;

-- 14
SELECT CustomerId,
    CASE
    WHEN Fax IS NULL THEN 'X'
    ELSE 'O'
    END "FAX 유/무"
FROM customers
ORDER BY CustomerId LIMIT 5;

-- 15
SELECT
    LastName,
    FirstName,
    CAST(SUBSTR(DATE("now", "localtime"), 1, 4) AS INTEGER) - CAST(BirthDate AS INTEGER) + 1 "나이"
FROM employees
ORDER BY EmployeeId;

SELECT
    LastName,
    FirstName,
    (STRFTIME("%Y", "now") - STRFTIME("%Y", "BirthDate") + 1) "나이"
FROM employees
ORDER BY EmployeeId;

-- 16
SELECT Name
FROM artists
WHERE
    ArtistId =
    (
        SELECT ArtistId FROM
        (
            SELECT ArtistId, COUNT(*)
            FROM albums
            GROUP BY ArtistId
            ORDER BY COUNT(*)
            DESC LIMIT 1
        )
    );

-- 17
SELECT Name
FROM genres
WHERE
    GenreId =
    (
        SELECT GenreId FROM
        (
            SELECT GenreId, COUNT(*)
            FROM tracks
            GROUP BY GenreId
            ORDER BY COUNT(*)
            LIMIT 1
        )
    );