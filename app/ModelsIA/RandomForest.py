import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os


# Guardamos encoders globalmente
encoders = {}

def entrenar_modelo(ruta_csv):

    df = pd.read_csv(ruta_csv, sep=";")
    df = df.drop(columns=["name", "lastname", "student_code"])

    for col in ["gender", "nationality", "marital_status", "who_pays"]:

        le = LabelEncoder()

        df[col] = le.fit_transform(df[col])

        encoders[col] = le

    X = df.drop("dropout", axis=1)

    y = df["dropout"]


    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    # Guardar modelo y encoders

    joblib.dump(model, "modelo.pkl")

    joblib.dump(encoders, "encoders.pkl")



    return model


def cargar_modelo():

    model = joblib.load("modelo.pkl")
    encoders = joblib.load("encoders.pkl")

    return model, encoders





def predecir_estudiante(data: dict):
    if not os.path.exists("modelo.pkl"):
        print("⚠️ Modelo no encontrado. Entrenando...")
        entrenar_modelo("estudiantes.csv")

    model, encoders = cargar_modelo()

    df = pd.DataFrame([data])



    # Aplicar encoding

    for col in ["gender", "nationality", "marital_status", "who_pays"]:

        df[col] = encoders[col].transform(df[col])

    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]

    return {

        "prediccion": int(pred),

        "probabilidad_desercion": float(prob)

    }

