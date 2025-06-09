import React, { useState } from 'react';

export default function App() {
  const [topic, setTopic] = useState('');
  const [taskId, setTaskId] = useState<string | null>(null);
  const [messages, setMessages] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setMessages([]);
    setTaskId(null);

    try {
      const resp = await fetch('/api/research', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ topic }),
      });

      if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
      const data = await resp.json();
      setTaskId(data.id);

      const protocol = window.location.protocol === 'https:' ? 'wss' : 'ws';
      const ws = new WebSocket(`${protocol}://${window.location.host}/ws/research/${data.id}`);
      ws.onmessage = (event) => {
        const payload = JSON.parse(event.data);
        if (payload.message) {
          setMessages((prev) => [...prev, payload.message]);
        }
      };
      ws.onclose = () => setLoading(false);
    } catch (err) {
      console.error(err);
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-4">
      <h1 className="text-2xl font-bold mb-4">Deep Research</h1>
      <form onSubmit={handleSubmit} className="flex gap-2">
        <input
          className="border rounded px-2 py-1"
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
          placeholder="Enter research topic"
        />
        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-1 rounded"
        >
          Start
        </button>
      </form>
      {loading && <p className="mt-2">Waiting for results...</p>}
      {messages.length > 0 && (
        <ul className="mt-4 space-y-1">
          {messages.map((m, i) => (
            <li key={i} className="border p-2 rounded bg-gray-100 w-full max-w-md text-sm">{m}</li>
          ))}
        </ul>
      )}
    </div>
  );
}
