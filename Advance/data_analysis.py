import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Kiran", "Anita"],
    "Maths": [78, 85, 62, 90, 55, 88],
    "Science": [82, 79, 68, 92, 60, 91],
    "English": [75, 80, 70, 88, 58, 86]
}

df = pd.DataFrame(data)

df["Total"] = df["Maths"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

print(df)

plt.figure()
plt.bar(df["Name"], df["Total"])
plt.title("Total Marks of Students")
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.show()

plt.figure()
plt.plot(df["Name"], df["Average"], marker='o')
plt.title("Average Marks of Students")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.show()