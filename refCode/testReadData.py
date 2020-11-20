import pandas as pd

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


df = pd.read_csv("testerData.csv",header=[0,1],index_col=0)
print(df)

calCol = findColSetup(df.columns,0)
print("-------------")
print(calCol)

# Manual method
# cols = pd.MultiIndex.from_tuples([ ('cal','today'),('cal','tom'),('cal','yes'),('eric','today'),('eric','tom'),('eric','yes') ])
# iters = [ ['cal','eric'],['today','tom','yes'] ]
cols = pd.MultiIndex.from_product(calCol,names=['Person','Day'])
df.columns = cols

print(df["eric"])
print(df["cal"])
print(df)
print( df.columns)




            