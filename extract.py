import pandas as pd
print ('Extract Data')

#Sample data
data = {
    'id':[101,102,103],
    'Name':['Ram','Raj','Raja'],
    'Age':[29,34,42]
}
#Create dataframe
df = pd.DataFrame(data)

#display dataframe
print(df)
