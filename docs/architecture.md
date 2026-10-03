# Architecture and behavior

The local CLI opens one MySQL connection. The copied implementation has no web
server, API, EC2 deployment, or connection pool.

## Files

| File | Responsibility |
| --- | --- |
| `main_code.py` | Menu, queries, input handling, connection cleanup |
| `db_config.py` | Connector settings from environment variables |
| `database_setup.sql` | Personal schema and sample data |
| `requirements.txt` | Connector dependency |
| `ai_use.txt` | AI assistance disclosure |
| `tests/test_cli.py` | Offline checks with database operations mocked |

## Item schema

| Column | Type | Meaning |
| --- | --- | --- |
| `itemid` | `INT`, auto-increment primary key | Record identifier |
| `purchasedate` | `DATE NOT NULL` | Purchase date |
| `purchaseprice` | `DECIMAL(10,2) NOT NULL` | Amount paid |
| `saleprice` | Nullable `DECIMAL(10,2)` | Sale amount; `NULL` means unsold |

There is no product-name, quantity, or customer table. The schema has no
non-negative-price constraint; the CLI checks negative input.

## Add flow

1. Parse the purchase date using `%Y-%m-%d`.
2. Parse prices with Python `float`; blank sale input becomes `None`.
3. Reject negative prices.
4. Pass values as parameters to an `INSERT`.
5. Commit and print a confirmation.

The menu catches `ValueError` for invalid input and Connector/Python `Error`
for database-operation failures. There is no explicit rollback/retry. Function
cursor cleanup is not protected by `finally` during an SQL error.

## Profit

```sql
SELECT SUM(saleprice - purchaseprice)
FROM item
WHERE saleprice IS NOT NULL;
```

This measures sale minus purchase price for sold items, not revenue. Fees, tax,
shipping, and other costs are excluded. If the aggregate returns `NULL`, the CLI
displays zero. The fixture contains unsold items and a sale below purchase price,
but sample data alone does not prove a successful live database run.
