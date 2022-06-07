

# Aircraft monitoring system(TEST)

The service uses the following technologies:

- `Python 3.8`
- `Django 3.2`
- `DjangoRestFramework-3.12.4`
- `psycopg2-binary 2.9.3`
- `drf-yasg 1.20.0`
- `PostgreSQL 12.4`
- `Docker`

## How to run project
```sh
$ git clone https://github.com/Sultanbek9899/aermetric_test && cd aermetric_test
$ cp .env.example .env # or see environment variables below.
$ docker-compos up -d --build #Run project build
$ docker exec -it aermetic python3 manage.py createsuperuser
```
Now app is available in http://127.0.0.1:8005/. 
You need data from csv_data.csv load it in page:
http://127.0.0.1:8005/admin/service/event/ . 
Use button Import CSV.
### PAGE TO GET DATA -> http://127.0.0.1:8005/service/api/event_statistic/

