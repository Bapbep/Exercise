import pandas as pd
import numpy as np
import time

# 生成指定大小的数据集
size = 1_000_000

# 使用 Pandas 生成随机整数数据，并记录操作时间
start_time_pandas = time.time()
pandas_data = pd.DataFrame({'random_values': np.random.randint(1, 100, size)})
end_time_pandas = time.time()
pandas_time = end_time_pandas - start_time_pandas

# 使用 NumPy 生成随机整数数据，并记录操作时间
start_time_numpy = time.time()
numpy_data = np.random.randint(1, 100, size)
end_time_numpy = time.time()
numpy_time = end_time_numpy - start_time_numpy

# 输出时间比较结果
print(f"Pandas 生成数据集的时间: {pandas_time:.5f} 秒")
print(f"NumPy 生成数据集的时间: {numpy_time:.5f} 秒")

# 比较结果
if pandas_time > numpy_time:
    print(f"NumPy 更快，时间减少了 {pandas_time - numpy_time:.5f} 秒")
else:
    print(f"Pandas 更快，时间减少了 {numpy_time - pandas_time:.5f} 秒")

# 可选: 如果需要验证生成的数据，可以输出前几项查看
print("Pandas 数据集的前 5 项:\n", pandas_data.head())
print("NumPy 数据集的前 5 项:\n", numpy_data[:5])



import pandas as pd
import numpy as np
import time

# 1. 使用 Pandas 加载数据并计算基本统计量
start_time_pandas = time.time()

# 加载数据集
sleep_data_pd = pd.read_csv('D:\download from the internet\sleep_health.csv')

# 计算指定列的均值
pandas_means = sleep_data_pd[['Sleep Duration', 'Systolic blood pressure', 'Diastolic blood pressure', 'Heart Rate', 'Daily Steps']].mean()

# 计算相关性
pandas_correlations = sleep_data_pd.corr()
sleep_age_corr_pd = pandas_correlations.loc['Sleep Duration', 'Age']
sleep_hr_corr_pd = pandas_correlations.loc['Sleep Duration', 'Heart Rate']
sleep_steps_corr_pd = pandas_correlations.loc['Sleep Duration', 'Daily Steps']

# 计算睡眠时长的标准差
pandas_sleep_std = sleep_data_pd['Sleep Duration'].std()
end_time_pandas = time.time()

# 记录 Pandas 操作时间
pandas_time = end_time_pandas - start_time_pandas

# 2. 使用 NumPy 加载数据并计算基本统计量
start_time_numpy = time.time()

# 加载数据集 (使用 np.genfromtxt)
data_np = np.genfromtxt('D:\download from the internet\sleep_health.csv', delimiter=',', skip_header=1, encoding='utf-8')

# 提取每个列（假设列顺序为：Age, Gender, Sleep Duration, Systolic Blood Pressure, Diastolic Blood Pressure, Heart Rate, Daily Steps）
age = data_np[:, 2]  # 修改为实际列索引
sleep_duration = data_np[:, 4]
systolic_bp = data_np[:, 9]
diastolic_bp = data_np[:, 10]
heart_rate = data_np[:, 11]
daily_steps = data_np[:, 12]

# 计算均值
numpy_means = np.array([np.mean(sleep_duration), np.mean(systolic_bp), np.mean(diastolic_bp), np.mean(heart_rate), np.mean(daily_steps)])

# 计算相关性
sleep_age_corr_np = np.corrcoef(sleep_duration, age)[0, 1]
sleep_hr_corr_np = np.corrcoef(sleep_duration, heart_rate)[0, 1]
sleep_steps_corr_np = np.corrcoef(sleep_duration, daily_steps)[0, 1]

# 计算睡眠时长的标准差
numpy_sleep_std = np.std(sleep_duration)

end_time_numpy = time.time()

# 记录 NumPy 操作时间
numpy_time = end_time_numpy - start_time_numpy

# 输出结果
print(f"Pandas 计算时间: {pandas_time:.5f} 秒")
print(f"NumPy 计算时间: {numpy_time:.5f} 秒")

# 输出均值
print("\nPandas 均值:\n", pandas_means)
print("\nNumPy 均值:\n", numpy_means)

# 输出相关性
print(f"\nPandas 相关性:\n 睡眠时长和年龄: {sleep_age_corr_pd:.5f}\n 睡眠时长和心率: {sleep_hr_corr_pd:.5f}\n 睡眠时长和日常步数: {sleep_steps_corr_pd:.5f}")
print(f"\nNumPy 相关性:\n 睡眠时长和年龄: {sleep_age_corr_np:.5f}\n 睡眠时长和心率: {sleep_hr_corr_np:.5f}\n 睡眠时长和日常步数: {sleep_steps_corr_np:.5f}")

# 输出标准差
print(f"\nPandas 睡眠时长标准差: {pandas_sleep_std:.5f}")
print(f"NumPy 睡眠时长标准差: {numpy_sleep_std:.5f}")

# 比较时间
if pandas_time > numpy_time:
    print(f"\nNumPy 更快，时间减少了 {pandas_time - numpy_time:.5f} 秒")
else:
    print(f"\nPandas 更快，时间减少了 {numpy_time - pandas_time:.5f} 秒")
    
    
    
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

# 加载数据集
data_path = 'D:\download from the internet\sleep_health.csv'
sleep_data = pd.read_csv(data_path)

# 检查数据集的列名
print("Columns in dataset:", sleep_data.columns)

# Pandas 实现可视化
start_time_pandas = time.time()

