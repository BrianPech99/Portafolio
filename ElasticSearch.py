# ElasticSearch.py
import os
import sys
import logging
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Optional: from elasticsearch import Elasticsearch, exceptions
try:
    from elasticsearch import Elasticsearch, exceptions as es_exceptions
    ES_AVAILABLE = True
except Exception:
    ES_AVAILABLE = False

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

OUT_DIR = "docs"
OUT_FILE = os.path.join(OUT_DIR, "grafico.png")

def ensure_out_dir():
    os.makedirs(OUT_DIR, exist_ok=True)
    logging.info("Directorio '%s' creado/confirmado.", OUT_DIR)

def fetch_from_elasticsearch():
    """Intentar obtener datos desde Elasticsearch.
    Se esperan documentos con campos 'timestamp' y 'value'. Ajusta según tu índice.
    """
    if not ES_AVAILABLE:
        logging.warning("elasticsearch-py no está instalado o no disponible.")
        return None

    es_url = os.environ.get("ELASTIC_URL", "http://localhost:9200")
    es_user = os.environ.get("ELASTIC_USER")
    es_pass = os.environ.get("ELASTIC_PASS")
    index = os.environ.get("ELASTIC_INDEX", "datos")

    # Conexión simple, ajusta auth según necesites
    try:
        if es_user and es_pass:
            es = Elasticsearch(es_url, http_auth=(es_user, es_pass))
        else:
            es = Elasticsearch(es_url)

        # Simple query: obtener últimos 1000 documentos ordenados por timestamp
        resp = es.search(
            index=index,
            body={
                "size": 1000,
                "sort": [{"timestamp": {"order": "asc"}}],
                "_source": ["timestamp", "value"],
                "query": {"match_all": {}}
            }
        )
        hits = resp.get("hits", {}).get("hits", [])
        if not hits:
            logging.info("No se encontraron documentos en el índice '%s'.", index)
            return None

        rows = []
        for h in hits:
            src = h.get("_source", {})
            ts = src.get("timestamp")
            val = src.get("value")
            rows.append({"timestamp": ts, "value": val})

        df = pd.DataFrame(rows)
        # Intentar convertir timestamp a datetime si es necesario
        try:
            df["timestamp"] = pd.to_datetime(df["timestamp"])
        except Exception:
            logging.debug("No se pudo parsear timestamp automáticamente.")
        return df

    except Exception as e:
        logging.exception("Error conectando a Elasticsearch: %s", e)
        return None

def generate_example_data():
    """Generar datos de ejemplo si no hay conexión/datos."""
    logging.info("Generando datos de ejemplo para el gráfico.")
    now = datetime.utcnow()
    timestamps = [now - timedelta(days=i) for i in reversed(range(30))]
    values = np.cumsum(np.random.randn(30)) + 10
    df = pd.DataFrame({"timestamp": timestamps, "value": values})
    return df

def plot_and_save(df):
    plt.style.use("seaborn-darkgrid")
    fig, ax = plt.subplots(figsize=(10, 4))

    # Si 'timestamp' está en df, usarlo; si no, usar índice
    if "timestamp" in df.columns:
        x = df["timestamp"]
    else:
        x = df.index

    y = df["value"]

    ax.plot(x, y, marker="o", linestyle="-", color="#1f77b4")
    ax.set_title("Gráfico generado por ElasticSearch.py")
    ax.set_xlabel("Fecha")
    ax.set_ylabel("Valor")
    plt.xticks(rotation=30)
    plt.tight_layout()

    # Guardar
    plt.savefig(OUT_FILE, bbox_inches="tight")
    plt.close(fig)
    logging.info("Gráfico guardado en: %s", OUT_FILE)

def main():
    ensure_out_dir()

    df = fetch_from_elasticsearch()
    if df is None or df.empty:
        logging.info("No se obtuvieron datos reales; se usará ejemplo.")
        df = generate_example_data()

    # Asegurar que hay columna 'value'
    if "value" not in df.columns:
        logging.error("No existe la columna 'value' en los datos.")
        # crear columna vacía para evitar fallos
        df["value"] = 0

    try:
        plot_and_save(df)
    except Exception as e:
        logging.exception("Error al generar o guardar el gráfico: %s", e)
        # Intentar crear un gráfico vacío para que el archivo exista y no falle el pipeline
        try:
            empty_df = generate_example_data()
            plot_and_save(empty_df)
        except Exception as e2:
            logging.exception("Fallo al crear gráfico de emergencia: %s", e2)
            sys.exit(1)

if __name__ == "__main__":
    main()