import pandas  as pd

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