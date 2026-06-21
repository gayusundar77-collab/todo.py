import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load Dataset
df = pd.read_csv("placement.csv")

# Encode Categorical Columns
categorical_cols = [
    "gender",
    "city_tier",
    "ssc_board",
    "hsc_board",
    "hsc_stream",
    "degree_field",
    "specialization"
]

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

# Features & Target
x = df.drop(["student_id", "placed", "salary_lpa", "degree_percentage"], axis=1)
y = df["placed"]

# Train Model
X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test) * 100

print("\n===== AI PLACEMENT PREDICTION SYSTEM =====")
print(f"Model Accuracy : {accuracy:.2f}%")

print("\nEnter Student Details")

age = int(input("Age: "))
ssc_percentage = float(input("SSC Percentage: "))
hsc_percentage = float(input("HSC Percentage: "))
cgpa = float(input("CGPA:"))
internships_count = int(input("Internships Count: "))
projects_count = int(input("Projects Count: "))
certifications_count = int(input("Certifications Count: "))
technical_skills_score = int(input("Technical Skills Score (0-100): "))
soft_skills_score = int(input("Soft Skills Score (0-100): "))
aptitude_score = int(input("Aptitude Score (0-100): "))
communication_score = int(input("Communication Score (0-100): "))
work_experience_months = int(input("Work Experience Months: "))
leadership_roles = int(input("Leadership Roles: "))
extracurricular_activities = int(input("Extracurricular Activities: "))
backlogs = int(input("Backlogs: "))

# Fixed Encoded Values
gender = 1
city_tier = 0
ssc_board = 0
hsc_board = 0
hsc_stream = 1
degree_field = 0
specialization = 0

student = [[
    gender,
    age,
    city_tier,
    ssc_percentage,
    ssc_board,
    hsc_percentage,
    hsc_board,
    hsc_stream,
    degree_field,
    cgpa,
    specialization,
    internships_count,
    projects_count,
    certifications_count,
    technical_skills_score,
    soft_skills_score,
    aptitude_score,
    communication_score,
    work_experience_months,
    leadership_roles,
    extracurricular_activities,
    backlogs
]]
print("Number of columns in x:", len(x.columns))
print("Number of values in student:", len(student[0]))
print(x.columns.tolist())
student_df = pd.DataFrame(student, columns=x.columns)

probability = model.predict_proba(student)[0][1]
placement_percentage = probability * 100

print("\n===== RESULT =====")
print(f"Placement Probability : {placement_percentage:.2f}%")

if placement_percentage >= 75:
    print("Prediction : PLACED")
elif placement_percentage >= 50:
    print("Prediction : MODERATE CHANCE")
else:
    print("Prediction : NOT PLACED")