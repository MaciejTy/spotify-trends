import { useState, useEffect } from 'react';
import api from './api/client';

function App() {
  const [tracks, setTracks] = useState([]);
  const [markets, setMarkets] = useState([]);
  const [selectedMarket, setSelectedMarket] = useState('PL')

  useEffect(() => {
    console.log('Fetching tracks for:', selectedMarket);
    api.get(`/tracks?market=${selectedMarket}`).then(response => {
        console.log('Got tracks:', response.data.length);
        setTracks(response.data);
    });
    api.get('/markets').then(response => {
        setMarkets(response.data);
    });
}, [selectedMarket]);
 return (
    <div className="max-w-4xl mx-auto p-6">
        <h1 className="text-3xl font-bold mb-4">Spotify Trends</h1>
        <select className="border p-2 rounded mb-4" value={selectedMarket} onChange={e => setSelectedMarket(e.target.value)}>
            {markets.map(m => (
                <option key={m} value={m}>{{PL: 'Poland', US: 'United States', GB: 'United Kingdom'}[m] || m}</option>
            ))}
        </select>
        {tracks.map(track => (
            <div key={track.spotify_id} className="flex items-center gap-4 p-3 border-b">
                <img src={track.album_image} alt={track.album} className="w-12 h-12 rounded" />
                <div>
                    <p className="font-semibold">{track.name}</p>
                    <p className="text-sm text-gray-500">{track.artist} · {track.album}</p>
                </div>
                <div className="ml-auto text-center">
                    <span className="text-green-600 font-bold text-lg">{track.popularity}</span>
                    <p className="text-xs text-gray-400">popularity</p>
                </div>
            </div>
        ))}
    </div>
);
}

export default App;