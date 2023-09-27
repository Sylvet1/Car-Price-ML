#LEER UN CSV

#TABLA
print("TABLA")
import pandas as pd
dataFrame = pd.read_csv('Car_Prices_Poland.csv')
print(dataFrame)

print("\nGRAFICO DE BARRAS DATOS CATEGORICOS")
# GRAFICO DE BARAS - DATOS CATEGORICOS
import matplotlib.pyplot as plt

dataFrame['province'].value_counts().plot(kind='bar') #poner la columna categorica
plt.show()

print("\nGRAFICO DE PASTEL")
#PASTEL - MUESTRA PORCIONES
dataFrame['city'].value_counts().plot(kind='pie', autopct='%1.1f%%') #poner la columna categorica
plt.show()

print("\nHISTOGRAMA")
#HISTOGRAMA, MUESTRA DISTRIBUCION DE UNA COLUMNA NUMERICA
dataFrame['price'].plot(kind='hist', bins=30) #columna unmerica
plt.show()

print("\nGRAFICO DE LINEA")
#LINEA - TENDENCIA EN SERIES TEMPORALES
dataFrame.plot(x='year', y='price', kind='line') #x='columna_temporal', y='columna_numerica
plt.show()

print("\nDIAGRAMA DISPERSION")
#RELACION ENTRE DOS COLUMNAs NUMERICAS
dataFrame.plot(x='price', y='mileage', kind='scatter') #x='columna_numerica1', y='columna_numerica2'
plt.show()

print("\nDIAGRAMA DE CAJA")
#MUESTRA DiSTRIBUCION Y DETECTA VALORES ATIPICOS
dataFrame.boxplot(column='price') #columna numerica
plt.show()

print("\nGRAFICO DE AREA")
#SIMILAR AL GRAFICO DE LINEA PERO AREA RELLENA
dataFrame.plot(x='year', y='price', kind='area') #x='columna_temporal', y='columna_numerica',
plt.show()