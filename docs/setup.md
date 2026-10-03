# Setup

Use Python, MySQL Connector/Python, and a separate MySQL database that you are
authorized to use. These instructions do not provision AWS resources or change
your class database. MySQL Workbench can run the SQL setup file.

## Install

From the repository directory in PowerShell:

```powershell
py -m pip install -r requirements.txt
```

## Prepare the personal database

Connect to your own MySQL server in Workbench and execute `database_setup.sql`.
It creates `inventory_portfolio.item` and inserts 15 sample rows.

Running the whole file again adds another copy of the sample rows. Use a fresh
database for a reproducible demonstration, or execute only the statements you
need. Do not run it against the class database. The schema-setup account needs
database/table creation permissions. Normal CLI use needs `SELECT` and `INSERT`
on the item table.

## Configure

```powershell
$env:DB_HOST = "your-mysql-host"
$env:DB_PORT = "3306"
$env:DB_USER = "your-database-user"
$env:DB_NAME = "inventory_portfolio"
$dbPassword = Read-Host "Database password" -AsSecureString
$env:DB_PASSWORD = [System.Net.NetworkCredential]::new("", $dbPassword).Password
```

The host can be your authorized RDS endpoint or another MySQL server. These
values apply to this PowerShell process and its children. The app does not
automatically load an `.env` file.

| Variable | Default | Purpose |
| --- | --- | --- |
| `DB_HOST` | `localhost` | Server host |
| `DB_PORT` | `3306` | TCP port, parsed as an integer |
| `DB_USER` | `inventory_user` | MySQL account |
| `DB_PASSWORD` | Empty | MySQL password |
| `DB_NAME` | `inventory_portfolio` | Database name |
| `DB_SSL_CA` | Unset | Optional CA certificate path |
| `DB_SOCKET` | Unset | Optional local Unix socket on Linux/macOS |

The defaults do not represent a provisioned working account. Set your actual
connection values before running the app. For certificate/hostname verification,
provide a CA certificate that matches your server:

```powershell
$env:DB_SSL_CA = "C:\certificates\your-ca-bundle.pem"
```

This enables `ssl_verify_cert` and `ssl_verify_identity`. Without this variable,
those options are not enabled. The code retains `ssl_disabled=False`; that
setting alone does not prove a verified TLS connection. See the [official
Connector/Python connection arguments](https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html).

For RDS, confirm your authorized network path and permitted inbound connection
source. This repository and its tests do not change any AWS settings.

## Run

```powershell
py main_code.py
```

The [verification record](verification.md) covers the local MySQL run. Check your own RDS connection separately. When finished, clear the password from the shell:

```powershell
Remove-Item Env:DB_PASSWORD
Remove-Variable dbPassword
```

On macOS/Linux use `python` and your shell's environment-variable syntax.
