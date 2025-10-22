from elasticsearch import Elasticsearch
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Conectarse a Elasticsearch con HTTPS y autenticación
es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", "NttvGEaD_q3qEOR9Szpk"),
    verify_certs=False  # Permite certificados auto-firmados
)

# Verificar conexión
if not es.ping():
    print("❌ No se pudo conectar a Elasticsearch con HTTPS y credenciales")
    exit()
else:
    print("✅ Conectado a Elasticsearch con HTTPS")

# Nombre del índice
index_name = "ligamx_2016_2022"

# Crear índice si no existe
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)
    print(f"✅ Índice '{index_name}' creado")
else:
    print(f"ℹ️ Índice '{index_name}' ya existe")

# Cargar dataset
df = pd.read_csv(r"C:\Users\Brian_ahg9dj5\Portafolio\data.csv")

# Mostrar columnas para confirmar
print("Columnas disponibles:", df.columns.tolist())

# Reemplazar NaN y valores no compatibles con JSON
df = df.replace({np.nan: None})
df = df.astype(object)

# Subir datos a Elasticsearch (si el ID ya existe, actualiza el documento)
for i, row in df.iterrows():
    es.index(index=index_name, id=i, document=row.to_dict())

count = es.count(index=index_name)["count"]
print(f"✅ Se subieron {count} registros a Elasticsearch")

# Graficar ejemplo: partidos ganados como local vs visitante
if "home_win" in df.columns and "away_win" in df.columns:
    home_wins = df["home_win"].sum()
    away_wins = df["away_win"].sum()

    plt.bar(["Local", "Visitante"], [home_wins, away_wins], color=["blue", "orange"])
    plt.title("Partidos ganados como Local vs Visitante (Liga MX 2016–2022)")
    plt.xlabel("Condición")
    plt.ylabel("Cantidad de partidos")
    plt.tight_layout()
    plt.savefig("grafico.png")

    print("✅ Gráfico guardado como 'grafico.png'")
else:
    print("⚠️ Las columnas 'home_win' y 'away_win' no existen en el dataset.")
