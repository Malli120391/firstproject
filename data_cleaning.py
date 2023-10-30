"""import pandas as pd
df = pd.read_csv("C:\\Users\\malle\\Downloads\\data.csv")
new_df1 = df.dropna()
print(new_df1.to_string())"""

"""import pandas as pd
df = pd.read_csv('C:\\Users\\malle\\Downloads\\data.csv')
df.dropna(inplace = True)
print(df.to_string())"""

"""import pandas as pd
df = pd.read_csv('C:\\Users\\malle\\Downloads\\data.csv')
df.fillna(130, inplace = True)"""

"""import pandas as pd
df = pd.read_csv('C:\\Users\\malle\\Downloads\\data.csv')
df["Calories"].fillna(130, inplace = True)"""

"""import pandas as pd

df = pd.read_csv('C:\\Users\\malle\\Downloads\\data.csv')

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)"""

import pandas as pd

df = pd.read_csv('C:\\Users\\malle\\Downloads\\data.csv')

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)
