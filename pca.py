# Calcula Componentes Prinipales

# Analiza base de datos SNP Holando
import pandas as pd
import numpy as np

# Read the XLSX files into a DataFrame
df = pd.read_excel('genotipos_2.xlsx', na_values='Missing')
df = df.drop(columns=df.columns[0])
print(df)

###############################################
import pandas as pd

# Assuming 'df' is your original DataFrame with 24 columns of "X/Y" type values

# Define a function to apply to each row
def assign_values(row):
    # Create a dictionary to map the patterns to the values
    value_map = {
        'A/A': 0, 'A/T': 0, 'T/A': 0, 'T/T': 0,
        'A/G': 1, 'A/C': 1, 'T/G': 1, 'T/C': 1,
        'G/G': 2, 'G/C': 2, 'C/G': 2, 'C/C': 2
    }
    
    # Initialize a list to store the new values
    new_values = []
    
    # Iterate over each cell in the row
    for cell in row:
        # Get the value from the map, default to 5 if the pattern is not found
        new_values.append(value_map.get(cell, 5))
    
    return new_values

# Apply the function to each row and create new columns
new_columns = df.apply(lambda row: assign_values(row), axis=1, result_type='expand')

# Set the column names for the new columns
new_column_names = [f'b{i}' for i in range(24)]
for i, column_name in enumerate(new_column_names):
    df[column_name] = new_columns[i]
#print(df)

# PCA analysis
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Assuming 'df' is your DataFrame and it has 48 columns in total

# Select the last 24 columns for PCA
data_for_pca = df.iloc[:, -24:]

# Standardize the data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_for_pca)

# Apply PCA
pca = PCA(n_components=2)  # Example: Reduce to 2 principal components
principal_components = pca.fit_transform(data_scaled)

# Create a DataFrame with the principal components
principal_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])

# Explained variance ratio
print("Explained variance ratio:", pca.explained_variance_ratio_)

# Add the principal components to the original DataFrame if needed
df['PC1'] = principal_df['PC1']
df['PC2'] = principal_df['PC2']

# Visualizar PCA
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd

import matplotlib.pyplot as plt

# Assuming 'principal_df' is the DataFrame with the principal components 'PC1' and 'PC2'
# and 'df' is the original DataFrame with the column names

# Extract the column names for labeling
column_labels = df.columns[-24:].tolist()  # Adjust the index if needed

# Create a scatter plot
plt.figure(figsize=(10, 8))
plt.scatter(principal_df['PC1'], principal_df['PC2'], alpha=0.5)

# Label each point with the corresponding column name
for i, label in enumerate(column_labels):
    plt.annotate(label, (principal_df['PC1'][i], principal_df['PC2'][i]))

# Set the title and labels for the axes
plt.title('PCA Results')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

# Show the plot
plt.show()
