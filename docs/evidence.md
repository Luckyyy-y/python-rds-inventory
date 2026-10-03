# Screenshots and output

The README includes three screenshots: view items, add an unsold item, and calculate profit.

They show actual recorded output from the Python program using local MySQL 8.0.46 and fictional sample records. Scripted menu input was echoed into the transcript. The screenshots were taken from a simple browser transcript page, not MySQL Workbench or a native terminal window.

The complete outputs are in [captures](captures/). The local database check started with 15 records, added one $10.00 unsold item, and read 16 records after reopening. Profit stayed at $180.75 and matched the SQL aggregate.

These captures support local MySQL behavior. They do not verify an AWS RDS deployment, AWS networking, or a TLS certificate.

## Still to add

- A separate RDS connection check with private details removed.
- A short video showing the menu and explaining one limitation.
