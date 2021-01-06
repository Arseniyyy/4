import pandas as pd


csv = pd.read_csv('validate.csv', sep=';')

print(csv.axes[1]['[2,1]'])