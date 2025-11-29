# Chore Tracker - Docker Deployment Guide

This guide will help you deploy the Chore Tracker application using Docker and Docker Compose.

## Quick Start

### 1. Build and Run with Docker Compose (Recommended)

```bash
# Clone or navigate to the project directory
cd chore_tracker_docker

# Build and start the application
docker-compose up -d

# View logs
docker-compose logs -f

# Open your browser to http://localhost:5000
```

### 2. Build and Run with Docker

```bash
# Build the Docker image
docker build -t chore-tracker .

# Create a data directory for persistent storage
mkdir -p chore_data

# Run the container
docker run -d \
  --name chore-tracker \
  -p 5000:5000 \
  -v $(pwd)/chore_data:/app/data \
  -v $(pwd)/logs:/app/logs \
  --restart unless-stopped \
  chore-tracker
```

## Directory Structure

After deployment, your directory will look like this:

```
chore_tracker_docker/
├── chore_data/           # Persistent database storage
│   └── chore_tracker.db
├── logs/                 # Application logs
├── chore_tracker/        # Application source code
├── Dockerfile           # Docker build instructions
├── docker-compose.yml   # Docker Compose configuration
├── dockerignore         # Docker ignore file
└── start_app.sh         # Startup script
```

## Features

### Persistent Storage
- Database is stored in `chore_data/chore_tracker.db`
- Data persists across container restarts and updates
- Easy backup and restore by copying the `chore_data` directory

### Health Monitoring
- Built-in health checks every 30 seconds
- Automatic restart on failure
- Health status available at `/health` endpoint

### Production Ready
- Environment variable configuration
- Proper logging setup
- Security hardening
- Production WSGI server ready

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `FLASK_ENV` | `production` | Flask environment |
| `FLASK_DEBUG` | `False` | Enable debug mode |
| `DATABASE_URL` | `sqlite:///data/chore_tracker.db` | Database connection string |
| `FLASK_RUN_HOST` | `0.0.0.0` | Host to bind to |
| `FLASK_RUN_PORT` | `5000` | Port to bind to |

### Custom Configuration

You can override any setting by creating a `.env` file:

```bash
# .env file
FLASK_DEBUG=True
DATABASE_URL=sqlite:///data/chore_tracker.db
```

## Management Commands

### View Logs
```bash
# Docker Compose
docker-compose logs -f

# Docker
docker logs chore-tracker
```

### Stop/Start
```bash
# Docker Compose
docker-compose stop
docker-compose start

# Docker
docker stop chore-tracker
docker start chore-tracker
```

### Update Application
```bash
# Docker Compose
docker-compose down
git pull  # or update your code
docker-compose up -d --build

# Docker
docker stop chore-tracker
docker rm chore-tracker
docker build -t chore-tracker .
docker run -d [same parameters as before] chore-tracker
```

### Backup Database
```bash
# Copy the database file
cp chore_data/chore_tracker.db chore_data/chore_tracker.backup.db

# Or backup from running container
docker exec chore-tracker cp /app/data/chore_tracker.db /app/data/chore_tracker.backup.db
```

### Reset Database
```bash
# Stop the container
docker-compose down

# Remove the database
rm -rf chore_data/

# Start fresh
docker-compose up -d
```

## Troubleshooting

### Container Won't Start
```bash
# Check logs for errors
docker-compose logs

# Check if port 5000 is already in use
netstat -an | grep 5000

# Try a different port in docker-compose.yml
```

### Database Issues
```bash
# Check database file permissions
ls -la chore_data/

# Reset database (WARNING: This deletes all data)
docker-compose down
rm -rf chore_data/
docker-compose up -d
```

### Health Check Failing
- Ensure the application is accessible at `http://localhost:5000`
- Check that curl is available in the container
- Verify network connectivity

## Security Notes

- Change the `SECRET_KEY` in `config.py` for production use
- Consider using HTTPS in production
- The database file contains no sensitive information, but restrict access as needed
- Regularly backup your database

## Performance

- The application uses SQLite, which is suitable for small to medium usage
- For high-traffic scenarios, consider switching to PostgreSQL or MySQL
- Monitor disk usage in the `chore_data` directory

## Next Steps

1. **Customize Chores**: Visit the admin panel at `http://localhost:5000/admin` to add custom chores
2. **Set Up Notifications**: Configure reminders for daily bonuses
3. **Backup Regularly**: Set up automated backups of the `chore_data` directory
4. **Monitor Usage**: Check the logs directory for application insights

## Support

If you encounter issues:

1. Check the logs: `docker-compose logs -f`
2. Verify the health check: `curl http://localhost:5000/`
3. Ensure proper file permissions on the `chore_data` directory
4. Check Docker version compatibility (requires Docker 18.09+)