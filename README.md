Proyecto Final: Análisis de Patrones Climáticos en Ciudades
Este repositorio contiene mi proyecto final para el curso de "Fundamentos de Python para el Análisis de Datos". En este análisis se explora cómo varían las condiciones climáticas entre diferentes ciudades utilizando un dataset histórico.


1. Pregunta de Investigación:

¿Cómo varía la temperatura promedio entre las distintas ciudades y existe una relación directa entre el calor y la humedad?

El objetivo es identificar si la ubicación geográfica determina rangos de temperatura diferentes y cómo se comportan otras variables como la lluvia y la humedad en relación con el calor.


2. Preparación de Datos:

Para este análisis se utilizaron las siguientes librerías de Python:

Pandas: Para la carga y manipulación del dataset clima_ciudades.csv.
Matplotlib & Seaborn: Para la creación de gráficos.

El dataset contiene información diaria sobre temperaturas (máxima, mínima, promedio), humedad, precipitación y velocidad del viento para varias ciudades.


3. Limpieza de Datos:

Antes de analizar, se realizaron los siguientes pasos de limpieza para asegurar la calidad de los datos:

- Eliminación de duplicados: Se verificó y eliminó cualquier registro repetido.
- Manejo de valores nulos: Se eliminaron filas incompletas para evitar sesgos en los cálculos.

Conversión de tipos:
- La columna fecha se convirtió al formato datetime.


4. Análisis Descriptivo:

Se calcularon estadísticas clave para entender el contexto:
- Temperatura Promedio por Ciudad: Se identificó qué ciudades son más cálidas.
- Precipitación Total: Suma de lluvias para ver qué ciudad es más húmeda.
- Correlación: Se generó una matriz para ver cómo interactúan variables como temperatura y humedad.


5. Visualización:

Se generaron 3 gráficos para comunicar los hallazgos:
- Distribución de Temperatura (Boxplot): Para comparar los rangos y medianas de temperatura entre ciudades.
- Relación Temperatura vs Humedad (Scatterplot): Para visualizar si el calor está relacionado con ambientes más secos o húmedos.
- Tendencia Temporal (Lineplot): Para observar la evolución del clima a lo largo de las fechas registradas.


6. Interpretación y Conclusiones:

Hallazgos Principales:
- Diferencias Regionales: Existen variaciones significativas entre ciudades, algunas mantienen rangos de temperatura muy estables mientras que otras fluctúan más.
- Relación Inversa: Se observó una tendencia donde los días con mayor temperatura suelen tener menor humedad.
- Estacionalidad: Los patrones de temperatura siguen ciclos claros que afectan a todas las ciudades al mismo tiempo.

Pasos futuros:
- Análisis de un a mayor escala temporal y predicción: Se podrían recolectar datos históricos más antiguos para tener un modelo más robusto con el que poder hacer estadística inferencial para predicciones futuras del clima.
- Mayor cantidad de parámetros: Se podrían incluir datos de consumo eléctrico o enfermedades respiratorias/golpes de calor para evaluar el impacto del clima en la infraestructura y salud pública.


Proyecto realizado por Mizraim Moroyoqui Cárdenas - Diciembre 2025