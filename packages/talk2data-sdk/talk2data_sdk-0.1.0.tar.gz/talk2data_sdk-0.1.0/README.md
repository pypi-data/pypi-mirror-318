# Talk2Data SDK

Talk2Data SDK is a Python-based software development kit designed for data interaction and analysis.

## Installation

You can install the Bioturing Connector using pip:

```bash
pip install talk2data-sdk
```

## Usage

```python
from talk2data_sdk.connector import Talk2DataConnector

connector = Talk2DataConnector(
    "https://talk2data.bioturing.com/beta/t2d/",
    "company token",
)
connector.test_connection()

connector.list_databases()

db = connector.get_database("aca43367-2d5d-450d-808c-d93a8c040894")
db.info

db.cell_types

db.get_expression_summary(["CD3D", "CD2"], cell_types=["T cell", "B cell"], tissues=["blood"], conditions=["normal"])
```
