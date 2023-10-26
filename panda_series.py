"""import pandas as pd
a = [1, 7, 5]
mydata = pd.Series(a)
#print(mydata)
print(mydata[0])"""

"""import pandas as pd
b = [1,5,9]
myval = pd.Series(b, index=['x','y','z'])
#print(myval)
print(myval['z'])"""

"""import pandas as pd
calories = {"day1": 450, "day2": 370, "day3": 390}
mycal = pd.Series(calories)
print(mycal)"""

"""import pandas as pd
calories = {"day1": 450, "day2": 370, "day3": 390}
mycal = pd.Series(calories, index=["day1", "day2"])
print(mycal)"""

import pandas as pd
data ={
"calories" : [450,  370, 390],
"duration": [50, 40, 45]
}
mydfram = pd.DataFrame(data)
print(mydfram)







