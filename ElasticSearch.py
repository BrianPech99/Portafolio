from elasticsearch import Elasticsearch
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

# Conectarse a Elasticsearch del runner de GitHub Actions
es = Elasticsearch("http://localhost:9200")  # HTTP y sin seguridad

# Esperar un poco para que Elasticsearch esté listo
time.sleep(10)

if not es.ping():
    print("❌ No se pudo conectar a Elasticsearch")
    exit()
else:
    print("✅ Conectado a Elasticsearch")

# Nombre del índice
index_name = "ligamx_2016_2022"

# Crear índice si no existe
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)
    print(f"✅ Índice '{index_name}' creado")
else:
    print(f"ℹ️ Índice '{index_name}' ya existe")

# Cargar dataset
df = pd.read_csv("data.csv")  # data.csv debe estar en la raíz del repositorio

# Reemplazar NaN y valores no compatibles con JSON
df = df.replace({np.nan: None})
df = df.astype(object)

# Subir datos a Elasticsearch
for i, row in df.iterrows():
    es.index(index=index_name, id=i, document=row.to_dict())

print(f"✅ Se subieron {len(df)} registros a Elasticsearch")

# Graficar
if "home_win" in df.columns and "away_win" in df.columns:
    home_wins = df["home_win"].sum()
    away_wins = df["away_win"].sum()

    plt.bar(["Local", "Visitante"], [home_wins, away_wins], color=["blue", "orange"])
    plt.title("Partidos ganados como Local vs Visitante (Liga MX 2016–2022)")
    plt.xlabel("Condición")
    plt.ylabel("Cantidad de partidos")
    plt.tight_layout()
    plt.savefig("docs/grafico.png")  # guardar dentro de docs para GitHub Pages
    print("✅ Gráfico guardado en docs/grafico.png")
