# Superleap Python SDK
Python SDK for clients to interact with Superleap

## Audit Data
Clients can poll audit-data (data-change logs) from Superleap using this sdk. 


## Installation
You can install the package using pip:

```bash
pip install superleap-sdk
```

## Usage

```python
from superleap-sdk import SuperleapClient

# Initialize the SDK

def handle_changes(changes: list[ObjectAuditData], mark_as_read, commit) -> None: # Worry about the type of mark_as_read later
    for change in changes:
        for data in change.audit_data_list:
            print(data.random_id)
            mark_as_read(data.get_object_pointer()) ## Latest data that is marked as read will be counted

client = SuperleapClient(Environment.LOCAL,"your-api-key")
sc.add_object(Object("lead",None))
sc.set_handler(handle_changes)

# Poll for updates
sc.poll_audit_data()
```

## Development

To set up the development environment:

1. Clone the repository
2. Create a virtual environment
3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

