#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Actividad 1 - Conceptos fundamentales de Python
Autora: Yaiza
Máster Bioinformática
"""

# --- IMPORTS ---
import os
from collections import Counter
import matplotlib
matplotlib.use('Agg')  # backend sin GUI, evita errores de Qt/Wayland
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# --- CONFIGURACIÓN DE LA CARPETA Y ARCHIVO PRINCIPAL DE RESULTADOS ---
results_dir = "./results"
os.makedirs(results_dir, exist_ok=True)
main_results_path = os.path.join(results_dir, "actividad1_results.txt")

with open(main_results_path, "w") as f:
    f.write("=== Resultados de la Actividad 1 - Bioinformática ===\n\n")

print(f" Carpeta 'results' creada y archivo principal '{main_results_path}' listo para guardar resultados")

# --- RUTAS DE ARCHIVOS ---
PDB_PATH = "/home/yaiza/Desktop/python_activity1_yai/1tup.pdb"
csv_path = "/home/yaiza/Desktop/python_activity1_yai/actividad.csv"
tsv_path = "/home/yaiza/Desktop/python_activity1_yai/ciudades.tsv"

# --- DICCIONARIO DE CONVERSIÓN 3 LETRAS -> 1 LETRA ---
three_to_one = {
    'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C',
    'GLN':'Q','GLU':'E','GLY':'G','HIS':'H','ILE':'I',
    'LEU':'L','LYS':'K','MET':'M','PHE':'F','PRO':'P',
    'SER':'S','THR':'T','TRP':'W','TYR':'Y','VAL':'V'
}

# --- 2.A: EXTRAER TITLE Y AUTHOR ---
if os.path.exists(PDB_PATH):
    with open(PDB_PATH, 'r') as file:
        title_lines = []
        author_lines = []
        for line in file:
            if line.startswith("TITLE"):
                title_lines.append(line.strip())
            elif line.startswith("AUTHOR"):
                author_lines.append(line.strip())
    title = " ".join(title_lines)
    author = " ".join(author_lines)

    print("\n--- RESULTADOS 2.A ---")
    print("TITLE:", title)
    print("AUTHOR:", author)

    with open(main_results_path, "a") as f:
        f.write("--- RESULTADOS 2.A ---\n")
        f.write(f"TITLE: {title}\n")
        f.write(f"AUTHOR: {author}\n\n")
else:
    print(f" No se encontró el archivo: {PDB_PATH}")

# --- 2.B: EXTRAER SECUENCIA DE AMINOÁCIDOS (SEQRES) ---
seqres_list = []
if os.path.exists(PDB_PATH):
    with open(PDB_PATH, 'r') as file:
        for line in file:
            if line.startswith("SEQRES"):
                residues = line[19:].split()
                for res in residues:
                    res = res.upper()
                    if res in three_to_one:
                        seqres_list.append(three_to_one[res])
    print("\n--- RESULTADOS 2.B ---")
    print(f"Total aminoácidos extraídos: {len(seqres_list)}")
    print("Primeros 50 aminoácidos:", "".join(seqres_list[:50]))

    with open(main_results_path, "a") as f:
        f.write("--- RESULTADOS 2.B ---\n")
        f.write(f"Total aminoácidos extraídos: {len(seqres_list)}\n")
        f.write("Primeros 50 aminoácidos: " + "".join(seqres_list[:50]) + "\n\n")

# --- 2.C: CONTAR AMINOÁCIDOS ---
aa_counts = Counter(seqres_list)
aa_counts_dict = dict(aa_counts)

print("\n--- RESULTADOS 2.C ---")
print("Conteo de aminoácidos (primeros 10):")
for i, (aa, count) in enumerate(aa_counts_dict.items()):
    if i < 10:
        print(f"{aa}: {count}")

with open(main_results_path, "a") as f:
    f.write("--- RESULTADOS 2.C ---\n")
    f.write("Conteo de aminoácidos:\n")
    for aa, count in aa_counts_dict.items():
        f.write(f"{aa}: {count}\n")
    f.write("\n")

# --- 2.D: GRÁFICO DE BARRAS Y GUARDADO ---
aa_list = list(aa_counts_dict.keys())
frequencies = list(aa_counts_dict.values())

fig_path = os.path.join(results_dir, "aa_frequencies.png")
plt.figure(figsize=(12,6))
sns.barplot(x=aa_list, y=frequencies, hue=aa_list, palette="hls", legend=False)
plt.title("Frecuencia de aminoácidos en la proteína P53 (1TUP)")
plt.xlabel("Aminoácido (una letra)")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.savefig(fig_path)
plt.close()
print(f" Gráfico guardado en {fig_path}")

with open(main_results_path, "a") as f:
    f.write(f"Gráfico de frecuencias de aminoácidos guardado en: {fig_path}\n\n")

# --- 3.A: LEER CSV Y TSV Y PREPARAR DATAFRAMES ---
df_actividad = pd.read_csv(csv_path, sep=';')
# Las columnas reales son: id, diet, pulse, time, kind
# Renombramos para usar nombres en español
df_actividad.columns = ['id', 'dieta', 'pulsaciones', 'tiempo', 'actividad']

df_ciudades = pd.read_csv(tsv_path, sep='\t')
# Las columnas son: id, city
# Renombramos para usar nombres en español
df_ciudades.columns = ['id', 'ciudad']

print("\n--- RESULTADOS 3.A ---")
print("Primeras 5 filas df_actividad:")
print(df_actividad.head())
print("\nPrimeras 5 filas df_ciudades:")
print(df_ciudades.head())

with open(main_results_path, "a") as f:
    f.write("--- RESULTADOS 3.A ---\n")
    f.write("Primeras 5 filas df_actividad:\n")
    f.write(df_actividad.head().to_string())
    f.write("\n\nPrimeras 5 filas df_ciudades:\n")
    f.write(df_ciudades.head().to_string())
    f.write("\n\n")

# --- 3.B: DETECTAR Y ELIMINAR FILAS CON VALORES VACÍOS ---

# Contar celdas vacías antes de eliminar
empty_actividad = df_actividad.isna().sum().sum()
empty_ciudades = df_ciudades.isna().sum().sum()

print("\n--- RESULTADOS 3.B ---")
print(f"Celdas vacías en df_actividad: {empty_actividad}")
print(f"Celdas vacías en df_ciudades: {empty_ciudades}")

with open(main_results_path, "a") as f:
    f.write("--- RESULTADOS 3.B ---\n")
    f.write(f"Celdas vacías en df_actividad: {empty_actividad}\n")
    f.write(f"Celdas vacías en df_ciudades: {empty_ciudades}\n\n")

# Eliminar filas con celdas vacías
df_actividad.dropna(inplace=True)
df_ciudades.dropna(inplace=True)

# Contar de nuevo para confirmar que ya no hay celdas vacías
empty_actividad_after = df_actividad.isna().sum().sum()
empty_ciudades_after = df_ciudades.isna().sum().sum()

print(f"Celdas vacías después de limpiar df_actividad: {empty_actividad_after}")
print(f"Celdas vacías después de limpiar df_ciudades: {empty_ciudades_after}")

with open(main_results_path, "a") as f:
    f.write(f"Celdas vacías después de limpiar df_actividad: {empty_actividad_after}\n")
    f.write(f"Celdas vacías después de limpiar df_ciudades: {empty_ciudades_after}\n\n")

# --- 3.C: CONTAR NIVELES EN LA COLUMNA 'dieta' Y SU FRECUENCIA ---

dieta_counts = df_actividad['dieta'].value_counts()

print("\n--- RESULTADOS 3.C ---")
print("Frecuencia de cada nivel de dieta:")
print(dieta_counts)

with open(main_results_path, "a") as f:
    f.write("--- RESULTADOS 3.C ---\n")
    f.write("Frecuencia de cada nivel de dieta:\n")
    f.write(dieta_counts.to_string())
    f.write("\n\n")

# --- 3.D: AGRUPAR POR NIVEL DE ACTIVIDAD ---

# Agrupamos por 'actividad'
grouped = df_actividad.groupby('actividad')

# Convertimos a lista para ver la estructura
grouped_list = list(grouped)

print("\n--- RESULTADOS 3.D ---")
print("Número de grupos creados:", len(grouped_list))
print("Tipos de actividad (primer elemento de cada grupo):")
for i, (actividad, group_df) in enumerate(grouped_list):
    print(f"Grupo {i+1}: {actividad}, número de filas: {len(group_df)}")

with open(main_results_path, "a") as f:
    f.write("--- RESULTADOS 3.D ---\n")
    f.write(f"Número de grupos creados: {len(grouped_list)}\n")
    f.write("Resumen de cada grupo:\n")
    for i, (actividad, group_df) in enumerate(grouped_list):
        f.write(f"Grupo {i+1}: {actividad}, número de filas: {len(group_df)}\n")
    f.write("\n")

# --- 3.E: FRECUENCIA CARDÍACA MEDIA Y DESVIACIÓN ESTÁNDAR POR ACTIVIDAD ---

# Calculamos media y desviación estándar usando agg
stats_by_activity = grouped.agg({
    'pulsaciones': ['mean', 'std']
})

print("\n--- RESULTADOS 3.E ---")
print(stats_by_activity)

with open(main_results_path, "a") as f:
    f.write("--- RESULTADOS 3.E ---\n")
    f.write("Frecuencia cardíaca media y desviación estándar por nivel de actividad:\n")
    f.write(stats_by_activity.to_string())
    f.write("\n\n")

# --- 3.F: AÑADIR INFORMACIÓN DE CIUDADES CON MERGE ---

# Merge de df_actividad con df_ciudades según la columna 'id'
df_completo = pd.merge(df_actividad, df_ciudades, on='id', how='left')

print("\n--- RESULTADOS 3.F ---")
print("Primeras 5 filas del DataFrame completo tras merge:")
print(df_completo.head())

with open(main_results_path, "a") as f:
    f.write("--- RESULTADOS 3.F ---\n")
    f.write("Primeras 5 filas del DataFrame completo tras merge:\n")
    f.write(df_completo.head().to_string())
    f.write("\n\n")

# --- 3.G: GRÁFICO MULTI-FACETADO DE PULSACIONES VS TIEMPO ---
g = sns.FacetGrid(df_completo, row='actividad', col='dieta', margin_titles=True, height=4)
g.map_dataframe(sns.scatterplot, x='tiempo', y='pulsaciones', alpha=0.7)
g.set_axis_labels("Tiempo (min)", "Pulsaciones (bpm)")
g.set_titles(row_template="{row_name}", col_template="{col_name}")
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle("Relación entre pulsaciones y tiempo según actividad y dieta", fontsize=16)

# Guardar la figura
fig_path2 = os.path.join(results_dir, "pulsaciones_vs_tiempo.png")
g.savefig(fig_path2)
plt.close()
print(f"✅ Gráfico guardado en {fig_path2}")

with open(main_results_path, "a") as f:
    f.write("--- RESULTADOS 3.G ---\n")
    f.write(f"Gráfico de pulsaciones vs tiempo según actividad y dieta guardado en: {fig_path2}\n\n")
