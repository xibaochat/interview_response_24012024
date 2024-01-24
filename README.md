## launch the project

### dependancies

* make
* docker
* docker-compose

### How to

```bash
make re
```

## connect to db manually

```bash
psql -h localhost -p 5432 -U root -d db
```

## route download_data
get all data in table instruction_record and return data.csv file.

### download the csv file
```bash
sudo wget http://127.0.0.1:8000/download_data
```
### test manualy
```bash
curl -X GET http://127.0.0.1:8000/download_data -H "Content-Type: application/json"
```
data.csv will be stored in a separate, uniquely identified directory under csv by using the uuid module.
Utilisation of functools.lru_cache decorator in Python helps avoid redundant data reading and file creation when there's no new data entry. It only triggers the database query and file creation when new data is entered into the database.

The data.csv contains columns instruction and result.
