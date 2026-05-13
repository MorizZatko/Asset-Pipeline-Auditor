"""Function to read and validate raw data from text file."""

import pandas as pd
import numpy as np

def load_raw_assets(file_path):
    """Load function for txt file with length check.

    Read txt file, check length of asset and converts version, size and extra data to float.
    Exception handling by ValueError.
    
    Args:
        file_path (str): Path to asset text file.

    Returns:
        data (list): fill data with checked assets.
    """
    data = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            #print(f"DEBUG: Verarbeitete Zeile: '{line}'")
            if not line: continue

            elements = line.split(',')

            if len(elements) == 5:
                try:
                    data.append({
                        'Name': elements[0],
                        'Type': elements[1],
                        'Version': float(elements[2]),
                        'Size': float(elements[3]),
                        'Extra': float(elements[4])
                    })

                except ValueError:
                    print(f"Fehler beim umwandeln der Version oder Size in der Zeile: {line}")

            else:
                print(f"Ungültige Anzahl der Elemente in Zeile: {line}")
    return data