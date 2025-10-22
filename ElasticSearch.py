import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os
from elasticsearch import Elasticsearch
import numpy as np

def main():
    print("Iniciando proceso de carga y visualización...")
    
    # 1. Cargar datos desde CSV
    df = pd.read_csv('data.csv')
    print(f"Datos cargados: {len(df)} registros")
    
    # 2. Conexión a Elasticsearch
    es = connect_elasticsearch()
    
    if es:
        # 3. Cargar datos a Elasticsearch
        load_to_elasticsearch(es, df)
        
        # 4. Generar visualizaciones
        generate_charts(df)
        
        # 5. Generar página HTML
        generate_html()
        
        print("Proceso completado exitosamente!")
    else:
        print("Error: No se pudo conectar a Elasticsearch")

def connect_elasticsearch():
    """Conectar a Elasticsearch usando variables de entorno"""
    try:
        es_cloud_id = os.getenv('ELASTIC_CLOUD_ID')
        es_username = os.getenv('ELASTIC_USERNAME')
        es_password = os.getenv('ELASTIC_PASSWORD')
        
        if es_cloud_id and es_username and es_password:
            es = Elasticsearch(
                cloud_id=es_cloud_id,
                http_auth=(es_username, es_password)
            )
        else:
            # Para desarrollo local o sin Elasticsearch
            print("Usando modo sin Elasticsearch (solo visualizaciones)")
            return None
        
        if es.ping():
            print("✅ Conectado a Elasticsearch")
            return es
        else:
            print("❌ No se pudo conectar a Elasticsearch")
            return None
            
    except Exception as e:
        print(f"❌ Error conectando a Elasticsearch: {e}")
        return None

def load_to_elasticsearch(es, df):
    """Cargar datos a Elasticsearch"""
    try:
        index_name = "dataset"
        
        # Crear índice si no existe
        if not es.indices.exists(index=index_name):
            # Mapeo dinámico basado en tipos de datos
            mapping = {
                "mappings": {
                    "properties": {
                        # Elasticsearch inferirá los tipos automáticamente
                    }
                }
            }
            es.indices.create(index=index_name, body=mapping)
        
        # Convertir DataFrame a documentos
        records = df.to_dict('records')
        
        # Indexar documentos
        for i, record in enumerate(records):
            es.index(index=index_name, id=i+1, body=record)
        
        print(f"✅ Datos cargados en Elasticsearch (índice: {index_name})")
        
    except Exception as e:
        print(f"❌ Error cargando datos a Elasticsearch: {e}")

def generate_charts(df):
    """Generar gráficos y guardarlos en la carpeta docs"""
    
    # Configurar estilo
    plt.style.use('default')
    sns.set_palette("husl")
    
    # Crear carpeta docs si no existe
    os.makedirs('docs', exist_ok=True)
    
    # Gráfico 1: Distribución de columnas numéricas
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    if len(numeric_cols) > 0:
        fig, axes = plt.subplots(1, min(3, len(numeric_cols)), figsize=(15, 5))
        if len(numeric_cols) == 1:
            axes = [axes]
        
        for i, col in enumerate(numeric_cols[:3]):
            df[col].hist(ax=axes[i], bins=15, alpha=0.7)
            axes[i].set_title(f'Distribución de {col}')
            axes[i].set_xlabel(col)
            axes[i].set_ylabel('Frecuencia')
        
        plt.tight_layout()
        plt.savefig('docs/distribucion_numerica.png', dpi=100, bbox_inches='tight')
        plt.close()
    
    # Gráfico 2: Top categorías (columnas categóricas)
    categorical_cols = df.select_dtypes(include=['object']).columns
    
    if len(categorical_cols) > 0:
        for col in categorical_cols[:2]:  # Máximo 2 columnas categóricas
            top_categories = df[col].value_counts().head(10)
            
            plt.figure(figsize=(10, 6))
            top_categories.plot(kind='bar')
            plt.title(f'Top 10 - {col}')
            plt.xlabel(col)
            plt.ylabel('Cantidad')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(f'docs/top_{col.lower()}.png', dpi=100, bbox_inches='tight')
            plt.close()
    
    # Gráfico 3: Correlación entre variables numéricas
    if len(numeric_cols) > 1:
        plt.figure(figsize=(8, 6))
        correlation_matrix = df[numeric_cols].corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
        plt.title('Matriz de Correlación')
        plt.tight_layout()
        plt.savefig('docs/correlacion.png', dpi=100, bbox_inches='tight')
        plt.close()
    
    print("✅ Gráficos generados en carpeta docs/")

def generate_html():
    """Generar página HTML principal"""
    
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Visualización de Dataset</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .header {
                text-align: center;
                background: white;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 20px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
            .chart-container {
                background: white;
                padding: 20px;
                margin: 15px 0;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
            .chart-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
                gap: 20px;
            }
            .chart-item {
                text-align: center;
            }
            .chart-item img {
                max-width: 100%;
                height: auto;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
            .last-update {
                text-align: center;
                color: #666;
                font-style: italic;
                margin-top: 30px;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>📊 Visualización de Dataset</h1>
            <p>Análisis automático generado con Python y GitHub Actions</p>
        </div>
        
        <div class="chart-container">
            <h2>📈 Gráficos Generados</h2>
            <div class="chart-grid">
    """
    
    # Agregar imágenes de gráficos
    image_files = [f for f in os.listdir('docs') if f.endswith('.png')]
    
    for img_file in image_files:
        html_content += f"""
                <div class="chart-item">
                    <h3>{img_file.replace('.png', '').replace('_', ' ').title()}</h3>
                    <img src="{img_file}" alt="{img_file}">
                </div>
        """
    
    html_content += f"""
            </div>
        </div>
        
        <div class="last-update">
            <p>Última actualización: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p>Generado automáticamente con GitHub Actions</p>
        </div>
    </body>
    </html>
    """
    
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ Página HTML generada: docs/index.html")

if __name__ == "__main__":
    main()