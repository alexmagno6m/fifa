import pandas as pd
import numpy as np
df = pd.read_csv(r'data.csv', encoding='ISO-8859-1', delimiter=',')
df1 = df[['Age', 'Nationality']]
print(df1)