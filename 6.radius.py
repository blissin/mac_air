import pandas as pd
import csv

test=pd.read_csv('/Users/song/Desktop/test.csv')
# print(test)
# filtered=test[test['direction']=='Y']
# filtered2=filtered[filtered['agg']=='Raw']
# print(filtered)
# print()
# print(filtered2)

filtered_test=test[(test.aggregation=='Raw')&(test.direction=='Y') ]
print(filtered_test)

