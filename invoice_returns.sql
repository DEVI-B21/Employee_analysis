-- Insert return header from invoice
INSERT INTO return_header (
    return_date,
    return_number,
    invoice_id,
    distributor_id,
    customer_id,
    total_amount,
    status
)
SELECT
    invoice_date,
    CONCAT('RET-', id),
    id,
    distributor_id,
    customer_id,
    total_amount,
    'S'
FROM invoice_header
WHERE status = 'I';


-- Insert return detail
INSERT INTO return_detail (
    return_id,
    product_id,
    unit_price,
    quantity,
    tax_amount,
    discount_amount,
    total_amount
)
SELECT
    rh.id,
    id.product_id,
    id.unit_price,
    id.quantity,
    id.tax_amount,
    id.discount_amount,
    id.total_amount
FROM invoice_detail id
JOIN return_header rh
ON id.invoice_id = rh.invoice_id;

-- invoice_header → return_header
-- invoice_detail → return_detail
-- return_header  → return_detail