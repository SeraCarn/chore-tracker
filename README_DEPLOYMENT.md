# Chore Tracker - Complete Docker Deployment Package

## 🎯 Quick Start

Deploy the Chore Tracker application in seconds with Docker:

```bash
# 1. Quick deployment
./deploy.sh

# 2. Open browser to http://localhost:5000

# 3. When done, cleanup
./cleanup.sh
```

## 📦 What's Included

### Core Docker Files
- **`Dockerfile`** - Multi-stage build with Python 3.12
- **`docker-compose.yml`** - Production-ready compose configuration
- **`.dockerignore`** - Optimized build context

### Management Scripts
- **`deploy.sh`** - One-click deployment script
- **`cleanup.sh`** - Complete cleanup and reset
- **`backup_db.sh`** - Database backup utility

### Configuration
- **`start_app.sh`** - Production startup script
- **Updated `app.py`** - Docker-aware configuration
- **Updated `setup.py`** - Robust database initialization

### Documentation
- **`DOCKER_DEPLOYMENT.md`** - Comprehensive deployment guide

## 🏗️ Architecture

```
┌───────────────────────┐       ┌─────────────────┐
│   Web Browser         │       │   Management    │
│                       │       │                 │
│ http://localhost:5000 │       │  ./deploy.sh    │
│                       │       │ ./backup_db.sh  │
│                       │       │ ./cleanup.sh    │
└─────────┬─────────────┘       └─────────┬───────┘
          │                               │
          │                               │
          ▼                               ▼
┌─────────────────┐           ┌─────────────────┐
│  Docker Host    │           │  Host Filesystem│
│                 │           │                 │
│ ┌─────────────┐ │           │ ┌─────────────┐ │
│ │Chore Tracker│ │           │ │ chore_data/ │ │
│ │ Container   │ │           │ │ └─ chore_   │ │
│ │             │ │           │ │   tracker.db│ │
│ │ Flask App   │ │           │ │             │ │
│ │ SQLite DB   │ │◄────────► │ │ logs/       │ │
│ │             │ │           │ │             │ │
│ │ Health      │ │           │ │ .env        │ │
│ │ Monitoring  │ │           │ │             │ │
│ └─────────────┘ │           │ └─────────────┘ │
│                 │           │                 │
│ Docker Network  │           │ Persistent      │
│ (Port 5000)     │           │ Storage         │
└─────────────────┘           └─────────────────┘
```       

## 🚀 Features

### ✅ Production Ready
- **Health Checks**: Automatic monitoring every 30 seconds
- **Auto Restart**: Container restarts on failure
- **Environment Variables**: Configurable settings
- **Logging**: Structured application logs

### ✅ Data Persistence
- **Volume Mapping**: Database stored outside container
- **Easy Backup**: Simple backup/restore scripts
- **Data Safety**: No data loss on container updates

### ✅ Easy Management
- **One-Click Deploy**: Automated setup and configuration
- **Status Monitoring**: Real-time container status
- **Cleanup Tools**: Complete removal and reset options
- **Backup System**: Automated database backups

### ✅ Security
- **Non-Root User**: Secure container execution
- **Minimal Image**: Reduced attack surface
- **Environment Isolation**: Separate from host system

## 📋 System Requirements

- **Docker**: 18.09+
- **Docker Compose**: 1.25+
- **RAM**: 256MB+ available
- **Storage**: 100MB+ for image + data storage

## 🔧 Configuration Options

### Environment Variables
```bash
# In .env file or docker-compose.yml
FLASK_ENV=production          # Environment mode
FLASK_DEBUG=False            # Debug mode
DATABASE_URL=sqlite:///data/chore_tracker.db  # DB location
FLASK_RUN_HOST=0.0.0.0       # Bind address
FLASK_RUN_PORT=5000          # Port number
```

### Custom Database Location
```yaml
# In docker-compose.yml
volumes:
  - /custom/path:/app/data
```

### Custom Port
```yaml
# In docker-compose.yml
ports:
  - "8080:5000"  # Map host port 8080 to container 5000
```

## 🛠️ Advanced Usage

### Custom Chores Setup
1. Deploy the application
2. Visit `http://localhost:5000/admin`
3. Add your custom chores and point values

### Database Migration
```bash
# Backup current data
./backup_db.sh

# Update application
docker-compose down
# Update your code...
docker-compose up -d --build

# Restore if needed
cp backups/latest_backup.db chore_data/chore_tracker.db
```

### Multi-Instance Deployment
```yaml
# In docker-compose.yml
services:
  chore-tracker-1:
    # ... config for instance 1
    ports:
      - "5000:5000"
  
  chore-tracker-2:
    # ... config for instance 2
    ports:
      - "5001:5000"
    volumes:
      - chore_data-2:/app/data
```

## 📊 Monitoring

### Health Check
```bash
# Manual health check
curl http://localhost:5000/

# Docker health status
docker-compose ps
```

### Logs
```bash
# View application logs
docker-compose logs -f chore-tracker

# View logs with timestamp
docker-compose logs -f --tail=100 chore-tracker
```

### Resource Usage
```bash
# Container resource usage
docker stats chore-tracker

# Disk usage
du -sh chore_data/
```

## 🆘 Troubleshooting

### Common Issues

**Port Already in Use**
```bash
# Find what's using port 5000
lsof -i :5000

# Use different port in docker-compose.yml
ports:
  - "5001:5000"
```

**Permission Denied**
```bash
# Fix permissions
sudo chown -R $USER:$USER chore_data/
sudo chown -R $USER:$USER logs/
```

**Container Won't Start**
```bash
# Check logs
docker-compose logs

# Rebuild image
docker-compose up -d --build --force-recreate
```

**Database Corruption**
```bash
# Restore from backup
cp backups/chore_tracker_backup_*.db chore_data/chore_tracker.db

# Or reset database
docker-compose down
rm -rf chore_data/
docker-compose up -d
```

## 🔄 Updates and Maintenance

### Regular Maintenance
```bash
# Weekly: Backup database
./backup_db.sh

# Monthly: Clean up old backups
ls -t backups/chore_tracker_backup_*.db | tail -n +6 | xargs rm

# As needed: Update application
docker-compose pull
docker-compose up -d --build
```

### Version Updates
```bash
# Update base image
# Edit Dockerfile to use newer Python version
docker-compose build --no-cache
docker-compose up -d

# Update dependencies
# Edit chore_tracker/requirements.txt
docker-compose build
docker-compose up -d
```

## 🎉 Success!

You now have a complete, production-ready Docker deployment of the Chore Tracker application with:

- ✅ Easy one-click deployment
- ✅ Persistent data storage
- ✅ Health monitoring
- ✅ Backup and recovery
- ✅ Clean management tools
- ✅ Comprehensive documentation

The application is ready for daily use and can be easily managed, updated, and maintained using the provided tools.

**Next Steps:**
1. Visit http://localhost:5000 to start using your chore tracker
2. Customize chores in the admin panel
3. Set up regular backups
4. Enjoy your gamified chore tracking experience! 🎮✨