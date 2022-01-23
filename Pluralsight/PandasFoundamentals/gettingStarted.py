import numpy as np
import pandas as pd

tempo = 25

# tempoArray = np.random.rand(3)
# tempoSeries = pd.Series(np.random.rand(3))
tempoDataFrame = pd.DataFrame(np.random.rand(3, 2))
tempoDataFrame.columns= ["first", "second"]
first = tempoDataFrame["first"]

print(tempoDataFrame)
print("")
print(first)

# print(tempoArray)
# print(tempoSeries)
