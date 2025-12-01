# 🌤️ Proyecto Final: Análisis de Patrones Climáticos en Ciudades

**Curso:** Fundamentos de Python para el Análisis de Datos  
**Autor:** Mizraim Moroyoqui Cárdenas  
**Fecha:** Diciembre 2025

---

## ❓ Pregunta de Investigación

> **¿Cómo varía la temperatura promedio entre las distintas ciudades y existe una relación directa entre el calor y la humedad?**

El objetivo es identificar si la ubicación geográfica determina rangos de temperatura diferentes y cómo se comportan variables como lluvia y humedad respecto al calor.

---

## 📦 Preparación de Datos

**Librerías utilizadas:**

- `pandas` → Carga y manipulación del dataset `clima_ciudades.csv`
- `matplotlib`, `seaborn` → Visualización de datos

**Descripción del dataset:**

| Columna         | Descripción                                           |
|-----------------|------------------------------------------------------|
| fecha           | Fecha en formato año-mes-día                         |
| ciudad          | Nombre de la ciudad                                  |
| temp_max        | Temperatura máxima diaria                            |
| temp_min        | Temperatura mínima diaria                            |
| temp_promedio   | Temperatura promedio diaria                          |
| humedad         | Humedad (%)                                          |
| precipitación   | Precipitación (mm)                                   |
| viento          | Velocidad del viento (km/h)                          |

---

## 🧹 Limpieza de Datos

**Pasos realizados:**
- Eliminación de duplicados
- Manejo de valores nulos (eliminación de filas incompletas)
- Conversión de la columna `fecha` a formato `datetime`

---

## 📊 Análisis Descriptivo

- **Temperatura Promedio por Ciudad:** Identificación de ciudades más cálidas.
- **Precipitación Total:** Ciudad más húmeda por suma anual/mensual.
- **Correlación entre variables:** Matriz para observar interacción entre temperatura, humedad, precipitación.

---

## 📈 Visualizaciones

1. **Distribución de Temperaturas**  
   _Boxplot para comparar rangos y medianas entre ciudades_

   ![Ejemplo Boxplot](ruta/boxplot.png)

2. **Relación Temperatura vs Humedad**  
   _Scatterplot para visualizar si el calor está relacionado con ambientes más secos o húmedos_

   ![Ejemplo Scatterplot](ruta/scatterplot.png)

3. **Tendencia Temporal**  
   _Lineplot para observar la evolución del clima por ciudad_

   ![Ejemplo Lineplot](ruta/lineplot.png)

---

## 💡 Interpretación y Conclusiones

**Hallazgos principales:**
- 🌎 **Diferencias Regionales:** Variaciones significativas entre ciudades; algunas con rangos estables, otras con alta fluctuación.
- 🔄 **Relación Inversa:** Los días más cálidos suelen tener menor humedad.
- 📅 **Estacionalidad:** Ciclos claros de temperatura afectan a todas las ciudades.

**Pasos futuros:**
- Análisis temporal extendido y predicciones con modelos robustos
- Incorporación de más variables (consumo eléctrico, datos de salud pública)

---

> Proyecto realizado por **Mizraim Moroyoqui Cárdenas**  
> _Diciembre 2025_
