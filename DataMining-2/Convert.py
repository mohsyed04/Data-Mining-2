# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 17:57:37 2019

@author: Syed Mohiuddin
"""

import csv

with open("water-treatment.data", 'r') as file:
    line_array = file.read().splitlines()
    cell_array = [line.split(',') for line in line_array]
    
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(cell_array)
   