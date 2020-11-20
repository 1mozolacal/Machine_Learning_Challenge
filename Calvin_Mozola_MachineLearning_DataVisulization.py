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
            thisLevelBuild.append(col[depth])
    returnLists.insert( 0, thisLevelBuild)
    return returnLists


def parseDataFromCsv():
    # configurations
    breakByGender = "n" #yes or no
    breakByAge = "y" # yes or no
    province = "Ontario"
    labour = "Labour force 4"

    plotSamps = []

    df = pd.read_csv("Calvin_Mozola_MachineLearning_DataMultiCol.csv",header=[0,1,2,3,4],index_col=0)
    colNames = ['Province','Labour','Gender','Age','Year']
    colParse = findColSetup(df.columns,0)
    cols = pd.MultiIndex.from_product(colParse,names=colNames)
    df.columns = cols
    for col in df.columns:#convert data to numbers
        df[col] = pd.to_numeric(df[col], errors='coerce')
    samp = df[province][labour]
    
    if breakByGender.lower() == 'y':
        plotSamps.append( (samp['Males'].sum(level=1, axis=1),'^','solid','Labour divison with Males') )
        plotSamps.append( (samp['Females'].sum(level=1, axis=1),'v','solid','Labour divison with Females') )
    else:   
        if  breakByAge.lower() == 'y':
            totalDf = [None,None,None]
            ageList = ['15 to 24 years','25 to 54 years','55 years and over']
            for genderSplit in list(set(findColSetup(samp,0)[0])):
                print(genderSplit)
                for x in range(len(totalDf)):
                    if totalDf[x] is None:
                        totalDf[x] = samp[genderSplit][ageList[x]].sum(level=0,axis=1)
                    else:
                        totalDf[x] = totalDf[x].add( samp[genderSplit][ageList[x]].sum(level=0,axis=1) )
            for index,item in enumerate(totalDf):
                plotSamps.append( (item,'o','solid',ageList[index]) )
        else: 
            plotSamps.append( (samp.sum(level=2, axis=1),'o','solid','Labour divison with all gender') )
    return plotSamps


if __name__ == "__main__":
    allData = parseDataFromCsv()

    for dataSet in allData:
        data,marker,line,title = dataSet
        data.transpose().plot(title=title, marker=marker,linestyle=line)
        plt.legend(bbox_to_anchor=(0.8, 1),loc='upper left',borderaxespad=0., fontsize='xx-small',framealpha=0.25)
    plt.show()


            