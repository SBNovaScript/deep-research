export async function startResearch(topic: string) {
  const resp = await fetch('/api/research', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ topic }),
  });
  if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
  return resp.json() as Promise<{ id: string }>;
}

export async function fetchResult(id: string) {
  const resp = await fetch(`/api/research/${id}`);
  if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
  return resp.json() as Promise<{ id: string; result: string | null }>;
}
