# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 02:45:48 2025

@author: Matias
"""

import json

field_mapping = {
    "código_usuario": "user_id",
    "nombre": "name",
    "dirección": "address",
    "teléfono": "phone",
    "correo_electrónico": "email",
    "fecha_de_alquiler": "rental_date",
    "fecha_de_entrega": "return_date",
    "nombre_de_la_película_video": "video_title",
    "formato": "format"
}

input_file = "dbJson_modificado.json"
output_file = "dbJson_english.json"

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

renamed_data = []
for item in data:
    new_item = {field_mapping.get(k, k): v for k, v in item.items()}
    renamed_data.append(new_item)


with open(output_file, "w", encoding="utf-8") as f:
    json.dump(renamed_data, f, indent=4, ensure_ascii=False)

print("JSON renombrado y guardado como dbJson_english.json")