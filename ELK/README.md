# Setup your ELK single node

- Install docker on the desire computer
- Follow this [tutorial](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html)

## Dependencies for the project
- python-dotenv (read/store `.env file` containing credentials)
    ```bash
    pip install python-dotenv
    ```
- python ElasticSearch
   ```bash
    pip install elasticsearch
    ```
## Setup your env variables

Create a `.env` file and paste in it the variable defined below:

```python
ELK_USER=
ELK_PASSWORD=
ELK_HOST= A_RUNNING_COMPUTER_OF_THE_CLUSTER
ELK_PORT= 9200
ELK_INDEX= DESIRED_INDEX
ELK_LOCATION= YOUR_GPS_COORDINATE IN FORMAT "lat, long"
ELK_ROOM= YOUR_ROOM_NAME
```

## Send the measures to ELK cluster

```bash
python upload_measure.py
```
