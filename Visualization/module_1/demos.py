import pandas as pd
import matplotlib.pyplot as plt
from PandasFoundamentals.helperClasses.helperClass import HelperClass

helper = HelperClass()
df = helper.getDataFrameFromCsvFile('water')
df.info()

ax = df.plot(subplots=True, title="Water measurements off the Dutch coast")

df['datetime'] = pd.to_datetime(df['datetime'])
df.info()

ax = df.plot(title="Water temperature", x='datetime', y='temp')
df['temp'].plot.box()

dfNobel = helper.getDataFrameFromCsvFile('nobel')
prizes_countries = dfNobel['Country'].value_counts()

top_countries = prizes_countries[:10]
top_countries.plot.pie()
ax = top_countries.plot.bar(title="Top Nobel Prize Winning Countries")

ax = dfNobel.plot.scatter(x='Country', y='Year')

grades = pd.DataFrame([[6, 4, 5], [7, 8, 8], [6, 7, 5], [6, 5, 7],
                       [5, 2, 6]], 
                       index = ['Mary', 'John', 'Ann', 'Pete', 'Laura'],
                       columns = ['test_1', 'test_2', 'test_3'])

ax = grades.mean(axis=1).plot.barh(title="Average student score")
grades['average'] = grades.mean(axis=1)
ax = grades.plot.bar(title="All test grades")

grades.loc['whole class'] = grades.mean()
ax = grades.plot.bar(title="All test grades")