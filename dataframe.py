import pandas as pd
data = {
  "calories": [450, 370, 390],
  "duration": [50, 70, 45]
}
df = pd.DataFrame(data, index=["day1", "day2","day3"])
#print(df)
#print(df.loc[0])
#print(df.loc[[0,1]])
#print(df)
print(df.loc["day2"])
