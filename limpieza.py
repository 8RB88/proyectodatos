import pandas as pd
from fuzzywuzzy import process
from tqdm import tqdm

# Cargar con encabezado correcto
df = pd.read_excel("base-datos-abiertos_oferta-academica_05022025.xlsx", header=13)

# Limpiar y preparar columnas
df = df.dropna(subset=["NOMBRE_CARRERA"])
df["NOMBRE_CARRERA"] = df["NOMBRE_CARRERA"].str.upper().str.strip()
df["NOMBRE_IES"] = df["NOMBRE_IES"].str.upper().str.strip()
df["MODALIDAD"] = df["MODALIDAD"].str.upper().str.strip().replace("A DISTANCIA", "DISTANCIA")


# Crear ID único para cada carrera
df = df.reset_index(drop=True)
df["ID_CARRERA"] = df.index.map(lambda i: f"CAR{i:04}")

# Separar carreras UTPL y otras
df_utpl = df[df["NOMBRE_IES"] == "UNIVERSIDAD TECNICA PARTICULAR DE LOJA"]
df_otras = df[df["NOMBRE_IES"] != "UNIVERSIDAD TECNICA PARTICULAR DE LOJA"]

# Emparejamiento fuzzy con barra de progreso
resultados = []
for _, row in tqdm(df_otras.iterrows(), total=df_otras.shape[0], desc="Procesando carreras"):
    nombre_carrera = row["NOMBRE_CARRERA"]
    mejor_match = process.extractOne(nombre_carrera, df_utpl["NOMBRE_CARRERA"])

    if mejor_match:
        carrera_utpl = df_utpl[df_utpl["NOMBRE_CARRERA"] == mejor_match[0]].iloc[0]
        resultado = {
            "ID Carrera Origen": row["ID_CARRERA"],
            "Universidad Origen": row["NOMBRE_IES"],
            "Carrera Origen": nombre_carrera,
            "Provincia Origen": row["PROVINCIA"],
            "Modalidad Origen": row["MODALIDAD"],
            "Campo Amplio Origen": row["CAMPO_AMPLIO"],
            "ID Carrera UTPL": carrera_utpl["ID_CARRERA"],
            "Carrera Similar UTPL": mejor_match[0],
            "Provincia UTPL": carrera_utpl["PROVINCIA"],
            "Modalidad UTPL": carrera_utpl["MODALIDAD"],
            "Campo Amplio UTPL": carrera_utpl["CAMPO_AMPLIO"],
            "Score de Similaridad": mejor_match[1]
        }
        resultados.append(resultado)

# Guardar resultados
df_resultados = pd.DataFrame(resultados)
df_resultados.to_excel("emparejamientos_similares.xlsx", index=False)
print("Limpieza completa: emparejamientos_similares.xlsx generado.")
