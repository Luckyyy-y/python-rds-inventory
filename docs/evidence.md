# Evidence to add

No screenshots or video have been added. This is a capture plan, not a record
of completed database tests.

| Capture | What to show | What it supports |
| --- | --- | --- |
| View inventory | CLI `iv` output and matching SQL rows | Stored records and unsold-item display |
| Add and restart | `ia` input, SQL row, then `iv` after reopening | Persistence of a committed record |
| Profit | `ic` output and matching aggregate query | Agreement with the database calculation |

Use sample data in a fresh personal database. Crop to relevant output and remove
credentials or unrelated account details. Add files to `docs/images/` when
available, then place them beside the relevant explanation in the README.

A caption should state the action, actual result, and supported conclusion.
For example, use this only after the persistence test actually succeeds:

> I added a sample item and reopened the application. The same item appeared
> in the CLI and database query, confirming that the insert persisted.

## Video later

Briefly explain the purpose, view sample records, add an item, verify it with a
query, show profit, and explain one limitation. Link the actual recording from
the README when available. No placeholder video URL is included.
