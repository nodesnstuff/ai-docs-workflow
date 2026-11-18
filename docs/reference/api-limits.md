# API limits

The Parcelo API applies the following limits to every API key.

| Limit | Value |
|-------|-------|
| Requests per minute | 60 |
| Maximum page size | 100 |

When you exceed the request limit, the API responds with HTTP `429 Too Many Requests`. Wait until the next minute before sending more requests.
