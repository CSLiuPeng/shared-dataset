import pandas as pd

# 读取Excel文件
df = pd.read_excel('/Users/liupeng/Desktop/csdn采集/原始数据表.xlsx')

# 获取总行数
total_rows = len(df)

# 计算拆分点
split_point = total_rows // 2

# 拆分数据
df_first_half = df.iloc[:split_point]
df_second_half = df.iloc[split_point:]

# 保存拆分后的数据到新的Excel文件
df_first_half.to_excel('/Users/liupeng/Desktop/csdn采集/first_half.xlsx', index=False)
df_second_half.to_excel('/Users/liupeng/Desktop/csdn采集/second_half.xlsx', index=False)

print("数据已成功拆分并保存到first_half.xlsx和second_half.xlsx")