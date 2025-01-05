# Arizona API Client

This is a Python client for the Arizona API, which provides information about various game servers.

## Installation

To use this client, you'll need to have Python 3 installed on your system. You can install the required dependencies using pip:

```
pip install arizona-rp-api
pip install requests
```

## Usage

Here's an example of how to use the `ArizonaAPI` class:

```python
from main import ArizonaAPI

api = ArizonaAPI()

all_servers = api.get_all_servers()
print(all_servers)

arizona_servers = api.get_arizona_servers()
print(arizona_servers)

rodina_servers = api.get_rodina_servers()
print(rodina_servers)

arizonav_servers = api.get_arizonav_servers()
print(arizonav_servers)

village_servers = api.get_village_servers()
print(village_servers)

arizona_staging_servers = api.get_arizona_staging_servers()
print(arizona_staging_servers)
```

## API

The `ArizonaAPI` class provides the following methods:

- `get_all_servers()`: Returns a list of all servers.
- `get_arizona_servers()`: Returns a list of Arizona servers.
- `get_rodina_servers()`: Returns a list of Rodina servers.
- `get_arizonav_servers()`: Returns a list of ArizonaV servers.
- `get_village_servers()`: Returns a list of Village servers.
- `get_arizona_staging_servers()`: Returns a list of Arizona Staging servers.
