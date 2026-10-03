# Verification

## Offline checks completed

On October 3, 2026, Codex ran the checks in `tests/test_cli.py` using Python 3.12
and MySQL Connector/Python 26.7.0. All 10 tests passed. The complete output is in
[offline-checks.txt](offline-checks.txt).

These checks mock the connection and cursor. They do not connect to MySQL/RDS,
execute SQL on a server, verify AWS networking, or confirm stored-data persistence.

| Behavior checked | Result |
| --- | --- |
| Sold and unsold item display | Passed |
| Empty inventory message | Passed |
| Add sends parameters and commits | Passed with mocked database |
| Negative purchase/sale input | Rejected before insert |
| Impossible date | Rejected before insert |
| Profit aggregate formatting | Passed with supplied aggregate value |
| Empty aggregate | Displays zero |
| Invalid menu choice and quit | Passed; mocked connection closed |
| Connection-error message | Passed with injected connector error |
| Environment variables and CA settings | Passed; no TLS connection attempted |

After installing the requirements, run from the repository root:

```powershell
py -m unittest discover -s tests -v
```

Importing `main_code.py` no longer opens a connection because the personal copy
adds a standard `if __name__ == "__main__"` guard.

## Local MySQL check

On October 3, 2026, the personal copy was run with MySQL 8.0.46 using a separate sample database and a local Unix socket. It did not use class credentials or an RDS instance.

| Check | Result |
| --- | --- |
| Run the sample SQL once | 15 rows |
| View inventory | All 15 sample rows displayed |
| Add an unsold item | $10.00 purchase, sale price `NULL` |
| Quit and reopen | 16 rows; the added item remained visible |
| Calculate profit | CLI and SQL both returned $180.75 |

Menu input was scripted. Output was recorded from the actual application and rendered on a plain page for screenshots. The record is in [captures](captures/), with the pictures in the README.

## Still pending

An AWS RDS connection, AWS network configuration, and certificate/hostname verification have not been tested in this copy. The existing invalid-input tests use mocked cursors; invalid-input behavior was not rechecked against this local database.
