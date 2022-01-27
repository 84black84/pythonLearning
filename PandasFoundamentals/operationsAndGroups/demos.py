import pandas as pd
import os
from PandasFoundamentals.helperClasses.helperClass import HelperClass

helper = HelperClass()
currentDirectory = helper.getCurrentDirectoryPath()
df = pd.read_pickle(os.path.join(currentDirectory, 'data', 'data_frame.pickle'))

# get a smaller data frame of the existing one
small_df = df.iloc[49980:50019, :].copy()
grouped_by_artist = small_df.groupby('artist') # type -> pandas.core.groupby.generic.DataFrameGroupBy

for name, group_df in grouped_by_artist:
    print(name)
    print(group_df)
    break

# Aggregate
# Mins
for name, group_df in grouped_by_artist:
    min_year = group_df['acquisitionYear'].min()
    print("{}: {}".format(name, min_year))

# he is doing some complicated stuff from now on - maybe to revisit in some point in the future