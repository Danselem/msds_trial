# importing packages
import pandas as pd

# reading data
df = pd.read_csv('./KAG_energydata_complete.csv')

# getting shape of data
print("The shape of the data is {}. It means it has {} rows and {} columns.".format(df.shape, df.shape[0], df.shape[1]))