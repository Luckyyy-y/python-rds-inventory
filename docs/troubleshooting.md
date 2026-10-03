# Troubleshooting

## Historical coursework connection issue

The original AI disclosure recorded `1045 (28000): Access denied` during a
MySQL/RDS connection attempt. It stated that permission settings were changed
and the problem was resolved, but did not identify the exact setting, provide
the full diagnostic sequence, or include retest output.

This copy does not claim a particular security group, password, or user grant
was the confirmed cause. The original network address was removed from the
disclosure summary. Add the actual checks, exact change, and successful query
if those details can be recovered; do not invent the missing incident history.

## New failures

| Symptom | Next investigation |
| --- | --- |
| Timeout / unreachable server | Host, port, DNS, authorized network path |
| Access denied | Configured MySQL account, authentication details, grants |
| Unknown database/table | Selected database and schema setup |
| Certificate validation failure | CA file, hostname, server certificate |
| Invalid port before menu | Set `DB_PORT` to an integer |

These are investigation directions, not diagnoses of a particular deployment.

For each issue record the symptom, checks and their output, confirmed cause (or
unknown), exact change, and retest. Exclude passwords, tokens, secret connection
strings, and unrelated private network details from public evidence.
