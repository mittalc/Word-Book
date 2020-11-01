import json
import difflib as dl
data=json.load(open("data.json"))

#function to convert word format to  lower,upper and title formats
def convert(word):
    wordArr=[]
    wordArr.append(word.lower())    
    wordArr.append(word.title())
    wordArr.append(word.upper())


    return wordArr

#function to pull meaning from the dataset
def findMeaning(wordConvertedArr):

    for word in wordConvertedArr:

        if word in data:
            i=1
            for item in data[word]:
                
                print(str(i)+". "+ item)
                i+=1
            break 


        if word not in data and word is wordConvertedArr[len(wordConvertedArr)-1]:
            print("I could not find that word. Trying to find close matches : \n" )
            closeMatching(wordConvertedArr)

        
 #function to find close matches to word      
def closeMatching(wordConvertedArr):
    closeArr=[]
    closeArr1=[]

    i=1
    
    for word in wordConvertedArr:

        
        
        close1=dl.get_close_matches(word, data, n=1, cutoff=0.6)
        if(len(close1)!=0):

         closeArr.append(str(i)+ " " + close1[0])
         closeArr1.append(close1[0])
         i+=1

    if(len(closeArr)!=0):
     print(closeArr)
     inp1= int(input("\n Press the number to find meaning of these words or 0 to find another word meaning: "))
     if(inp1==1 and len(closeArr1)>=1):
         return findMeaning(convert(closeArr1[0]))
     elif(inp1==2 and len(closeArr1)>=2):
         return findMeaning(convert(closeArr1[1]))    
     elif(inp1==3 and len(closeArr1)>=3):
         return findMeaning(convert(closeArr1[2]))   
     else:
        print("Could not find any matching words")   

    else:
        print("Could not find any matching words")   