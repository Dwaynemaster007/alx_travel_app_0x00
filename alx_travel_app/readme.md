# ALX Travel App 0x00

A Django-based travel booking application with RESTful API endpoints for managing property listings, bookings, and reviews.

## Project Structure

```
alx_travel_app_0x00/
├── alx_travel_app/
│   ├── listings/
│   │   ├── models.py          # Database models for Listing, Booking, Review
│   │   ├── serializers.py     # DRF serializers for API responses
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── seed.py    # Database seeding management command
│   │   └── ...
│   └── ...
└── README.md
```

## Models

### Listing
- **listing_id**: UUID primary key
- **host_id**: Foreign key to User
- **name**: Property name (max 200 chars)
- **description**: Detailed description
- **location**: Property location (max 200 chars)
- **price_per_night**: Decimal field for nightly rate
- **created_at/updated_at**: Timestamps

### Booking
- **booking_id**: UUID primary key
- **property_id**: Foreign key to Listing
- **user_id**: Foreign key to User
- **start_date/end_date**: Booking date range
- **total_price**: Calculated total cost
- **created_at**: Timestamp

### Review
- **review_id**: UUID primary key
- **property_id**: Foreign key to Listing
- **user_id**: Foreign key to User
- **rating**: Integer (1-5 scale)
- **comment**: Review text
- **created_at**: Timestamp

## Features

- **Relational Database Models**: Proper foreign key relationships between users, listings, bookings, and reviews
- **Data Validation**: Model-level and serializer-level validation for data integrity
- **API Serializers**: DRF serializers for JSON API responses
- **Database Seeding**: Management command to populate database with sample data
- **UUID Primary Keys**: Enhanced security and uniqueness for all entities

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install django djangorestframework
   ```

2. **Run Migrations**:
   ```bash
   python manage.py makemigrations listings
   python manage.py migrate
   ```

3. **Seed Database**:
   ```bash
   # Seed with default amounts (10 listings, 20 bookings, 30 reviews)
   python manage.py seed
   
   # Or specify custom amounts
   python manage.py seed --listings 20 --bookings 50 --reviews 100
   ```

4. **Create Superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

5. **Run Development Server**:
   ```bash
   python manage.py runserver
   ```

## Management Commands

### Seed Command
Populates the database with realistic sample data for development and testing.

**Usage**:
```bash
python manage.py seed [--listings N] [--bookings N] [--reviews N]
```

**Options**:
- `--listings`: Number of listings to create (default: 10)
- `--bookings`: Number of bookings to create (default: 20)
- `--reviews`: Number of reviews to create (default: 30)

## API Serializers

The application includes comprehensive serializers for:

- **ListingSerializer**: Converts Listing model instances to JSON, includes nested host information
- **BookingSerializer**: Handles booking data with validation for date ranges
- **ReviewSerializer**: Manages review data with rating validation (1-5 scale)
- **UserSerializer**: Basic user information for nested serialization

## Database Relationships

- **One-to-Many**: User can have multiple listings (as host)
- **One-to-Many**: User can have multiple bookings (as guest)
- **One-to-Many**: User can have multiple reviews
- **One-to-Many**: Listing can have multiple bookings
- **One-to-Many**: Listing can have multiple reviews
- **Unique Constraint**: One review per user per property

## Validation Rules

- Booking end date must be after start date
- Review ratings must be between 1-5
- Price fields cannot be negative
- Unique reviews per user-property combination

## Sample Data

The seeder creates:
- **Users**: Mix of hosts and guests with realistic profiles
- **Listings**: Diverse property types across different locations
- **Bookings**: Random bookings with calculated total prices
- **Reviews**: Varied ratings and comments for properties

## Development Workflow

1. Create/modify models in `models.py`
2. Update serializers in `serializers.py` if needed
3. Run migrations to update database schema
4. Use seed command to populate with test data
5. Test API endpoints and data relationships

This structure provides a solid foundation for a travel booking platform with proper data modeling, API serialization, and development tooling..
