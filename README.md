# Hands-on-Message-brokers

## Team 11
| Full name       | Group     | Email                           |
|-----------------|-----------|---------------------------------|
| Azamat Bayramov | B22-SD-03 | a.bayramov@innopolis.university |
| Darya Koncheva  | B22-SD-02 | d.koncheva@innopolis.university |
| Matthew Rusakov | B22-SD-03 | m.rusakov@innopolis.university  |
| Egor Valikov    | B22-CBS-01| e.valikov@innopolis.university  |

## How to launch application

### Single service

```
bash run.sh single
```

OR (just content of `run.sh` with `single` parameter)

```
docker compose -f docker-compose-multiple.yml down
docker compose -f docker-compose-single.yml up --build -d
```

### Multiple service

```
bash run.sh multiple
```

OR (just content of `run.sh` with `multiple` parameter)

```
docker compose -f docker-compose-single.yml down
docker compose -f docker-compose-multiple.yml up --build -d
```

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
