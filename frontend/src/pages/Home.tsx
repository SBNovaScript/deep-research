import React, { useState } from 'react';
import { useNavigate } from 'react-router';
import { startResearch } from '../lib/api';
import LoadingSpinner from '../components/LoadingSpinner';

export default function Home() {
  const [topic, setTopic] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const { id } = await startResearch(topic);
      navigate(`/task/${id}`);
    } catch (err) {
      console.error(err);
      alert('Failed to start research');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center p-4 gap-4">
      <h1 className="text-2xl font-bold">Deep Research</h1>
      <form onSubmit={handleSubmit} className="flex gap-2 w-full max-w-md">
        <input
          className="border rounded px-2 py-1 flex-1"
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
          placeholder="Enter research topic"
        />
        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-1 rounded flex items-center justify-center w-20"
          disabled={loading}
        >
          {loading ? <LoadingSpinner /> : 'Start'}
        </button>
      </form>
      {loading && <p>Starting research...</p>}
    </div>
  );
}
