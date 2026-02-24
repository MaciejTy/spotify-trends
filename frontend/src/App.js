import { useState, useEffect } from 'react';
import api from './api/client';

const MARKET_NAMES = {
  PL: 'Poland',
  US: 'United States',
  GB: 'United Kingdom',
};

function formatDuration(ms) {
  const minutes = Math.floor(ms / 60000);
  const seconds = Math.floor((ms % 60000) / 1000);
  return `${minutes}:${seconds.toString().padStart(2, '0')}`;
}

function App() {
  const [tracks, setTracks] = useState([]);
  const [markets, setMarkets] = useState([]);
  const [selectedMarket, setSelectedMarket] = useState('PL');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get('/markets').then(response => {
      setMarkets(response.data);
    });
  }, []);

  useEffect(() => {
    setLoading(true);
    api.get(`/tracks?market=${selectedMarket}`).then(response => {
      setTracks(response.data);
      setLoading(false);
    });
  }, [selectedMarket]);

  return (
    <div className="min-h-screen bg-zinc-950 text-white">
      <div className="max-w-4xl mx-auto p-6">

        <div className="flex items-center gap-3 mb-8">
          <div className="w-10 h-10 bg-green-500 rounded-full flex items-center justify-center">
            <svg className="w-5 h-5 text-black" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.841.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.601.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.539.3.719 1.02.419 1.56-.299.421-1.02.599-1.559.3z"/>
            </svg>
          </div>
          <h1 className="text-3xl font-bold">Spotify Trends</h1>
        </div>

        <div className="mb-6">
          <select
            className="bg-zinc-800 border border-zinc-700 text-white p-2.5 rounded-lg focus:border-green-500 focus:outline-none"
            value={selectedMarket}
            onChange={e => setSelectedMarket(e.target.value)}
          >
            {markets.map(m => (
              <option key={m} value={m}>{MARKET_NAMES[m] || m}</option>
            ))}
          </select>
        </div>

        {loading ? (
          <div className="flex justify-center items-center py-20">
            <div className="w-8 h-8 border-2 border-zinc-700 border-t-green-500 rounded-full animate-spin"></div>
          </div>
        ) : (
          <div className="bg-zinc-900 rounded-xl overflow-hidden">
            <div className="grid grid-cols-[3rem_3rem_1fr_auto] gap-4 px-4 py-3 text-xs text-zinc-500 uppercase tracking-wider border-b border-zinc-800">
              <span>#</span>
              <span></span>
              <span>Title</span>
              <span className="text-right">Popularity</span>
            </div>

            {tracks.map((track, index) => (
              <div
                key={track.spotify_id}
                className="grid grid-cols-[3rem_3rem_1fr_auto] gap-4 px-4 py-3 items-center hover:bg-zinc-800 transition-colors cursor-default group"
              >
                <span className="text-zinc-500 text-sm">{index + 1}</span>

                <img
                  src={track.album_image}
                  alt={track.album}
                  className="w-10 h-10 rounded shadow-md"
                />

                <div className="min-w-0">
                  <p className="font-medium truncate group-hover:text-green-400 transition-colors">
                    {track.name}
                  </p>
                  <p className="text-sm text-zinc-400 truncate">
                    {track.artist} &middot; {track.album} &middot; {formatDuration(track.duration_ms)}
                  </p>
                </div>

                <div className="flex items-center gap-3 pl-4">
                  <div className="w-24 h-1.5 bg-zinc-800 rounded-full overflow-hidden">
                    <div
                      className="h-full bg-green-500 rounded-full"
                      style={{ width: `${track.popularity}%` }}
                    />
                  </div>
                  <span className="text-green-400 font-semibold text-sm w-7 text-right">
                    {track.popularity}
                  </span>
                </div>
              </div>
            ))}

            {tracks.length === 0 && (
              <div className="text-center py-12 text-zinc-500">
                No tracks found
              </div>
            )}
          </div>
        )}

        <p className="text-center text-zinc-600 text-xs mt-6">
          {tracks.length} tracks &middot; Updated daily at 03:00 UTC
        </p>
      </div>
    </div>
  );
}

export default App;
