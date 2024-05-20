# Genetica-FAGRO
Contiene codigo Python y planillas Analisis datos Holando 2024
Vaca.py toma los datos de “genotipos_2.xlsx” donde forma un dataframe con los
Valores “X/Y” de las 24 vacas y 4478 SNPs
Cuenta la cantidad de gen_ATAT = ["A/A","A/T","T/A","T/T"], 
gen_ATGC = ["A/G","A/C","T/G","T/C"] y gen_GCGC = ["G/G","G/C","C/G","C/C"], llamandosles A1A1, A1A2 y A2A2 respectivamente. Ignora los vacíos.
Calcula luego el % de heterocigotas (% de A1A2)
Produce un histograma de frecuencias de He atraves de los SNPs
Produce una planilla con datos procesados llamada “vaca_out.xlsx”

Cromo.py lee 'cromosomas.xlsx'. 
Calcula el contenido de “GC” en cada cromosoma y produce un histograma
Produce una planilla con datos procesados “cromosoma_out.xlsx”

PCA.py lee 'genotipos_2.xlsx’ 
Realiza una transformación de valores, del tipo “X/Y” a 0,1 o 2.
'A/A': 0, 'A/T': 0, 'T/A': 0, 'T/T': 0,
 'A/G': 1, 'A/C': 1, 'T/G': 1, 'T/C': 1,
 'G/G': 2, 'G/C': 2, 'C/G': 2, 'C/C': 2
Analiza la frecuencia de los tipos “0”, “1” y “2” para cada animal, atraves de los 4478 loci y calcula los Componentes Principales usando estos datos.
Grafica los dos primeros componentes principales

Se produce manualmente “vaca_out_final.xlsx”, a partir de “vaca_out.xlsx”, que además contiene los analisis Chi Cuadrado de las frecuencias respecto a Hardy Weinberg



