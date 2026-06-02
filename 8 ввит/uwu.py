import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns # Для быстрой загрузки, если нет локального файла

# Задание 1: Загрузка и ознакомление
try:
    df = pd.read_csv("titanic.csv")
except FileNotFoundError:
    df = sns.load_dataset("titanic") # Загрузка из seaborn, если файла нет

print("Первые строки:\n", df.head())
print("\nТипы данных:\n", df.dtypes)
print("\nСтатистики:\n", df.describe())

# Задание 2: Фильтрация
adults = df[df["age"] >= 18]
women = df[df["sex"] == "female"]
first_class = df[df["pclass"] == 1]
print(f"\nФильтрация -> Взрослых: {len(adults)}, Женщин: {len(women)}, 1 класс: {len(first_class)}")

# Задание 3: Сравнение NumPy и Pandas
mean_age_np = np.mean(df["age"].dropna())
max_fare_np = np.max(df["fare"])
mean_age_pd = df["age"].mean()
print(f"\nСравнение: NumPy (Ср. возраст {mean_age_np:.2f}) == Pandas (Ср. возраст {mean_age_pd:.2f})")

# Задание 4: Группировка
grouped = df.groupby(["sex", "pclass"]).agg(
    survival_rate=("survived", "mean"),
    mean_fare=("fare", "mean"),
    mean_age=("age", "mean")
)
print("\nГруппировка (Пол и Класс):\n", grouped)

# Задание 5: Обработка пропусков
print("\nПропуски до обработки:\n", df.isnull().sum())
df["age"] = df["age"].fillna(df["age"].median())
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])

# Задание 6: Визуализация
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 6.1 Гистограмма возраста
df["age"].plot(kind="hist", bins=20, edgecolor="black", ax=axes[0], color="skyblue")
axes[0].set_title("Распределение возраста")
axes[0].set_xlabel("Возраст")

# 6.2 Доля выживших по полу
survival_by_sex = df.groupby("sex")["survived"].mean()
survival_by_sex.plot(kind="bar", color=["salmon", "lightgreen"], ax=axes[1], edgecolor="black")
axes[1].set_title("Доля выживших по полу")
axes[1].set_ylabel("Доля выживших")
axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=0)

# 6.3 Зависимость от класса
survival_by_class = df.groupby("pclass")["survived"].mean()
survival_by_class.plot(kind="bar", color=["gold", "silver", "#cd7f32"], ax=axes[2], edgecolor="black")
axes[2].set_title("Выживаемость по классу")
axes[2].set_ylabel("Доля выживших")
axes[2].set_xticklabels(axes[2].get_xticklabels(), rotation=0)

plt.tight_layout()
plt.show()