import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Asegurarse de que la carpeta 'docs' exista
os.makedirs("docs", exist_ok=True)

# Cargar dataset desde la raíz del repositorio
df = pd.read_csv("data.csv")

# Mostrar columnas para confirmar
print("Columnas disponibles:", df.columns.tolist())

# Reemplazar NaN con None (opcional, útil si quieres procesar JSON)
df = df.replace({np.nan: None})

# Graficar ejemplo: partidos ganados como local vs visitante
if "home_win" in df.columns and "away_win" in df.columns:
    home_wins = df["home_win"].sum()
    away_wins = df["away_win"].sum()

    plt.bar(["Local", "Visitante"], [home_wins, away_wins], color=["blue", "orange"])
    plt.title("Partidos ganados como Local vs Visitante (Liga MX 2016–2022)")
    plt.xlabel("Condición")
    plt.ylabel("Cantidad de partidos")
    plt.tight_layout()

    # Guardar gráfico en la carpeta docs
    plt.savefig("docs/grafico.png")
    print("✅ Gráfico guardado como 'docs/grafico.png'")
else:
    print("⚠️ Las columnas 'home_win' y 'away_win' no existen en el dataset.")
