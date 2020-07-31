import json
import difflib

fi=open("dataset.json","r")
file=json.load(fi)
i=1

def findMe(val):
  if val in file:
    return file[val]
  elif val.upper() in file:
    return file[val.upper()]
  elif val.title() in file:
    return file[val.title()]
  elif len(difflib.get_close_matches(val,file))>0:
    inp=int(input("did u mean:\n" + difflib.get_close_matches(val,file)[0] +"\n for yes press 1,for no press 2"))
    if inp==1:
     return file[difflib.get_close_matches(val,file)[0]]
    elif inp==2:
     print("We'll try to add that word soon !")
     return ""
    else :
      print("invalid entry ! \n Returning to main menu.... \n ")
      return""
      
  else:
    print("We'll try to add that word soon !")
    return""
    
      
      
      
while(i):
  start=input("\nPress 1 to enter the Word Book or any other key to exit the wordbook: ")
  
  if(start=="1"):
   val=input("Enter the word you are looking for today: ")
   print(findMe(val.lower()))
  else:
   print("exiting program....")
   exit()
   
