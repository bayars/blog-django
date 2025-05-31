# Blog API

A modern blog API built with FastAPI and PostgreSQL.

## Features

- RESTful API endpoints for blog posts, albums, and photos
- PostgreSQL database with SQLAlchemy ORM
- File upload support for images
- Automatic API documentation with OpenAPI/Swagger
- Poetry for dependency management
- Docker support for easy development and deployment

## Prerequisites

- Python 3.8 or higher
- Poetry
- PostgreSQL
- Docker and Docker Compose (for containerized setup)

## Installation

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/blog.git
cd blog
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Create a `.env` file in the root directory with the following content:
```env
POSTGRES_SERVER=localhost
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=blog
POSTGRES_PORT=5432
```

4. Create the database:
```bash
createdb blog
```

### Docker Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/blog.git
cd blog
```

2. Build and start the containers:
```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000` and the OpenAPI documentation at `http://localhost:8000/docs`.

## Running the Application

### Local Development

1. Activate the Poetry shell:
```bash
poetry shell
```

2. Run the application:
```bash
uvicorn app.main:app --reload
```

### Docker Development

The application will automatically start when you run `docker-compose up`. To stop the application:

```bash
docker-compose down
```

## API Endpoints

### Posts
- `GET /api/v1/posts` - List all posts
- `POST /api/v1/posts` - Create a new post
- `GET /api/v1/posts/{post_id}` - Get a specific post
- `GET /api/v1/posts/slug/{slug}` - Get a post by slug
- `PUT /api/v1/posts/{post_id}` - Update a post
- `DELETE /api/v1/posts/{post_id}` - Delete a post
- `POST /api/v1/posts/{post_id}/upload-image` - Upload a post image

### Albums
- `GET /api/v1/albums` - List all albums
- `POST /api/v1/albums` - Create a new album
- `GET /api/v1/albums/{album_id}` - Get a specific album
- `GET /api/v1/albums/slug/{slug}` - Get an album by slug
- `PUT /api/v1/albums/{album_id}` - Update an album
- `DELETE /api/v1/albums/{album_id}` - Delete an album
- `POST /api/v1/albums/{album_id}/upload-cover` - Upload an album cover

### Photos
- `GET /api/v1/photos` - List all photos
- `GET /api/v1/photos/album/{album_id}` - List photos in an album
- `POST /api/v1/photos/album/{album_id}` - Add a photo to an album
- `GET /api/v1/photos/{photo_id}` - Get a specific photo
- `PUT /api/v1/photos/{photo_id}` - Update a photo
- `DELETE /api/v1/photos/{photo_id}` - Delete a photo

## Development

### Database Migrations

The project uses Alembic for database migrations. To create a new migration:

```bash
alembic revision --autogenerate -m "description"
```

To apply migrations:

```bash
alembic upgrade head
```

### Docker Commands

- Build the containers:
```bash
docker-compose build
```

- Start the containers:
```bash
docker-compose up
```

- Start the containers in detached mode:
```bash
docker-compose up -d
```

- Stop the containers:
```bash
docker-compose down
```

- View logs:
```bash
docker-compose logs -f
```

- Execute commands in the web container:
```bash
docker-compose exec web <command>
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.