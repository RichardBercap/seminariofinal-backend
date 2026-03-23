import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

def crear_modelo(ruta_csv):
    # Cargar datos
    df = pd.read_csv(ruta_csv, sep=";")

    # Eliminar columnas que no aportan
    df = df.drop(columns=["name", "lastname", "student_code"])

    # Crear diccionario de encoders
    encoders = {}

    # Columnas categóricas
    columnas_cat = ["gender", "nationality", "marital_status", "who_pays"]

    for col in columnas_cat:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le

    # Separar variables
    X = df.drop("dropout", axis=1)
    y = df["dropout"]

    # Crear modelo
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # Entrenar
    model.fit(X, y)

    # Guardar modelo y encoders
    joblib.dump(model, "modelo.pkl")
    joblib.dump(encoders, "encoders.pkl")

    print("✅ Modelo guardado como modelo.pkl")
    print("✅ Encoders guardados como encoders.pkl")


# Ejecutar entrenamiento
if __name__ == "__main__":
    crear_modelo("estudiantes.csv")