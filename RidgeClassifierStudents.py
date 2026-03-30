import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import RidgeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_curve, roc_auc_score
import json

# --- Entrenamiento al arrancar la app ---
df = pd.read_csv("Predict_students_dropout.csv")
df.columns = df.columns.str.strip()
df['Target'] = df['Target'].map({'Dropout': 0, 'Graduate': 1, 'Enrolled': 1})

X = df[[
    'Age at enrollment',
    'Curricular units 1st sem (approved)',
    'Curricular units 2nd sem (approved)',
    'Curricular units 1st sem (grade)',
    'Curricular units 2nd sem (grade)'
]]
y = df['Target']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = RidgeClassifier(alpha=1.0)
model.fit(X_train, y_train)

# Calcular ROC con datos reales del test set
decision = model.decision_function(X_test)
fpr_vals, tpr_vals, _ = roc_curve(y_test, decision)
auc_val = roc_auc_score(y_test, decision)

# Convertir a listas para pasar al template
roc_points = json.dumps([
    {"x": round(float(f), 4), "y": round(float(t), 4)}
    for f, t in zip(fpr_vals, tpr_vals)
])

def predict_student(data):
    data_scaled = scaler.transform([data])
    return model.predict(data_scaled)[0]