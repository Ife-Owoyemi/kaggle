import pandas as pd
import os.path

def find_data_filename(filename):
    if os.path.isfile(filename):
        return filename
    # Check if the file for csv.gz
    elif os.path.isfile(filename+ ".gz"):
        return filename + ".gz"
    # Check if the file for csv.zip
    elif os.path.isfile(filename+ ".zip"):
        return filename + ".zip"
    else: 
        raise IOError, "Input file doesn't exist in uncompressed, gzip, or zip form."
