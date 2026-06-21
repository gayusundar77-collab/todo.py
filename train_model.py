import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("placement.csv")

df.columns = df.columns.str.strip()

# Convert categorical columns
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
    df[col] = df[col].astype("category").cat.codes

# Features & Target
X = df.drop(["student_id", "placed", "salary_lpa"], axis=1)
y = df["placed"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

print("\n===== MODEL TRAINING COMPLETE =====")
print(f"Accuracy : {accuracy*100:.2f}%")

import pickle
pickle.dump(model, open("placement_model.pkl","wb"))
print("model saved succesfully")