"""
Read results.csv from measure.py and produce:
  - Histograms of total latency and TTFT, with P50/P90/P95/P99 lines
  - CDF plots for both metrics
  - A printed summary table
"""

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

INPUT_CSV = "results.csv"
PERCENTILES = [50, 90, 95, 99]
BUCKET_COLORS = {"short": "#4C9EEB", "medium": "#E0853A", "long": "#5BB17F"}


def load() -> dict:
    """Return {bucket: {'ttft': [...], 'total': [...]}, ...} in seconds."""
    data: dict = {}
    with open(INPUT_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("error"):
                continue
            bucket = row["bucket"]
            d = data.setdefault(bucket, {"ttft": [], "total": []})
            if row["ttft_ms"]:
                d["ttft"].append(float(row["ttft_ms"]) / 1000)
            d["total"].append(float(row["total_ms"]) / 1000)
    return data


def percentiles(values: list[float]) -> dict:
    arr = np.array(values)
    return {p: float(np.percentile(arr, p)) for p in PERCENTILES}


def print_summary(data: dict) -> None:
    print(f"\n{'bucket':<10} {'metric':<8} {'n':>5} {'mean(s)':>8} {'P50':>8} {'P90':>8} {'P95':>8} {'P99':>8} {'max':>8}")
    print("-" * 76)
    rows = []
    for bucket in sorted(data):
        for metric in ("ttft", "total"):
            vals = data[bucket][metric]
            if not vals:
                continue
            rows.append((bucket, metric, vals))

    all_ttft, all_total = [], []
    for bucket, metric, vals in rows:
        pct = percentiles(vals)
        print(f"{bucket:<10} {metric:<8} {len(vals):>5} {np.mean(vals):>8.2f} "
              f"{pct[50]:>8.2f} {pct[90]:>8.2f} {pct[95]:>8.2f} {pct[99]:>8.2f} {max(vals):>8.2f}")
        if metric == "ttft":
            all_ttft.extend(vals)
        else:
            all_total.extend(vals)

    print("-" * 76)
    for label, vals in (("ALL", all_ttft), ("ALL", all_total)):
        metric = "ttft" if vals is all_ttft else "total"
        if not vals:
            continue
        pct = percentiles(vals)
        print(f"{label:<10} {metric:<8} {len(vals):>5} {np.mean(vals):>8.2f} "
              f"{pct[50]:>8.2f} {pct[90]:>8.2f} {pct[95]:>8.2f} {pct[99]:>8.2f} {max(vals):>8.2f}")


def plot_metric(data: dict, metric: str, title: str) -> None:
    """One figure: histogram (left) + CDF (right) for a given metric."""
    fig, (ax_hist, ax_cdf) = plt.subplots(1, 2, figsize=(13, 5))
    fig.suptitle(title, fontsize=14)

    combined = []
    for bucket in sorted(data):
        vals = data[bucket][metric]
        if not vals:
            continue
        combined.extend(vals)
        color = BUCKET_COLORS.get(bucket, "gray")
        ax_hist.hist(vals, bins=20, alpha=0.5, label=f"{bucket} (n={len(vals)})", color=color)

        sorted_vals = np.sort(vals)
        cdf = np.arange(1, len(sorted_vals) + 1) / len(sorted_vals)
        ax_cdf.plot(sorted_vals, cdf, label=bucket, color=color, linewidth=2)

    if not combined:
        plt.close(fig)
        return

    pct = percentiles(combined)
    mean_val = float(np.mean(combined))

    # Histogram: percentile + mean lines on combined data
    for p in PERCENTILES:
        ax_hist.axvline(pct[p], color="red", linestyle="--", linewidth=1, alpha=0.7)
        ax_hist.text(pct[p], ax_hist.get_ylim()[1] * 0.95, f"P{p}={pct[p]:.2f}s",
                     rotation=90, color="red", fontsize=9, ha="right", va="top")
    ax_hist.axvline(mean_val, color="black", linestyle=":", linewidth=1.5)
    ax_hist.text(mean_val, ax_hist.get_ylim()[1] * 0.55, f"mean={mean_val:.2f}s",
                 rotation=90, color="black", fontsize=9, ha="right", va="top")
    ax_hist.set_xlabel("seconds")
    ax_hist.set_ylabel("requests")
    ax_hist.set_title("Histogram (combined percentiles overlaid)")
    ax_hist.legend(loc="upper right")

    # CDF: horizontal reference lines at percentiles
    for p in PERCENTILES:
        ax_cdf.axhline(p / 100.0, color="red", linestyle="--", linewidth=0.8, alpha=0.5)
        ax_cdf.text(ax_cdf.get_xlim()[1], p / 100.0, f" P{p}", color="red", fontsize=9, va="center")
    ax_cdf.set_xlabel("seconds")
    ax_cdf.set_ylabel("cumulative fraction")
    ax_cdf.set_title("CDF (per bucket)")
    ax_cdf.set_ylim(0, 1.05)
    ax_cdf.legend(loc="lower right")

    output_path = Path(__file__).parent / f"{metric}_latency.png"
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    print(f"Saved {output_path}")
    plt.tight_layout()


def main() -> None:
    data = load()
    if not data:
        print("No usable rows in results.csv (all errors or file empty).")
        return
    print_summary(data)
    plot_metric(data, "total", "Total latency")
    plot_metric(data, "ttft", "Time to first token (TTFT)")
    plt.show()


if __name__ == "__main__":
    main()
