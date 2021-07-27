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

print("Title Fetcher: 1.0")
print("Author : Sujal Srivastava")
print("Twitter: @SjlHexa")
with open('response.csv', 'a+') as f: 
  thewriter = csv.writer(f)
  thewriter.writerow(["Url", "Response", "Title"])
file_2 = [] 
def func1(user):
    f = open(user, "r") 
    for line in f: 
        line = line.rstrip()
        if line.startswith('http://') or line.startswith('https://'):
            print(f"[+] Url is in right format : ",line)
            file_2.append(line)
        else:
            print(f"[-] Url isn't in the format : ", line)
            new_url = "http://" + line 
            print(f"[+] Url is corrected to : ", new_url) 
            file_2.append(new_url)

    print(file_2)

def func2(): 
    for z in file_2:
        (response) = requests.get(z)
        soup = BeautifulSoup(response.content, "html.parser")
        soup2 = BeautifulSoup(response.text, 'html.parser')
        print("------------")
        print(soup)
        print(response)
        print(response.headers)
        print("Title of the website is : ")
        for title in soup.find_all('title'): 
            jj = title.get_text()
            print(jj)
        with open('response.csv', 'a+') as x:
            thewriter = csv.writer(x)
            thewriter.writerow([z, response, jj])

        print("_____________________________________________________________________________________")


parser = argparse.ArgumentParser()
parser.add_argument("File_Name", type=str, help="Please check the data given in the file")

args = parser.parse_args()

func1(args.File_Name)
func2()
