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

## Database checks still pending

Use a fresh personal `inventory_portfolio` database. Fill in actual results and
attach evidence after running each check.

| Check | Expected behavior | Actual result |
| --- | --- | --- |
| Run SQL fixture once | 15 sample rows | Not run in this copy |
| View items | CLI values match SQL rows | Not run |
| Add an unsold sample | Row has `saleprice IS NULL` | Not run |
| Add, quit, reopen | Added record remains visible | Not run |
| Profit | CLI agrees with aggregate SQL | Not run |
| Invalid input | No unintended database row | Not run |
| Certificate verification | Connection succeeds with the correct CA/host | Not run |

No copied class credentials were used, and no original class data was changed
while preparing or testing this repository.
