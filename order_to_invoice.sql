-- Insert invoice headers from orders
INSERT INTO invoice_header (
    invoice_date,
    invoice_number,
    customer_id,
    distributor_id,
    created_by,
    total_amount,
    status
)
SELECT
    order_date,
    CONCAT('INV-', id),
    customer_id,
    distributor_id,
    created_by,
    total_amount,
    'I'
FROM order_header
WHERE status = 'I';


-- Insert invoice details from order details
INSERT INTO invoice_detail (
    invoice_id,
    product_id,
    unit_price,
    quantity,
    tax_amount,
    discount_amount,
    total_amount
)
SELECT
    ih.id,
    od.product_id,
    od.unit_price,
    od.quantity,
    od.tax_amount,
    od.discount_amount,
    od.total_amount
FROM order_detail od
JOIN invoice_header ih
ON od.order_id = ih.id;


-- invoice_header-  order header
-- invoice_detail -  order detail 