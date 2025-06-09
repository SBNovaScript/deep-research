import React, { useState } from 'react';

export default function App() {
  const [topic, setTopic] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // TODO: integrate with backend API
    console.log('Submitted topic:', topic);
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
    </div>
  );
}
