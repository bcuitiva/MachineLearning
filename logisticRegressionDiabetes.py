import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, roc_curve, auc

# Data loading
data = pd.read_csv('diabetes.csv')

print(data.head())
print(data.info())
print(data.describe())

# Data preparation
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Division
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Predictions
y_pred = model.predict(X_test_scaled)

# Metrics
print(classification_report(y_test, y_pred))

accuracy = accuracy_score(y_test, y_pred)
print(f'Exactitud del modelo: {accuracy * 100:.2f}%')

# Prediction function
def predecir_diabetes(pregnancies, glucose, bloodpressure, skinthickness,
                      insulin, bmi, dpf, age):

    nuevo_paciente = np.array([[pregnancies, glucose, bloodpressure,
                                skinthickness, insulin, bmi, dpf, age]])

    nuevo_paciente_scaled = scaler.transform(nuevo_paciente)

    prediccion = model.predict(nuevo_paciente_scaled)[0]
    probabilidad = model.predict_proba(nuevo_paciente_scaled)[0][1]

    return prediccion, probabilidad