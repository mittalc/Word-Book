
import functions

from functions import convert
from functions import findMeaning
from functions import closeMatching 


while(1):
    inp=input("What word are you looking for today?  (Press y anytime to exit the program) ")
    if(inp=="y" or inp =="Y"):
        exit()

        

    wordConvertedArr = convert(inp)
    Meaning= findMeaning(wordConvertedArr)







