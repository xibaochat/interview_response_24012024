# API for polish calculation

FastAPI with Postgresql project to make polish calculation and get an history of given instructions.

## Consideration

* The project was lint using `flake8`, `bandit`, `safety` and `xenon`.
```
export SRC_PATH="backend/src"
flake8 $SRC_PATH
bandit -r $SRC_PATH
safety check
xenon -b B -m A -a A $SRC_PATH
```
* Secrets are defined inside the `.env` en `.env_fastapi` files. This behavior is too dangerous to be kept in production.
* The DB user has all privilege ; for production, make sure to create a limited one.

## launch the project

### dependancies

* make
* docker
* docker-compose

### How to

```bash
make re
```

## Access to SWAGGER documenation

```
http://127.0.0.1:8000/docs#/
```

## Connect to db manually

```bash
psql -h localhost -p 5432 -U root -d db
```

## Make some calculation

```bash
$ curl -X POST http://127.0.0.1:8000/calculator -H "Content-Type: application/json" -d '{"instruction": [3,2,"+"]}'
5

$ curl -X POST http://127.0.0.1:8000/calculator -H "Content-Type: application/json" -d '{"instruction": [3, 1, 2, "+", 1, "*", "+"]}'
6
$ curl -X POST http://127.0.0.1:8000/calculator -H "Content-Type: application/json" -d '{"instruction": [2,"+"]}'
{"detail":"Something went wrong with the provided inputs."}

```

##  Download data csv file

Get all the data in the table `instruction_record` and return it as a csv file (named `data.csv` by default).

```bash
curl -X GET http://127.0.0.1:8000/download_data -H "Content-Type: application/json"
```
