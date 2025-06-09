import { useEffect, useState } from 'react';

interface StreamMessage {
  type: 'thinking' | 'search' | 'citation' | 'final';
  text?: string;
  url?: string;
}

export default function useResearchStream(taskId: string) {
  const [messages, setMessages] = useState<string[]>([]);
  const [done, setDone] = useState(false);

  useEffect(() => {
    if (!taskId) return;
    const apiBase = import.meta.env.RESEARCH_API_URL || window.location.origin;
    const url = new URL(`/api/ws/research/${taskId}`, apiBase);
    url.protocol = url.protocol === 'https:' ? 'wss:' : 'ws:';
    const ws = new WebSocket(url.toString());
    ws.onmessage = (event) => {
      const payload: StreamMessage = JSON.parse(event.data);
      switch (payload.type) {
        case 'thinking':
          if (payload.text)
            setMessages((prev) => [...prev, payload.text]);
          break;
        case 'search':
          if (payload.url)
            setMessages((prev) => [...prev, `Searching ${payload.url}`]);
          break;
        case 'citation':
          if (payload.url)
            setMessages((prev) => [...prev, `Cited ${payload.url}`]);
          break;
        case 'final':
          if (payload.text)
            setMessages((prev) => [...prev, payload.text]);
          break;
        default:
          break;
      }
    };
    ws.onclose = () => setDone(true);
    ws.onerror = () => setDone(true);
    return () => ws.close();
  }, [taskId]);

  return { messages, done };
}
