import pandas as pd
import os

# 确保csvs文件夹存在
os.makedirs("csvs", exist_ok=True)

df = pd.read_csv("我的学习记录_Aug 3, 2025-all copy.csv")
chunk_size = 50
for i in range(0, len(df), chunk_size):
    df[i:i+chunk_size].to_csv(f"csvs/chapter_{i//chunk_size+1}.csv", index=False)