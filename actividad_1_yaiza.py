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
