"""Prompt templates used throughout the backend workflow."""

SUMMARY_TEMPLATE = (
    "You are an expert research assistant. Summarize the following text in a"
    " concise paragraph while preserving key details:\n{text}"
)

FACT_CHECK_TEMPLATE = (
    "You are a fact-checking AI. Analyze the text below and list any"
    " inaccuracies or reply 'OK' if everything is supported by the context:\n{text}"
)

BIAS_CHECK_TEMPLATE = (
    "You are a bias detection AI. Identify any biased language or unfair"
    " assumptions in the following text. If none are present, reply 'No bias found.':\n{text}"
)
