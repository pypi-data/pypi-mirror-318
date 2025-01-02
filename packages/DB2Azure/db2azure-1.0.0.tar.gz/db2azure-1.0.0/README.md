<picture align="center">
  <source media="(prefers-color-scheme: dark)" srcset="https://ik.imagekit.io/isyob5kdk4y/DB2AzureLogo_i2TWk-13b?updatedAt=1734874553185">
  <img alt="DB2Azure Logo" src="https://ik.imagekit.io/isyob5kdk4y/DB2AzureLogo_i2TWk-13b?updatedAt=1734874553185">
</picture>

# DB2Azure

DB2Azure is a Python package designed to streamline the process of loading data from SQL Server (MSSQL) and PostgreSQL databases to Azure Blob Storage in both JSON and CSV formats. This package simplifies the data extraction and upload processes with separate modules for SQL Server (`SQLLoader`) and PostgreSQL (`PostgreLoader`), enabling efficient and seamless integration with Azure Blob Storage.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
  - [SQL Server Loader](#sql-server-loader)
  - [PostgreSQL Loader](#postgresql-loader)
- [Methods](#methods)
  - [SQLLoader](#sqlloader)
  - [PostgreLoader](#postgreloader)
- [Configuration](#configuration)
- [Error Handling](#error-handling)
- [License](#license)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Description

DB2Azure helps automate the process of extracting data from SQL Server and PostgreSQL databases and uploading it directly to Azure Blob Storage in either JSON or CSV format. The package includes two main modules for SQL Server (`SQLLoader`) and PostgreSQL (`PostgreLoader`), each providing methods for executing SQL queries and transferring the data to Azure Blob Storage.

### Key Features:
- **SQL Server Support**: Extracts data from Microsoft SQL Server databases using `pyodbc`.
- **PostgreSQL Support**: Extracts data from PostgreSQL databases using `psycopg`.
- **Azure Blob Storage Upload**: Uploads data as JSON or CSV to Azure Blob Storage using the `azure-storage-blob`.
- **Flexibility**: Allows customization of folder path, file name, and blob URL.
- **Error Handling**: Provides detailed error messages in case of failures.

## Installation

To install the `DB2Azure` package, use the following `pip` command:

```bash
pip install DB2Azure
```

Alternatively, clone the repository and install it manually:

```bash
git clone https://github.com/mr-speedster/DB2Azure.git
cd DB2Azure
pip install .
```

## Usage

### SQL Server Loader

To use the SQL Server loader, you can use the `SQLLoader` class in the `db2azure` module. The `SQLLoader` class allows you to execute SQL queries and upload the resulting data to Azure Blob Storage in either JSON or CSV format.

#### Example:

```python
from db2azure import SQLLoader

# SQL Query
query = "SELECT [UserID], [FirstName], [LastName], [Email], [Age] FROM [SampleDB].[dbo].[Users]"

# SQL Server connection string
sql_conn = r"Driver=<driver>;Server=<server_name>;Database=<database>;Trusted_Connection=yes;"

# Azure Blob Storage parameters
container_name = "your_container"
folder_path = "your_folder"
json_file_name = "your_file.json"
csv_file_name = "your_file.csv"
azure_blob_url = "https://your_account_name.blob.core.windows.net"
sas_token = "your_sas_token"

# Load to JSON
json_status = SQLLoader.load_to_json(query, sql_conn, container_name, folder_path, json_file_name, azure_blob_url, sas_token)
print("JSON Upload Status:", json_status)

# Load to CSV
csv_status = SQLLoader.load_to_csv(query, sql_conn, container_name, folder_path, csv_file_name, azure_blob_url, sas_token)
print("CSV Upload Status:", csv_status)
```

### PostgreSQL Loader

To use the PostgreSQL loader, you can use the `PostgreLoader` class in the `db2azure` module. The `PostgreLoader` class operates similarly to `SQLLoader`, but it works with PostgreSQL databases.

#### Example:

```python
from db2azure import PostgreLoader

# SQL Query
query = "SELECT user_id, first_name, last_name, email, age FROM public.users;"

# PostgreSQL connection parameters
connection_params = {
    "host": "localhost",      # e.g., "localhost" or an IP address
    "port": "5432",           # default PostgreSQL port
    "dbname": "SampleDB",     # name of the database
    "user": "*****",          # PostgreSQL username
    "password": "*****"       # PostgreSQL password
}

# Azure Blob Storage parameters
container_name = "your_container"
folder_path = "your_folder"
json_file_name = "your_file.json"
csv_file_name = "your_file.csv"
azure_blob_url = "https://your_account_name.blob.core.windows.net"
sas_token = "your_sas_token"

# Load to JSON
json_status = PostgreLoader.load_to_json(query, connection_params, container_name, folder_path, json_file_name, azure_blob_url, sas_token)
print("JSON Upload Status:", json_status)

# Load to CSV
csv_status = PostgreLoader.load_to_csv(query, connection_params, container_name, folder_path, csv_file_name, azure_blob_url, sas_token)
print("CSV Upload Status:", csv_status)
```

## Methods

### `SQLLoader`

- **`load_to_json`**: Loads data from SQL Server to a JSON file in Azure Blob Storage.
    - Parameters: `sql_query`, `connection_string`, `container_name`, `folder_path`, `file_name`, `azure_blob_url`, `sas_token`
    
- **`load_to_csv`**: Loads data from SQL Server to a CSV file in Azure Blob Storage.
    - Parameters: `sql_query`, `connection_string`, `container_name`, `folder_path`, `file_name`, `azure_blob_url`, `sas_token`

### `PostgreLoader`

- **`load_to_json`**: Loads data from PostgreSQL to a JSON file in Azure Blob Storage.
    - Parameters: `sql_query`, `connection_params`, `container_name`, `folder_path`, `file_name`, `azure_blob_url`, `sas_token`
    
- **`load_to_csv`**: Loads data from PostgreSQL to a CSV file in Azure Blob Storage.
    - Parameters: `sql_query`, `connection_params`, `container_name`, `folder_path`, `file_name`, `azure_blob_url`, `sas_token`

## Configuration

For both SQL Server and PostgreSQL loaders, you will need to provide the following configuration:

- **SQL Server**: Use the `connection_string` parameter to configure the connection to your SQL Server.
- **PostgreSQL**: Use the `connection_params` dictionary to configure the connection to your PostgreSQL database.
- **Azure Blob Storage**: Provide `container_name`, `folder_path`, `file_name`, `azure_blob_url`, and `sas_token` to specify where and how the data should be uploaded to Azure Blob Storage.

## Error Handling

If any error occurs during the data extraction or upload process, the methods will return an error response containing:

- **`status`**: Always `error`.
- **`message`**: The error message describing the issue.

Example error response:

```json
{
  "status": "error",
  "message": "Connection failed: 'Your error message here'"
}

```

## License

DB2Azure is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

We welcome contributions! Feel free to open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- **pyodbc**: A Python DB API 2.0 interface for ODBC databases, used for connecting to SQL Server.
- **psycopg**: A PostgreSQL database adapter for Python, used for connecting to PostgreSQL.
- **azure-storage-blob**: Azure SDK for Python, used for uploading files to Azure Blob Storage.
