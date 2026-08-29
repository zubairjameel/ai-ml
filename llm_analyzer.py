import pandas as pd

data = pd.read_csv("llm_benchmark_comparison_2025_2026.csv")
#print(data.columns)
#print(data.head())

sorted_val = data.sort_values(by="overall_benchmark_avg", ascending=False)
print(sorted_val.head(10))

group_data = data.groupby("organization")
mean_val = group_data["overall_benchmark_avg"].mean()
mean_val = mean_val.sort_values(ascending=False)
print(mean_val)

sort_by_dollars = data.sort_values(by="performance_per_dollar", ascending=False)
print(sort_by_dollars.head(5))
data["total_price"] = data["input_price_per_1m"] + data["output_price_per_1m"]
sort_price = data.sort_values(by="total_price", ascending=True)
print(sort_price[["model_name", "total_price"]].head(10))