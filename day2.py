import pandas as pd

data = {
    "name": ["Aman", "Priya", "Rahul", "Sneha", "Arjun"],
    "python": [85, 90, 60, 95, 70],
    "sql": [75, 80, 65, 90, 70],
    "experience": [1, 2, 0, 3, 1]
}

df = pd.DataFrame(data)

print(df.describe())
print(df[df["python"] >= 80])