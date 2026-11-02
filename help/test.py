# Kommentar für anfang

import pandas as pd
import ifcopenshell

print("Hello World")
ifc_file_path = r"C:\Users\MichalRontsinsky\OneDrive - beyondBIM\Dokumente\VS_Projects\preprocessor\data\125_S1_01_LAN_MO_FAM.ifc"

ifc_file = ifcopenshell.open(ifc_file_path)
print(ifc_file)
print("opened")
