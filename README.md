# ✈️ ALX Travel App 0x00: Models & Seeding

Milestone 0x00 of the travel booking API: database models, DRF serializers and a management command that seeds sample data.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)

## What's in this milestone

| File | Purpose |
| --- | --- |
| [`listings/models.py`](alx_travel_app/listings/models.py) | `Listing`, `Booking` and `Review` models with relationships and constraints |
| [`listings/serializers.py`](alx_travel_app/listings/serializers.py) | `ListingSerializer` and `BookingSerializer` |
| [`listings/management/commands/seed.py`](alx_travel_app/listings/management/commands/seed.py) | `python manage.py seed` fills the database with sample listings |

Copy [`alx_travel_app/.env.example`](alx_travel_app/.env.example) to `.env` and fill in your database credentials.

## The travel app series

Each repository holds the code added in one milestone of the **ALX ProDev Backend** travel booking project:

| Repo | Milestone |
| --- | --- |
| [`alx_travel_app`](https://github.com/Dwaynemaster007/alx_travel_app) | Project setup: Django, DRF, Swagger, MySQL configuration |
| [`alx_travel_app_0x00`](https://github.com/Dwaynemaster007/alx_travel_app_0x00) | Models (`Listing`, `Booking`, `Review`), serializers and a seed command |
| [`alx_travel_app_0x01`](https://github.com/Dwaynemaster007/alx_travel_app_0x01) | CRUD API with DRF `ViewSet`s and routers |
| [`alx_travel_app_0x02`](https://github.com/Dwaynemaster007/alx_travel_app_0x02) | Chapa payment initiation and verification |
| [`alx_travel_app_0x03`](https://github.com/Dwaynemaster007/alx_travel_app_0x03) | Celery + RabbitMQ background email tasks |

## Author

**Thubelihle Dlamini**, [GitHub](https://github.com/Dwaynemaster007) · [LinkedIn](https://linkedin.com/in/thubelihledlamini)
