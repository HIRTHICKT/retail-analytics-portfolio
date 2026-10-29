
USE retail_analytics;

-- 1. Total orders and delivered-order rate
SELECT
    COUNT(*) AS total_orders,
    SUM(order_status = 'delivered') AS delivered_orders,
    ROUND(
        100.0 * SUM(order_status = 'delivered') / COUNT(*),
        2
    ) AS delivery_success_rate_pct
FROM orders;

-- 2. Order status distribution
SELECT
    order_status,
    COUNT(*) AS order_count,
    ROUND(
        100.0 * COUNT(*) / (SELECT COUNT(*) FROM orders),
        2
    ) AS percentage
FROM orders
GROUP BY order_status
ORDER BY order_count DESC;

-- 3. Delivery performance
SELECT *
FROM delivery_kpis;

-- 4. Order status summary view
SELECT *
FROM order_status_summary
ORDER BY order_count DESC;
