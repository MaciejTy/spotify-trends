from sqlalchemy import (Integer, Column, ForeignKey, String, DateTime,
                        func, Float, UniqueConstraint, Date)
from sqlalchemy.orm import DeclarativeBase



class Base(DeclarativeBase):
    pass

class Track(Base):
    __tablename__ = 'tracks'
    spotify_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    album = Column(String)
    album_image = Column(String)
    popularity = Column(Integer)
    duration_ms = Column(Integer)
    preview_url = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())

# class AudioFeatures(Base):
#     __tablename__ = 'audio_features'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     track_id = Column(String, ForeignKey('tracks.spotify_id'))
#     acousticness = Column(Float)
#     danceability = Column(Float)
#     energy = Column(Float)
#     instrumentalness = Column(Float)
#     tempo = Column(Float)
#     loudness = Column(Float)
#     liveness = Column(Float)
#     speechiness = Column(Float)
#     fetched_at = Column(DateTime, server_default=func.now())
#     valence = Column(Float)

class ChartSnapshot(Base):
    __tablename__ = 'chart_snapshots'
    id = Column(Integer, primary_key=True, autoincrement=True)
    track_id = Column(String, ForeignKey('tracks.spotify_id'))
    market = Column(String)
    position = Column(Integer)
    snapshot_date = Column(Date)
    popularity = Column(Integer)

    __table_args__ = (
        UniqueConstraint('track_id', 'market', 'snapshot_date'),
    )





