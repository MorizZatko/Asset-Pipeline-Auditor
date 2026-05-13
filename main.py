"""Asset Pipeline Auditor.

This module validates a provided asset list as txt file to check status and weight.
Outputs a new DataFrame and two string lines with the results for status and weight.
"""

import pandas as pd
import numpy as np

from src.loader import load_raw_assets
from src.models import Asset
from src.models import MeshAsset
from src.models import TextureAsset
from src.models import AssetLibrary

raw_data = load_raw_assets('data/raw_assets.txt')
df = pd.DataFrame(raw_data)

my_lib = AssetLibrary()

# Basic loop to filter all validated assets by asset type
for index, row in df.iterrows():
    if row['Type'] == 'Mesh':
        mesh_obj = MeshAsset(row['Name'], "Mesh", row['Version'], row['Size'], row['Extra'])
        my_lib.add_asset(mesh_obj)
    elif row['Type'] == 'Texture':
        texture_obj = TextureAsset(row['Name'], "Texture", row['Version'], row['Size'], row['Extra'])
        my_lib.add_asset(texture_obj)
    else:
        obj = Asset(row['Name'], row['Type'], row['Version'], row['Size'])
        my_lib.add_asset(obj)

my_lib.run_health_check()

print("----------------")
for a in my_lib.assets:
    a.describe_asset()

report_data = []

# Basic loop for output
for a in my_lib.assets:
    asset_info = {
        "Name": a.name,
        "Type": a.asset_type,
        "Size_MB": a.size,
        "Status": a.status
    }
    report_data.append(asset_info)

df_report = pd.DataFrame(report_data)

# Total count of crtitical assets.
critical_assets = df_report[df_report['Status'] != 'ok']
total_critical = len(critical_assets)

# Total count of final assets.
final_assets = df_report[df_report['Status'] == 'ok']
total_final = len(final_assets)

print("-------------------")
print(f"Insgesamt kritische Daten: {total_critical}")
print(f"Insgesamt finale Daten: {total_final}")