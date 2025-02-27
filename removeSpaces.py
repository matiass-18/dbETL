# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 02:36:39 2025

@author: Matias
"""

import json

ruta_json = "input route"

with open(ruta_json, "r", encoding="utf-8") as f:
    datos = json.load(f)

def limpiar_clave(clave):
    return clave.lower().replace(" ", "_").replace("/", "_").replace("\\", "_")

datos_modificados = [{limpiar_clave(k): v for k, v in doc.items()} for doc in datos]

ruta_salida = "output route/dbJson_modificado.json"
with open(ruta_salida, "w", encoding="utf-8") as f:
    json.dump(datos_modificados, f, indent=4, ensure_ascii=False)

print(f"Archivo modificado guardado en: {ruta_salida}")