# 1.1. Age 分布图
sns.histplot(sleep_data['Age'], kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# 1.2. Sleep Duration 分布图
sns.histplot(sleep_data['Sleep Duration'], kde=True)
plt.title('Sleep Duration Distribution')
plt.xlabel('Sleep Duration (Hours)')
plt.ylabel('Frequency')
plt.show()

# 1.3. Quality of Sleep 分布图
sns.countplot(x='Quality of Sleep', data=sleep_data)
plt.title('Quality of Sleep Distribution')
plt.xlabel('Quality of Sleep')
plt.ylabel('Count')
plt.show()

# 1.4. Physical Activity Level 分布图
sns.countplot(x='Physical Activity Level', data=sleep_data)
plt.title('Physical Activity Level Distribution')
plt.xlabel('Physical Activity Level')
plt.ylabel('Count')
plt.show()

# 1.5. Stress Level 分布图
sns.countplot(x='Stress Level', data=sleep_data)
plt.title('Stress Level Distribution')
plt.xlabel('Stress Level')
plt.ylabel('Count')
plt.show()

# 1.6. Heart Rate 分布图
sns.histplot(sleep_data['Heart Rate'], kde=True)
plt.title('Heart Rate Distribution')
plt.xlabel('Heart Rate')
plt.ylabel('Frequency')
plt.show()

# 3.1. 基于 'Quality of Sleep' 的 'Sleep Duration' 分布
sns.boxplot(x='Quality of Sleep', y='Sleep Duration', data=sleep_data)
plt.title('Sleep Duration based on Quality of Sleep')
plt.show()

# 3.2. 基于 'Stress Level' 的 'Sleep Duration' 分布
sns.boxplot(x='Stress Level', y='Sleep Duration', data=sleep_data)
plt.title('Sleep Duration based on Stress Level')
plt.show()

# 3.3. 基于 'Physical Activity Level' 的 'Sleep Duration' 分布
sns.boxplot(x='Physical Activity Level', y='Sleep Duration', data=sleep_data)
plt.title('Sleep Duration based on Physical Activity Level')
plt.show()

# 3.4. 基于 'Occupation' 的 'Sleep Duration' 分布
sns.boxplot(x='Occupation', y='Sleep Duration', data=sleep_data)
plt.title('Sleep Duration based on Occupation')
plt.show()

# 3.5. 基于 'BMI' 的 'Sleep Duration' 分布（修改后的检查逻辑）
if 'BMI' in sleep_data.columns:
    sns.boxplot(x='BMI', y='Sleep Duration', data=sleep_data)
    plt.title('Sleep Duration based on BMI')
    plt.show()
else:
    print("Column 'BMI' not found in the dataset. Skipping this visualization.")

# 5.1. Age 与 Sleep Duration 的关系
sns.scatterplot(x='Age', y='Sleep Duration', data=sleep_data)
plt.title('Age vs. Sleep Duration')
plt.show()

# 5.2. Sleep Duration 与 Heart Rate 的关系
sns.scatterplot(x='Sleep Duration', y='Heart Rate', data=sleep_data)
plt.title('Sleep Duration vs. Heart Rate')
plt.show()

# 5.3. Heart Rate 与 Daily Steps 的关系
sns.scatterplot(x='Heart Rate', y='Daily Steps', data=sleep_data)
plt.title('Heart Rate vs. Daily Steps')
plt.show()

# 5.4. Sleep Duration 与 Daily Steps 的关系
sns.scatterplot(x='Sleep Duration', y='Daily Steps', data=sleep_data)
plt.title('Sleep Duration vs. Daily Steps')
plt.show()

end_time_pandas = time.time()

# 记录 Pandas 可视化的执行时间
pandas_time = end_time_pandas - start_time_pandas
print(f"Pandas 可视化时间: {pandas_time:.5f} 秒")

# NumPy 实现可视化
start_time_numpy = time.time()

# 使用 NumPy 加载数据
data_np = np.genfromtxt(data_path, delimiter=',', skip_header=1, encoding='utf-8')

# 提取各列数据（注意列顺序的调整）
age = data_np[:, 2]
sleep_duration = data_np[:, 4]
quality_of_sleep = data_np[:, 5]
physical_activity = data_np[:, 6]
stress_level = data_np[:, 7]
heart_rate = data_np[:, 8]

# 1. 使用 NumPy 和 matplotlib 绘制各列分布
plt.hist(age, bins=30, color='skyblue')
plt.title('Age Distribution (NumPy)')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

plt.hist(sleep_duration, bins=30, color='lightgreen')
plt.title('Sleep Duration Distribution (NumPy)')
plt.xlabel('Sleep Duration')
plt.ylabel('Frequency')
plt.show()

# 3. 使用 NumPy 绘制箱线图（以 Quality of Sleep 为例）
quality_sleep_list = [sleep_duration[quality_of_sleep == i] for i in np.unique(quality_of_sleep)]
plt.boxplot(quality_sleep_list, labels=np.unique(quality_of_sleep))
plt.title('Sleep Duration based on Quality of Sleep (NumPy)')
plt.xlabel('Quality of Sleep')
plt.ylabel('Sleep Duration')
plt.show()

end_time_numpy = time.time()

# 记录 NumPy 可视化的执行时间
numpy_time = end_time_numpy - start_time_numpy
print(f"NumPy 可视化时间: {numpy_time:.5f} 秒")

# 比较两者的执行时间
if pandas_time > numpy_time:
    print(f"\nNumPy 更快，时间减少了 {pandas_time - numpy_time:.5f} 秒")
else:
    print(f"\nPandas 更快，时间减少了 {numpy_time - pandas_time:.5f} 秒")



