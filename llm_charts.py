import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("llm_benchmark_comparison_2025_2026.csv")
group_data = data.groupby("organization")
mean_val = group_data["overall_benchmark_avg"].mean()
mean_val = mean_val.sort_values(ascending=False)

mean_val.plot(kind="bar")
plt.title("Average LLM Benchmark Score by Organization")
plt.xlabel("Organization")
plt.ylabel("Average Benchmark Score")
plt.tight_layout()
plt.show()