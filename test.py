import pandas as pd
import re

#with open('./fr_50k.txt') as f:
	#data = f.readlines()

cleanData=[]
#for _ in range(1300):
	#print(data[_].replace(re.findall('\S[0-9]+',data[_]),''))
	#print(re.findall('[\d]+',data[_]))
	#cleanData.append(re.findall('\D{1,}',data[_])[0])
	#print(data[_].replace('\n',''))
	#print(_)
#print(data)
#dtf = pd.DataFrame(cleanData)
#dtf.to_excel('cleanned.xlsx')
#print(dtf)

datav=pd.read_csv('./FR_EN.CSV').to_dict(orient='records')

print(datav)