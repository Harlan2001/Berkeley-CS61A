import matplotlib.pyplot as plt

# 数据
years = list(range(1977, 2025))
gdp_growth = [7.6, 11.67, 7.59, 7.83, 5.11, 9.02, 10.77, 15.19, 13.43, 8.95, 
              11.66, 11.22, 4.21, 3.92, 9.26, 14.22, 13.88, 13.04, 10.95, 9.92, 
              9.24, 7.85, 7.66, 8.49, 8.34, 9.13, 10.04, 10.11, 11.39, 12.72, 
              14.23, 9.65, 9.4, 10.64, 9.55, 7.86, 7.77, 7.43, 7.04, 6.85, 
              6.95, 6.75, 5.95, 2.24, 8.45, 3.0, 5.2, 5.0]

# 绘图
plt.figure(figsize=(12, 6))
plt.plot(years, gdp_growth, marker='o', linestyle='-', color='b', label='GDP 增速')

# 添加标题和标签
plt.title('中国GDP增速（1977-2024年）')
plt.xlabel('年份')
plt.ylabel('GDP 增速（%）')
plt.grid(True)
plt.legend()

# 旋转X轴刻度以更清晰显示
plt.xticks(rotation=45)

# 显示图形
plt.show()
