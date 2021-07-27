logo = """

  _______ __  __        ______     __       __             
 /_  __(_) /_/ /__     / ____/__  / /______/ /_  ___  _____
  / / / / __/ / _ \   / /_  / _ \/ __/ ___/ __ \/ _ \/ ___/
 / / / / /_/ /  __/  / __/ /  __/ /_/ /__/ / / /  __/ /    
/_/ /_/\__/_/\___/  /_/    \___/\__/\___/_/ /_/\___/_/     
                                                           

"""

import argparse
import csv
import requests
from bs4 import BeautifulSoup
print(logo)
with open('response.csv', 'a+') as f: #checks if the file exists or not if not then it will create the file and open it
  thewriter = csv.writer(f)#start's the writer function
  thewriter.writerow(["Url", "Response", "Title"])# appended this in the file response.cvs
file_2 = [] # created a blank list for storing data
def func1(user):
    f = open(user, "r") # opening the file given by the user in read only mode
    for line in f: #looping through line by line
        line = line.rstrip()# removes the trailing charcters.
        if line.startswith('http://') or line.startswith('https://'):  # check if the url starts with web prtocol
            # http/https or not
            print(f"[+] Url is in right format : ",line)  # if url strats with http/https like e.g http://web.com then
            # print the url is in right format
            file_2.append(line)#appends the url to the list if it clears the if statement.
        else:
            print(f"[-] Url isn't in the format : ", line)#tells that the url is not having web protocol http/https.
            new_url = "http://" + line  # Adding right formating to the url (url prefix)
            print(f"[+] Url is corrected to : ", new_url)  # corectly formated url is new_url
            file_2.append(new_url)# appends the new url wich have web protocol

    print(file_2)# print the list

def func2(): # extract the data and append it to the response file.
    for z in file_2:#loop through the file.(and also reset the variables for looping)
        (response) = requests.get(z)# this send's get request to the urls which are looping.
        soup = BeautifulSoup(response.content, "html.parser")#extract content of the sites and store it into a variable
        soup2 = BeautifulSoup(response.text, 'html.parser')#extract text from the sites and store it into a variable
        print("------------")#print a small line helps the code to look cleaner and more readable.
        print(soup)#prints the content of the site which was stored in the variable
        print(response)#print's the responce code it helps in  checking if the site/webpage is up or not
        print(response.headers)#print's headers of the site.
        print("Title of the website is : ")#print's a string to make our code more readable
        for title in soup.find_all('title'): #finds the title of the site which is currently looping
            jj = title.get_text()# stores the title in the variable
            print(jj)#prints the variable
        with open('response.csv', 'a+') as x:# opens the file response.csv in append mode
            thewriter = csv.writer(x)#start's the writer function
            thewriter.writerow([z, response, jj])#appends the data stored i the variable into the csv file.

        print("_____________________________________________________________________________________")
        #print's a line to make are code look readable

parser = argparse.ArgumentParser()#generates help and usage messages.
parser.add_argument("File_Name", type=str, help="Please check the data given in the file")
#takes input of the argument name and type and also the help function what should it print.
args = parser.parse_args()# it phrases the args
## print(f"~ FileName : {args.File_Name}")#print the
func1(args.File_Name)#calls the function and also gives the input to the function
func2()#calls the function
