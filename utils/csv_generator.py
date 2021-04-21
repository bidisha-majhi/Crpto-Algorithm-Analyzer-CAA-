import pandas as pd 
data = {'Algorithm': ['abc', 'def', 'pqr', 'uvw'], 
                'FileSize': [21, 19, 20, 18], 
                'EncryptionTime(hrs)': [2, 1.5, 3, 1.3], 
                'DecryptionTime(hrs)': [4, 2.1, 3, 2.5]} 
  
df = pd.DataFrame(data, columns = ['Algorithm', 'FileSize', 'EncryptionTime(hrs)', 'DecryptionTime(hrs)']) 
  
print("Given Dataframe :\n", df) 
  
print("\nIterating over rows using index attribute :\n")  
for ind in df.index: 
     print(df['Algorithm'][ind], df['EncryptionTime(hrs)'][ind], df['DecryptionTime(hrs)'][ind]) 

df.to_csv(path_or_buf='cryptography.csv',index=False)