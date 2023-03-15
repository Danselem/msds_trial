# importing packages
import pandas as pd

# reading data
df = pd.read_csv('./KAG_energydata_complete.csv')

# getting shape of data
print("The size of the data is {}. ".format(df.size))