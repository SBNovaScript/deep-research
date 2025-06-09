import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router';
import { fetchResult } from '../lib/api';
import useResearchStream from '../hooks/useResearchStream';

export default function Results() {
  const { id } = useParams<{ id: string }>();
  const [result, setResult] = useState<string | null>(null);
  const { messages, done } = useResearchStream(id!);

  useEffect(() => {
    if (!done || !id) return;
    (async () => {
      const res = await fetchResult(id);
      if (res.result) setResult(res.result);
    })();
  }, [done, id]);

  return (
    <div className="flex flex-col items-center p-4 gap-4 max-w-2xl mx-auto">
      <h1 className="text-xl font-bold">Research Progress</h1>
      <div className="w-full">
        <ul className="space-y-1">
          {messages.map((m, idx) => (
            <li key={idx} className="border p-2 rounded bg-gray-50 text-sm">
              {m}
            </li>
          ))}
        </ul>
        {done && result && (
          <pre className="border p-4 mt-4 whitespace-pre-wrap bg-white rounded">
            {result}
          </pre>
        )}
        {done && !result && (
          <p className="mt-2 text-gray-600">No final report yet.</p>
        )}
      </div>
      <Link to="/" className="text-blue-600 underline">Start New Research</Link>
    </div>
  );
}
