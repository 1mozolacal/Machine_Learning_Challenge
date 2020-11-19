import pandas as pd
import matplotlib.pyplot as plt

def findColSetup(columns, depth):
    discoverNum = 0
    thisLevelBuild = []
    returnLists = []
    for index,col in enumerate(columns):
        if not col[depth].startswith("Unnamed:"):
            if discoverNum == 1 and depth+1 < len(col):
                smallerLists = findColSetup( columns[:index], depth+1)
                returnLists.extend(smallerLists)
            discoverNum+=1
            print( col )
            thisLevelBuild.append(col[depth])
    returnLists.insert( 0, thisLevelBuild)
    return returnLists


df = pd.read_csv("Calvin_Mozola_MachineLearning_DataMultiCol.csv",header=[0,1,2,3,4],index_col=0)

colNames = ['Province','Labour','Gender','Age','Year']
colParse = findColSetup(df.columns,0)
print("Cal col")
print(colParse)

cols = pd.MultiIndex.from_product(colParse,names=colNames)

df.columns = cols

#convert data to numbers
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')


province = "Ontario"
labour = "Labour force 4"
gender ="Males"
age = ""

samp = df['Ontario']['Labour force 4']['Males']
# samp = pd.to_numeric(samp, errors='coerce')
print(samp)
# a = samp.index.get_level_values(2).astype(float)
# for year in samp.columns:
#     yearCol = samp[year]
#     print( type(yearCol))
#     print(yearCol)
#     for age in yearCol.columns:
# #         print(" --> {}".format(age))
# for col in samp.columns:
#     samp[col] = pd.to_numeric(samp[col], errors='coerce')
# print(samp)

sum = samp.sum(level=1, axis=1)#sum ascross gender

plt.figure()
sum.transpose().plot()
    # plt.plot( data=df, marker='o',  linewidth=1)
    
plt.legend()
plt.show()






            