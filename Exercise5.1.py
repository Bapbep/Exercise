import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('D:/download from the internet/github 文件/titanic.csv')

print(df['Survived'].unique())
df['Survived'] = df['Survived'].replace({'Zero': 0, 'One': 1})
df['Survived'] = df['Survived'].astype(int)

first_10 = df.head(10)
last_20 = df.tail(20)
info = df.info()
description = df.describe()
description_df = pd.DataFrame(description).T
combined_info = pd.concat([first_10, last_20, description_df], axis=0, ignore_index=True)
print(combined_info)

missing_values = df.isnull().sum()
print("Missing values in each column:\n", missing_values)

plt.figure(figsize=(10, 6))
sns.histplot(df['Age'].dropna(), bins=30, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

age_median = df['Age'].median()
print("Median Age:", age_median)
df['Age'].fillna(age_median, inplace=True)

df['Cabin'].fillna('Unknown', inplace=True)
embarked_mode = df['Embarked'].mode()[0]
df['Embarked'].fillna(embarked_mode, inplace=True)

print("Unique values in 'Survived':", df['Survived'].unique())
df['Survived'] = pd.to_numeric(df['Survived'], errors='coerce')
df['Survived'].fillna(df['Survived'].mode()[0], inplace=True)
df['Survived'] = df['Survived'].astype(int)

df['Fare'] = pd.to_numeric(df['Fare'], errors='coerce')
fare_median = df['Fare'].median()
df['Fare'].fillna(fare_median, inplace=True)

print("\nCleaned DataFrame Info:")
print(df.info())

df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Fare'] = pd.to_numeric(df['Fare'], errors='coerce')
df['Fare'].fillna(df['Fare'].median(), inplace=True)
df['Age'].fillna(df['Age'].median(), inplace=True)
df['FamilySize'] = df['SibSp'] + df['Parch']

sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'].dropna(), bins=30, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['Fare'].dropna(), bins=30, kde=True)
plt.title('Fare Distribution')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Pclass', palette='viridis')
plt.title('Passenger Class Distribution')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Survived', palette='pastel')
plt.title('Survival Distribution')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Embarked', palette='magma')
plt.title('Embarked Distribution')
plt.xlabel('Embarked')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Survived', y='Fare', data=df, palette='coolwarm')
plt.title('Fare Distribution by Survival')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Fare')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Pclass', y='Fare', data=df, palette='coolwarm')
plt.title('Fare Distribution by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Fare')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Survived', y='Age', data=df, palette='coolwarm')
plt.title('Age Distribution by Survival')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Age')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Pclass', y='Age', data=df, palette='coolwarm')
plt.title('Age Distribution by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Age')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='FamilySize', hue='Survived', data=df, palette='Set2')
plt.title('Family Size Distribution by Survival')
plt.xlabel('Family Size')
plt.ylabel('Count')
plt.legend(title='Survived', loc='upper right', labels=['No', 'Yes'])
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='FamilySize', hue='Pclass', data=df, palette='Set2')
plt.title('Family Size Distribution by Passenger Class')
plt.xlabel('Family Size')
plt.ylabel('Count')
plt.legend(title='Passenger Class', loc='upper right')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Age', y='Fare', hue='Survived', palette='deep', alpha=0.6)
plt.title('Scatter Plot of Age vs Fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.legend(title='Survived', loc='upper left', labels=['No', 'Yes'])
plt.show()

correlation_matrix = df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title('Correlation Matrix')
plt.show()

age_fare_corr = df['Age'].corr(df['Fare'])
print("Correlation between 'Age' and 'Fare':", age_fare_corr)

# Other possible correlations to explore:
# Correlation between 'Pclass' and 'Fare'
# Correlation between 'SibSp' and 'Survived'
# Correlation between 'Parch' and 'Survived'
# Correlation between 'Age' and 'Survived'
# Correlation between 'FamilySize' and 'Survived'




