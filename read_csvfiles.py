import pandas as pd

"""df = pd.read_csv("C:\\Users\\malle\\Downloads\\data.csv")
##print(df) #this is print only first 5 rows and last 5 rows
print(df.to_string())"""

"""import pandas as pd
print(pd.options.display.max_rows)"""

import pandas as pd
pd.options.display.max_rows = 9999
df = pd.read_csv("C:\\Users\\malle\\Downloads\\data.csv")
print(df)