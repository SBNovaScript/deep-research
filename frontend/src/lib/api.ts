export interface ResearchResponse {
  id: string;
  result: string | null;
}

const API_BASE = import.meta.env.RESEARCH_API_URL ?? '';

export async function startResearch(topic: string): Promise<ResearchResponse> {
  const resp = await fetch(`${API_BASE}/api/research`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ topic }),
  });
  if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
  return resp.json() as Promise<ResearchResponse>;
}

export async function fetchResult(id: string): Promise<ResearchResponse> {
  const resp = await fetch(`${API_BASE}/api/research/${id}`);
  if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
  return resp.json() as Promise<ResearchResponse>;
}
