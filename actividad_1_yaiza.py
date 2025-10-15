#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Actividad 1 - Conceptos fundamentales de Python
Autora: Yaiza
Máster Bioinformática
"""

# --- IMPORTS ---
# (en esta primera parte aún no hacen falta librerías externas)
import os

# --- RUTAS DE ARCHIVOS ---
PDB_PATH = "/home/yaiza/Desktop/python_activity1_yai/1tup.pdb"

# Carpeta de resultados
results_dir = "./results"
os.makedirs(results_dir, exist_ok=True)

# Archivo principal de resultados
main_results_path = os.path.join(results_dir, "actividad1_results.txt")
# Abrimos en modo escritura 'w' para iniciar limpio
with open(main_results_path, "w") as f:
    f.write("=== Resultados de la Actividad 1 - Bioinformática ===\n\n")

print(f"Carpeta 'results' creada y archivo principal '{main_results_path}' listo para guardar resultados")

# --- SECCIÓN 2: MANIPULACIÓN DE ARCHIVOS DE TEXTO PLANO (PDB) ---

import os
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

# --- RUTA DEL ARCHIVO PDB ---
PDB_PATH = "/home/yaiza/Desktop/python_activity1_yai/1tup.pdb"

# --- DICCIONARIO DE CONVERSIÓN 3 LETRAS -> 1 LETRA ---
three_to_one = {
    'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C',
    'GLN':'Q','GLU':'E','GLY':'G','HIS':'H','ILE':'I',
    'LEU':'L','LYS':'K','MET':'M','PHE':'F','PRO':'P',
    'SER':'S','THR':'T','TRP':'W','TYR':'Y','VAL':'V'
}

# --- CARPETA Y ARCHIVO PRINCIPAL DE RESULTADOS ---
results_dir = "./results"
os.makedirs(results_dir, exist_ok=True)
main_results_path = os.path.join(results_dir, "actividad1_results.txt")
with open(main_results_path, "w") as f:
    f.write("=== Resultados de la Actividad 1 - Bioinformática ===\n\n")
print(f" Carpeta 'results' creada y archivo principal '{main_results_path}' listo para guardar resultados")

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
colors = sns.color_palette("hls", len(aa_list))

# Guardar gráfico
fig_path = os.path.join(results_dir, "aa_frequencies.png")
plt.figure(figsize=(12,6))
sns.barplot(x=aa_list, y=frequencies, palette=colors)
plt.title("Frecuencia de aminoácidos en la proteína P53 (1TUP)")
plt.xlabel("Aminoácido (una letra)")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.savefig(fig_path)
plt.close()
print(f" Gráfico guardado en {fig_path}")

with open(main_results_path, "a") as f:
    f.write(f"Gráfico de frecuencias de aminoácidos guardado en: {fig_path}\n\n")
