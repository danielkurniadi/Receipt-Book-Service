# Receipt Book V1 Service

This repo contains the source code for Receipt Book v1 App.

## Contributors ###
Team members and contributors:
 * Daniel Kurniadi @iqDF
 * Hans Albert Lianto @HansAlbertLianto

## Requirements (Package)

- `python=3.5.2` or newer
- `MySQL`
- `virtualvenv` or `venv`
- `git`

## Installation

```bash
# ensure that you are using virtualvenv and python 3.5
pip3 install -r requirements.pip 
```

## DB Setup

You need to install `MySQL` DB in the local environment.

After installing, make sure you have created the `gtd` and `gtd_test` database in your local.

```bash
$ mysql -u root -p # Type in your password
mysql> CREATE DATABASE receiptbookdb;
mysql> CREATE DATABASE receiptbookdb_test;
```

## Run Server

```bash
export DATABASE_URI=mysql+pymysql://root:rootpassword@127.0.0.1:3306/receiptbookdb # get your mysql url
export FLASK_ENV=development # dev mode
export DEBUG=True # dev mode
python3 run.py # available at 127.0.0.1:5000
```

## Run Testing

```bash
pytest -s -v
```
