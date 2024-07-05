SELECT * FROM customers LIMIT 5;
SELECT * FROM invoices LIMIT 5;
SELECT * FROM invoice_items LIMIT 5;
.schema

SELECT A.InvoiceLineId, A.InvoiceId, D.CustomerId
FROM
    (invoice_items AS A JOIN invoices AS B ON A.InvoiceId = B.InvoiceId) AS
    C JOIN customers AS D
        ON C.CustomerId = D.CustomerId
ORDER BY A.InvoiceId DESC LIMIT 5;

SELECT customers.CustomerId, COUNT(*) 개수
FROM 



ORDER BY CustomerId LIMIT 5;