"""
Send a bucketed mix of requests to OpenRouter, measure TTFT and total latency
per request, and write the raw timings to results.csv.
"""

import csv
import json
import os
import random
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["OPENROUTER_API_KEY"]
URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "baidu/cobuddy:free"
SLEEP_BETWEEN = 1.0
OUTPUT_CSV = "results.csv"
PROMPTS_DIR = Path(__file__).parent / "prompts"
BUCKETS = ["short", "medium"]


def load_prompts(bucket: str) -> list[str]:
    text = (PROMPTS_DIR / f"{bucket}.md").read_text(encoding="utf-8")
    parts = [p.strip() for p in text.split("\n---\n")]
    return [p for p in parts if p]


def send_streaming(prompt: str):
    """Send one streaming request. Return (ttft_ms, total_ms, output_tokens, error)."""
    body = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": True,
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    t0 = time.perf_counter()
    ttft = None
    output_tokens = 0

    try:
        resp = requests.post(URL, json=body, headers=headers, stream=True, timeout=120)
        resp.raise_for_status()

        for raw in resp.iter_lines(decode_unicode=True):
            if not raw or not raw.startswith("data: "):
                continue
            payload = raw[len("data: "):]
            if payload.strip() == "[DONE]":
                break
            try:
                chunk = json.loads(payload)
            except json.JSONDecodeError:
                continue
            delta = chunk.get("choices", [{}])[0].get("delta", {}).get("content")
            if delta:
                if ttft is None:
                    ttft = (time.perf_counter() - t0) * 1000.0
                output_tokens += 1

        total = (time.perf_counter() - t0) * 1000.0
        return ttft, total, output_tokens, None

    except Exception as e:
        total = (time.perf_counter() - t0) * 1000.0
        return ttft, total, output_tokens, str(e)


def main():
    plan = []
    for bucket in BUCKETS:
        for prompt in load_prompts(bucket):
            plan.append((bucket, prompt))
    random.shuffle(plan)
    print(f"Loaded {len(plan)} prompts across buckets: {BUCKETS}")

    rows = []
    for i, (bucket, prompt) in enumerate(plan, start=1):
        ttft, total, out_tokens, err = send_streaming(prompt)
        rows.append({
            "bucket": bucket,
            "prompt_len": len(prompt),
            "output_tokens": out_tokens,
            "ttft_ms": f"{ttft:.1f}" if ttft is not None else "",
            "total_ms": f"{total:.1f}",
            "error": err or "",
        })
        if err:
            print(f"[{i}/{len(plan)}] bucket={bucket} ERROR: {err}")
        else:
            ttft_str = f"{ttft:.0f}" if ttft is not None else "n/a"
            print(f"[{i}/{len(plan)}] bucket={bucket} ttft={ttft_str}ms total={total:.0f}ms tokens={out_tokens}")
        time.sleep(SLEEP_BETWEEN)

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["bucket", "prompt_len", "output_tokens", "ttft_ms", "total_ms", "error"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nWrote {len(rows)} rows to {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
