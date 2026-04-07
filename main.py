import pandas  as pd
import matplotlib.pyplot as plt

# Local data
df = pd.read_csv("jobs.csv")

# Show first rows
print("\n Job Data Preview:")
print("df.head()")

# Top locations
print("\n Jobs by Location:")
print(df['location'].value_counts())

# Extract skills
all_skills = []

for skills in df['skills']:
    for skill in skills.split(","):
        all_skills.append(skill.strip())

skill_series = pd.Series(all_skills)

print("\n Top Skills in Demand:")
print(skill_series.value_counts())

# Average salary
print("\n Average Salary:")
print(df['salary'].mean())

skill_series.value_counts().head(5).plot(kind='bar')
plt.title("Top Skills in Demand")
plt.xlabel("Skills")
plt.ylabel("Number of Jobs")
plt.show()