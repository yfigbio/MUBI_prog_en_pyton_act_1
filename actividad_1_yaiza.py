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

# --- PARTE 2.A: Examinar el archivo y extraer TITLE y AUTHOR ---

# Comprobamos que el archivo existe antes de intentar abrirlo
if os.path.exists(PDB_PATH):
    with open(PDB_PATH, 'r') as file: #abre el archivo y garantiza que se cierre automáticamente.
        #Recorre cada línea y busca si empieza con "TITLE" o "AUTHOR".
        title_lines = []
        author_lines = []

        for line in file:
            if line.startswith("TITLE"):
                title_lines.append(line.strip())
            elif line.startswith("AUTHOR"):
                author_lines.append(line.strip())

    # Unimos las líneas fragmentadas con join para formar cadenas completas.
    title = " ".join(title_lines)
    author = " ".join(author_lines)

    print("\n--- RESULTADOS 2.A ---")
    print("TITLE:", title)
    print("AUTHOR:", author)

else:
    print(f" No se encontró el archivo: {PDB_PATH}")

# --- PARTE 2.B: Extraer secuencia de aminoácidos (SEQRES) ---

# Mapa de tres letras a una letra (aminoácidos estándar)
three_to_one = {
    'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C',
    'GLN':'Q','GLU':'E','GLY':'G','HIS':'H','ILE':'I',
    'LEU':'L','LYS':'K','MET':'M','PHE':'F','PRO':'P',
    'SER':'S','THR':'T','TRP':'W','TYR':'Y','VAL':'V'
}

seqres_list = []  # lista donde guardaremos la secuencia

if os.path.exists(PDB_PATH):
    with open(PDB_PATH, 'r') as file:
        for line in file:
            if line.startswith("SEQRES"):
                # Extraemos los nombres de residuos (aprox desde columna 19 en adelante)
                residues = line[19:].split()
                for res in residues:
                    res = res.upper()
                    if res in three_to_one:
                        seqres_list.append(three_to_one[res])
                    # ignoramos residuos no estándar

    print("\n--- RESULTADOS 2.B ---")
    print(f"Total aminoácidos extraídos: {len(seqres_list)}")
    print("Primeros 50 aminoácidos:", "".join(seqres_list[:50]))

else:
    print(f"No se encontró el archivo: {PDB_PATH}")

# --- PARTE 2.C: Contar aminoácidos y guardar en diccionario ---

from collections import Counter

# Creamos un diccionario con el conteo de cada aminoácido
aa_counts = Counter(seqres_list)  # Counter devuelve un diccionario con clave=aminoácido y valor=frecuencia

# Convertimos a dict normal (opcional)
aa_counts_dict = dict(aa_counts)

print("\n--- RESULTADOS 2.C ---")
print("Conteo de aminoácidos (primeros 10):")
for i, (aa, count) in enumerate(aa_counts_dict.items()):
    if i < 10:  # mostramos solo los primeros 10 para no saturar
        print(f"{aa}: {count}")


