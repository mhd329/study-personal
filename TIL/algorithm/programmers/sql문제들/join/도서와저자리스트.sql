SELECT book_id, author_name, DATE_FORMAT(published_date, "%Y-%m-%d")
FROM BOOK as b
JOIN AUTHOR as a
ON b.author_id = a.author_id
WHERE category = "경제"
ORDER BY published_date;