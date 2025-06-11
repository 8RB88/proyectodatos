
# 🧹 Proyecto de Limpieza y Emparejamiento de Carreras Universitarias

Este proyecto realiza limpieza, estandarización y análisis de datos sobre la oferta académica en Ecuador, con especial enfoque en emparejar carreras ofrecidas por otras universidades con las de la **Universidad Técnica Particular de Loja (UTPL)** usando coincidencia difusa (*fuzzy matching*).

---

## 📁 Estructura del Proyecto

```
├── limpieza.py                      # Script principal de procesamiento
├── requirements.txt                 # Dependencias del entorno
├── base-datos-abiertos_0502...     # Dataset bruto descargado (fuente SENESCYT)
├── emparejamientos_similares.xlsx  # Resultados generados
├── README.md                        # Este archivo
```

---

## 📦 Instalación

Asegúrate de tener Python 3.6+ instalado. Luego, instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecución

Ejecuta el script principal:

```bash
python limpieza.py
```

Este script realiza:

- ✅ Limpieza y estandarización de columnas clave  
- ✅ Separación entre carreras UTPL y otras IES  
- ✅ Emparejamiento de carreras similares usando FuzzyWuzzy  
- ✅ Exportación a un archivo Excel (`emparejamientos_similares.xlsx`)

---

## 📚 Requisitos del Script

Listado en `requirements.txt`:

```
pandas
openpyxl
fuzzywuzzy
python-Levenshtein
tqdm
```


