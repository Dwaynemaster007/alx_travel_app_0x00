# ✈️ ALX Travel App 0x00: Models & Seeding

Milestone 0x00 of the travel booking API: database models, DRF serializers and a management command that seeds sample data.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)

## What's in this milestone

| File | Purpose |
| --- | --- |
| [`listings/models.py`](alx_travel_app/listings/models.py) | `Listing`, `Booking` (works out `total_price` from the nightly rate) and `Review` |
| [`listings/serializers.py`](alx_travel_app/listings/serializers.py) | `ListingSerializer`, `BookingSerializer` (checks the dates) and `ReviewSerializer` |
| [`listings/management/commands/seed.py`](alx_travel_app/listings/management/commands/seed.py) | `python manage.py seed` creates sample listings, bookings and reviews |
| `GET /api/listings/` | Read-only list to check the data |

## Run it

You need Python 3.10+. MySQL is optional: leave `DB_NAME` empty in `.env` to use SQLite.

```bash
git clone https://github.com/Dwaynemaster007/alx_travel_app_0x00.git
cd alx_travel_app_0x00
cd alx_travel_app
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt   # mysqlclient needs the MySQL client headers; remove it if you only use SQLite
cp .env.example .env
python manage.py migrate
python manage.py seed           # sample data
python manage.py runserver       # http://localhost:8000/swagger/
python manage.py test listings  # run the tests
```

## The travel app series

Each repository holds the project as it was at the end of one milestone:

| Repo | Milestone |
| --- | --- |
| [`alx_travel_app`](https://github.com/Dwaynemaster007/alx_travel_app) | Project setup: Django, DRF, CORS, Swagger, MySQL/SQLite settings |
| **`alx_travel_app_0x00`** | Models (`Listing`, `Booking`, `Review`), serializers and a `seed` command |
| [`alx_travel_app_0x01`](https://github.com/Dwaynemaster007/alx_travel_app_0x01) | CRUD API with DRF `ViewSet`s and a router |
| [`alx_travel_app_0x02`](https://github.com/Dwaynemaster007/alx_travel_app_0x02) | Chapa payment initiation and verification |
| [`alx_travel_app_0x03`](https://github.com/Dwaynemaster007/alx_travel_app_0x03) | Celery + RabbitMQ booking confirmation emails |

## Author

**Thubelihle Dlamini**, [GitHub](https://github.com/Dwaynemaster007) · [LinkedIn](https://linkedin.com/in/thubelihledlamini)
