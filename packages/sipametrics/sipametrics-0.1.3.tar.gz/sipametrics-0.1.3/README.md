# SIPA Metrics Service

A Python package for interacting with the SIPA Metrics API to fetch metrics and other relevant data. This package simplifies integration by providing an easy-to-use interface for developers.

## Installation

Install the package via pip:

```
pip install sipametrics
```


## Usage
Here’s how you can use the sipametrics package in your Python projects.

### Example 1: Simple Usage
This example demonstrates a basic way to initialize the service and fetch metrics using an `async` function.

```
import asyncio
from sipametrics.services import SipaMetricsService

async def main():
    service = SipaMetricsService(api_key='your_api_key', api_secret='your_api_secret')
    response = await service.metrics(entity_id="INFRBGWX", metric_id="T01414")
    print(response)
    await service.close()

if __name__ == "__main__":
    asyncio.run(main())
```

### Example 2: Using Context Manager
This example uses a context manager `async with` for better resource management.

```
import aiohttp
import asyncio
from sipametrics.services import SipaMetricsService

async def main():
    async with SipaMetricsService(api_key='your_api_key', api_secret='your_api_secret') as session:
        response = await session.metrics(entity_id="INFRBGWX", metric_id="T01414")
        print(response)

asyncio.run(main())
```


## API Reference
**Service Initialization**

- `SipaMetricsService(api_key: str, api_secret: str)`: Initializes the service with your API credentials.

**Methods**

- `metrics(entity_id: str, metric_id: str)`: Fetches metrics for a given entity and metric ID.

## License

This package is licensed under the MIT License. See the LICENSE file for details.

