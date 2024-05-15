
# Analiza base de datos SNP Holando
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the "cromosomas" XLSX files into a DataFrame
df = pd.read_excel('cromosomas.xlsx', na_values='Missing')

# Agregar tres columnas ATAT, ATGC y GCGC
tipo_GC = ["G", "C"]

# Cuando solo "A1" tiene un valor y "A2" esta vacia,
# quiere decir que ambas valen A1
df['A2'].fillna(df['A1'], inplace=True)

# Calculate GC content using vectorized operations
df['GC_A1'] = df['A1'].isin(tipo_GC).astype(int)
df['GC_A2'] = df['A2'].isin(tipo_GC).astype(int)
df['GC_TOTAL'] = df['GC_A1'] + df['GC_A2']

# Calculate GC frequency per locus
df['frec_GC'] = df['GC_TOTAL'] / 2

# Drop chromosome MT
df = df.drop(df[df['Cromosoma'] == "MT"].index)

# Ensure 'Cromosoma' is treated as a categorical variable
df['Cromosoma'] = df['Cromosoma'].astype('category')
print(df)

# Now, when you group by 'Cromosoma', pandas will maintain the categorical data type
grouped = df.groupby('Cromosoma')['frec_GC'].agg(['mean', 'std']).reset_index()
# Display df
print(grouped)

# Plotting
plt.figure(figsize=(10, 6))

# Create a point plot with error bars for standard deviation
# The 'order' parameter ensures that the categories are plotted in the order they appear in the data
sns.pointplot(x='Cromosoma', y='mean', data=grouped, capsize=.2, join=False, order=grouped['Cromosoma'])

# Optionally, you can add the standard deviation as error bars
plt.errorbar(x=np.arange(len(grouped['Cromosoma'])), y=grouped['mean'], yerr=grouped['std'], fmt='none', c='k', capsize=5)

# Improve plot aesthetics
plt.xlabel('Cromosoma')
plt.ylabel('Frecuencia G+C')
plt.title('Frecuencia G+C por Cromosoma')
plt.xticks(rotation=90)  # Rotate x-axis labels if they overlap
plt.tight_layout()  # Adjust layout to prevent clipping of labels

# Display the plot
plt.show()

# Exportar como excel
grouped.to_excel("cromosoma_out.xlsx")
# Exportar figura
plt.savefig('C:/Users/Pablo/Maestria/Genetica/cromosomas.png')
#plt.close()
