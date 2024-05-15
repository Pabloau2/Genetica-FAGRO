# Analiza base de datos SNP Holando
import pandas as pd
import numpy as np

# Read the XLSX files into a DataFrame
df = pd.read_excel('genotipos_2.xlsx', na_values='Missing')

# Agregar tres columnas ATAT, ATGC y GCGC

df["A1A1"] = ""
df["A1A2"] = ""
df["A2A2"] = ""
df ["Tot_gen"] = ""

gen_ATAT = ["A/A","A/T","T/A","T/T"]
gen_ATGC = ["A/G","A/C","T/G","T/C"]
gen_GCGC = ["G/G","G/C","C/G","C/C"]

countATAT = 0
countATGC = 0
countGCGC = 0

#print(df)

# Row index to iterate over (e.g., the second row)
row_index = 0

# Column indices to iterate through (e.g., columns 'A' and 'C')
columns_to_iterate = ["animal.1",	"animal.3",	"animal.4",	"animal.5",	"animal.6",	"animal.8",	"animal.9",	"animal.10"]

# Iterate through cells of the specified row for certain columns
for row_index in range(0,7748):
    for column in columns_to_iterate:
        cell_value = df.loc[row_index, column]
        if cell_value in gen_ATAT:
            countATAT = countATAT +1
        elif cell_value in gen_ATGC:
            countATGC = countATGC +1
        elif cell_value in gen_GCGC:
            countGCGC = countGCGC +1
          
    # append data calculated for each new row
    df.loc[row_index, ['A1A1']] = countATAT
    df.loc[row_index, ['A1A2']] = countATGC
    df.loc[row_index, ['A2A2']] = countGCGC
    df.loc[row_index, ['Tot_gen']] = int(countATAT+countATGC+countGCGC)
    #df.loc [row_index,['Frec_He']] = countATGC/(countATAT+countATGC+countGCGC)
        
    # return variables to zero
    countATAT = 0
    countATGC = 0
    countGCGC = 0
    
#print(df)

A1A1 = 0
A1A2 = 0
A2A2 = 0

# Calculate statistics for genotype freq
# in polulation

A1A1 =  df['A1A1'].sum()
A1A2 =  df['A1A2'].sum()
A2A2 =  df['A2A2'].sum()
print("A1A1 son: ", A1A1)
print("A1A2 son: ", A1A2)
print("A2A2 son: ", A2A2)
print("-----------------")
print("Total    :", A1A1+A1A2+A2A2)

#Calculate He freq per locus
df['Tot_gen'] = df['Tot_gen'].replace(0, np.nan)
df['Frec_He'] = (df['A1A2'] / df['Tot_gen']).fillna(0)

print(df)

#  Plot He values
import matplotlib.pyplot as plt

# Plotting the histogram
plt.hist(df['Frec_He'].dropna(), bins=10) 

# Adding labels and title
plt.xlabel('Valores Frec A1A2')
plt.ylabel('Frecuencia')
plt.title('Frecuencias de A1A2')

# Display the histogram
#plt.show()
#plt.savefig('C:/Users/Pablo/Maestria/Genetica/histogram.png')
#plt.close()

# Save df as excel sheet
df.to_excel("vaca_out.xlsx")

