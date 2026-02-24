# 🎵 Spotify Trends Pipeline

A full-stack data pipeline that collects daily music release data from Spotify across multiple markets, tracks popularity changes over time, and visualizes trends through an interactive dashboard.

## Tech Stack

**Backend:** Python, FastAPI, SQLAlchemy, Alembic, APScheduler, Spotipy  
**Frontend:** React, Axios, Tailwind CSS  
**Database:** PostgreSQL  
**Infrastructure:** Docker, Docker Compose

## Architecture

```
Spotify API
     ↓
[Collector] → Fetches new releases & track details daily (APScheduler)
     ↓
[Processor] → Normalizes data, extracts popularity scores
     ↓
[PostgreSQL] → Stores tracks & daily popularity snapshots
     ↓
[FastAPI] → REST API serving processed data
     ↓
[React Dashboard] → Interactive UI with market filtering
```

## Features

- **Automated daily collection** of new music releases from Spotify across multiple markets (PL, US, UK)
- **Popularity tracking** over time — see how tracks rise and fall
- **Market comparison** — compare music trends across different countries
- **Interactive dashboard** with album artwork, popularity scores, and market selector
- **RESTful API** with clean endpoints for tracks, history, and markets

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/tracks?market=PL` | Top tracks for a given market, sorted by popularity |
| `GET` | `/api/tracks/{spotify_id}/history` | Popularity history of a specific track across markets |
| `GET` | `/api/markets` | List of available markets |

## Getting Started

### Prerequisites

- Docker & Docker Compose
- Spotify Developer account ([developer.spotify.com](https://developer.spotify.com))

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/MaciejTy/spotify-trends.git
   cd spotify-trends
   ```

2. **Configure environment**
   ```bash
   cp backend/.env.example backend/.env
   ```
   Edit `backend/.env` and add your Spotify API credentials:
   ```
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret
   DATABASE_URL=postgresql://postgres:postgres@db:5432/spotify_trends
   ```

3. **Run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

4. **Access the app**
   - Frontend: [http://localhost:3000](http://localhost:3000)
   - API: [http://localhost:8000/api/tracks?market=PL](http://localhost:8000/api/tracks?market=PL)
   - API Docs (Swagger): [http://localhost:8000/docs](http://localhost:8000/docs)

### Manual Setup (without Docker)

1. **Database**
   ```bash
   createdb spotify_trends
   ```

2. **Backend**
   ```bash
   cd backend
   pip install -r requirements.txt
   alembic upgrade head
   uvicorn app.main:app --reload
   ```

3. **Seed initial data**
   ```bash
   python3 -c "from app.collector.tasks import collect_data; collect_data()"
   ```

4. **Frontend**
   ```bash
   cd frontend
   npm install
   npm start
   ```

## Database Schema

```
tracks
├── spotify_id (PK)
├── name
├── artist
├── album
├── album_image
├── popularity
├── duration_ms
├── preview_url
└── created_at

chart_snapshots
├── id (PK)
├── track_id (FK → tracks.spotify_id)
├── market
├── position
├── snapshot_date
├── popularity
└── UNIQUE(track_id, market, snapshot_date)
```

## Future Improvements

- [ ] Audio features analysis (danceability, energy, valence) — pending Spotify API access restoration
- [ ] Migration from APScheduler to Celery + Redis for horizontal scaling
- [ ] Additional markets and genre-based filtering
- [ ] Historical trend charts with Recharts
- [ ] CI/CD pipeline with GitHub Actions
- [ ] Comprehensive test suite (pytest)

## License

MIT