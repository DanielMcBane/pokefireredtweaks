# These don't do anything for some reason >:(

from pandas import DataFrame
l1 = [1,2,3,4]
l2 = [1,2,3,4]
df = DataFrame({'Stimulus Time': l1, 'Reaction Time': l2})
print(df)

df.to_excel('test.xlsx', sheet_name='sheet1', index=False)

f = open('example.csv', 'w')
f.write("display,variable x")
f.close()