import numpy as np

import pandas as pd

Sample=['S'+str(i) for i in range(1,6)]

Intensity=['I'+str(i) for i in range(1,3)]
Lambda=['L'+str(i) for i in range(1,3)]

# print(Intensity)

# var=np.hstack((Intensity,Lambda))
#
# print(var)


data=pd.DataFrame(columns=[sample], index=[Intensity,Lambda])

print(data)
