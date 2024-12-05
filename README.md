# Hands-on-Message-brokers

## Table of contents

* [Team Information](#team-information)
* [Demo](#demo)
* [Report](#report)
* [Project Structure](#project-structure)
* [How To](#how-to)

## Team Information

### Team 11

| Full name       | Group     | Email                           |
|-----------------|-----------|---------------------------------|
| Azamat Bayramov | B22-SD-03 | a.bayramov@innopolis.university |
| Darya Koncheva  | B22-SD-02 | d.koncheva@innopolis.university |
| Matthew Rusakov | B22-SD-03 | m.rusakov@innopolis.university  |
| Egor Valikov    | B22-CBS-01| e.valikov@innopolis.university  |

## Demo

TODO

## Report

TODO

## Project Structure

TODO

## How To

### How to launch application

#### Single services (pipes and filters)

```
bash run.sh single
```

OR (just content of `run.sh` with `single` parameter)

```
docker compose -f docker-compose-multiple.yml down
docker compose -f docker-compose-single.yml up --build -d
```

#### Multiple services (broker)

```
bash run.sh multiple
```

OR (just content of `run.sh` with `multiple` parameter)

```
docker compose -f docker-compose-single.yml down
docker compose -f docker-compose-multiple.yml up --build -d
```

### How to use application

- Open http://localhost:8000/docs
- Send messages

### How to launch load test

- Install locally load testing tools (locust)
```
pip install -r requirements-test.txt
```

- Run locust
```
locust -f test/locustfile.py --host=http://localhost:8000
```

- Open web interface and start load test
