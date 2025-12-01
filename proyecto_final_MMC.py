"""
PROYECTO FINAL: Análisis de Patrones Climáticos en Ciudades
=============================================================================
Autor: Mizraim Moroyoqui Cárdenas
Fecha: 01/12/2025
Pregunta de investigación: ¿Cómo varía la temperatura promedio entre las distintas
ciudades y existe una relación directa entre el calor y la humedad?
=============================================================================
"""

# 1. IMPORTACIONES
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2. CARGA DE DATOS
print("CARGA DE DATOS")
try:
    # Asegurar que el archivo csv esté en la misma carpeta que este script
    df = pd.read_csv('clima_ciudades.csv')
    print("Dataset 'clima_ciudades.csv' cargado correctamente.")
except FileNotFoundError:
    print("ERROR: No se encontró el archivo 'clima_ciudades.csv'.")

# 3. EXPLORACIÓN INICIAL
print("\nEXPLORACIÓN INICIAL")
# Ver primeras filas para entender estructura
print("Primeras 5 filas:")
print(df.head())

# Información general de columnas y tipos datos
print("\nInformación del Dataset:")
print(df.info())

# Estadísticas básicas
print("\nEstadísticas Descriptivas:")
print(df.describe())

# 4. LIMPIEZA DE DATOS
print("\nLIMPIEZA DE DATOS")

# Eliminar duplicados
duplicados = df.duplicated().sum()
print(f"Duplicados encontrados: {duplicados}")
if duplicados > 0:
    df = df.drop_duplicates()
    print("Duplicados eliminados.")

# Valores nulos
nulos = df.isnull().sum().sum()
print(f"Valores nulos encontrados: {nulos}")
# Eliminar filas con nulos para no afectar análisis
df = df.dropna()
print("Filas con valores nulos eliminadas.")

# Conversión de tipos de datos
# Convertir fecha a datetime para poder graficar tiempo
df['fecha'] = pd.to_datetime(df['fecha'])
print("\nDataset listo para análisis:")

# 5. ANÁLISIS DESCRIPTIVO
print("\nANÁLISIS DESCRIPTIVO")

# Temperatura promedio por ciudad
temp_ciudad = df.groupby('ciudad', observed=True)['temperatura_promedio'].mean().sort_values(ascending=False)
print("\nTemperatura Promedio por Ciudad (°C):")
print(temp_ciudad)

# Ciudad con más lluvia acumulada
lluvia_total = df.groupby('ciudad', observed=True)['precipitacion_mm'].sum().sort_values(ascending=False)
print("\nPrecipitación Total Acumulada (mm):")
print(lluvia_total.head(3))

# Matriz de correlación
cols_numericas = ['temperatura_promedio', 'humedad', 'precipitacion_mm', 'velocidad_viento_kmh']
correlacion = df[cols_numericas].corr()
print("\nCorrelación Temperatura vs Humedad:")
print(f"{correlacion.loc['temperatura_promedio', 'humedad']:.2f}")

# 6. VISUALIZACIONES
print("\nGENERANDO VISUALIZACIONES")

# GRAFICO 1: Distribución de Temperatura (Boxplot)
# Muestra rangos, mediana y valores atípicos de cada ciudad
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='ciudad', y='temperatura_promedio')
plt.title('Distribución de Temperaturas Promedio por Ciudad')
plt.xlabel('Ciudad')
plt.ylabel('Temperatura (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico1_cajas_temperatura.png', dpi=300)
print("grafico1_cajas_temperatura.png guardado.")
plt.close()

# GRAFICO 2: Relación Temperatura vs Humedad (Scatterplot)
# Responde a segunda parte de pregunta de investigación
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='temperatura_promedio', y='humedad', hue='ciudad', alpha=0.7)
plt.title('Relación entre Temperatura y Humedad')
plt.xlabel('Temperatura Promedio (°C)')
plt.ylabel('Humedad (%)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('grafico2_dispersion_humedad.png', dpi=300)
print("grafico2_dispersion_humedad.png guardado.")
plt.close()

# GRAFICO 3: Evolución Temporal (Lineplot)
# Muestra cambio del clima a lo largo del tiempo
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='fecha', y='temperatura_promedio', hue='ciudad')
plt.title('Tendencia de Temperatura en el Tiempo')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico3_tendencia_temporal.png', dpi=300)
print("grafico3_tendencia_temporal.png guardado.")
plt.close()