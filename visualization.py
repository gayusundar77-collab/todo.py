import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("placement.csv")

# Style
sns.set_style("whitegrid")

# 1. Placement Distribution
plt.figure(figsize=(6,4))
sns.countplot(x="placed", data=df)
plt.title("Placement Distribution")
plt.savefig("placement_distribution.png")
plt.show()

# 2. CGPA vs Placement
plt.figure(figsize=(6,4))
sns.boxplot(x="placed", y="cgpa", data=df)
plt.title("CGPA vs Placement")
plt.savefig("cgpa_vs_placement.png")
plt.show()

# 3. Technical Skills vs Placement
plt.figure(figsize=(6,4))
sns.boxplot(x="placed", y="technical_skills_score", data=df)
plt.title("Technical Skills vs Placement")
plt.savefig("technical_skills_vs_placement.png")
plt.show()

# 4. Aptitude Score Distribution
plt.figure(figsize=(6,4))
sns.histplot(df["aptitude_score"], bins=20, kde=True)
plt.title("Aptitude Score Distribution")
plt.savefig("aptitude_distribution.png")
plt.show()

# 5. Correlation Heatmap
plt.figure(figsize=(12,8))

numeric_df = df.select_dtypes(include=["int64","float64"])

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Feature Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()

print("Visualizations Created Successfully")