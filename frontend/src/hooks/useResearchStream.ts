import { useEffect, useState } from 'react';

export default function useResearchStream(taskId: string) {
  const [messages, setMessages] = useState<string[]>([]);
  const [done, setDone] = useState(false);

  useEffect(() => {
    if (!taskId) return;
    const protocol = window.location.protocol === 'https:' ? 'wss' : 'ws';
    const ws = new WebSocket(`${protocol}://${window.location.host}/ws/research/${taskId}`);
    ws.onmessage = (event) => {
      const payload = JSON.parse(event.data);
      if (payload.message) setMessages((prev) => [...prev, payload.message]);
    };
    ws.onclose = () => setDone(true);
    ws.onerror = () => setDone(true);
    return () => ws.close();
  }, [taskId]);

  return { messages, done };
}
