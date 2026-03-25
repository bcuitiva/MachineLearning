import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression

# Cargar datos
data = pd.read_csv('ObesityDataSet_raw_and_data_sinthetic.csv')

# Separar variables
X = data.drop(['Weight', 'NObeyesdad'], axis=1)
y = data['Weight']

# Columnas categóricas
categorical_columns = X.select_dtypes(include=['object']).columns

# Preprocesamiento
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(drop='first'), categorical_columns)
    ],
    remainder='passthrough'
)

X_transformed = preprocessor.fit_transform(X)

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(
    X_transformed, y, test_size=0.2, random_state=42
)

# Entrenar modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Función para predecir
def predecir_peso(datos):
    input_df = pd.DataFrame([datos])
    input_transformed = preprocessor.transform(input_df)
    return model.predict(input_transformed)[0]

#Exportar variables para usar en Flask
y_pred = model.predict(X_test)

#Convertir a listas
actual_values = y_test.tolist()
predicted_values = y_pred.tolist()