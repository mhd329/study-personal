.tables
.headers on
.mode column

-- 01
SELECT A.* FROM playlist_track AS "A" ORDER BY PlaylistId DESC LIMIT 5;

-- 02
SELECT B.* FROM tracks AS "B" ORDER BY TrackId LIMIT 5;

-- 03
SELECT A.PlaylistId, B.Name
FROM playlist_track AS A JOIN tracks AS B
    ON A.TrackId = B.TrackId
ORDER BY A.PlaylistId DESC LIMIT 10;

-- 04
SELECT A.PlaylistId, B.Name
FROM playlist_track AS A JOIN tracks AS B
    ON A.TrackId = B.TrackId
WHERE A.PlaylistId = 10
ORDER BY B.Name DESC LIMIT 5;

-- 05
SELECT COUNT(*)
FROM tracks AS T JOIN artists AS A
    ON T.Composer = A.Name;

-- 06
SELECT COUNT(*)
FROM tracks AS T LEFT JOIN artists AS A
    ON T.Composer = A.Name;

-- 07
SELECT COUNT(*)
FROM tracks AS T LEFT JOIN artists AS A
    ON T.Composer = A.Name
WHERE A.Name IS NOT NULL;

-- 08
SELECT InvoiceLineId, InvoiceId FROM invoice_items ORDER BY InvoiceId LIMIT 5;

-- 09
SELECT InvoiceId, CustomerId FROM invoices ORDER BY InvoiceId LIMIT 5;

-- 10
SELECT inv_item.InvoiceLineId, inv.InvoiceId
FROM invoice_items AS inv_item JOIN invoices AS inv
    ON inv_item.InvoiceId = inv.InvoiceId
ORDER BY inv_item.InvoiceId DESC LIMIT 5;

-- 11
SELECT invoices.InvoiceId, customers.CustomerId
FROM invoices JOIN customers
    ON invoices.CustomerId = customers.CustomerId
ORDER BY invoices.InvoiceId DESC LIMIT 5;

-- 12
SELECT invoices_info.InvoiceLineId, invoices_info.InvoiceId, customers.CustomerId
FROM
    (invoice_items JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId) AS
        invoices_info JOIN customers ON invoices_info.CustomerId = customers.CustomerId
ORDER BY invoices_info.InvoiceId DESC LIMIT 5;

-- 13
SELECT * FROM invoice_items;
SELECT * FROM invoices;
SELECT * FROM customers;

-- 각 고객별 송장이 몇개인지 >>> 송장별 상품이 몇개인지

SELECT invoice_items.InvoiceId, invoice_items.Quantity FROM invoice_items;
SELECT InvoiceId, CustomerId FROM invoices;

SELECT invoices.CustomerId, COUNT(*) FROM (SELECT invoice_items.InvoiceId, invoice_items.Quantity, invoices.CustomerId, COUNT(*) FROM invoice_items JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId GROUP BY invoice_items.InvoiceId ORDER BY invoices.CustomerId) GROUP BY invoices.CustomerId;
