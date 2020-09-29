import numpy as np
import pandas as pd

raw_lines_to_csv = []

with open("IJM400025.geo") as GeoFile:
    raw_lines = GeoFile.readlines()
    for line in raw_lines:
        if "Point " in line:
            raw_lines_to_csv.append(line.strip())


lines_to_csv = []
for line in raw_lines_to_csv:
    lines_to_csv.append(line.replace("Point ", ""))



with open("IJM400025.csv", "w") as CSVFile:
    for line in lines_to_csv:
        CSVFile.write(line + "\n")