import argparse
import csv
import requests
from bs4 import BeautifulSoup
# user_input = input("Enter the file name : ")
with open('response.csv', 'w') as f: #will check if the file exists
  thewriter = csv.writer(f)
  thewriter.writerow(["Url", "Response", "Title"])# appended this file
file_2 = []
def func1(user):
    f = open(user, "r")
    for line in f:
        line = line.rstrip()
        print(line)
        # for check_url in url_list:  # loop through each url in the list
        if line.startswith('http://') or line.startswith('https://'):  # check if the url starts with web prtocol http/https or not
            print(f"[+] Url is in right format : ",line)  # if url strats with http/https like e.g http://web.com then print the url is in right format
            file_2.append(line)
        else:
            print(f"[-] Url isn't in the format : ", line)
            new_url = "http://" + line  # Adding right formating to the url (url prefix)
            print(f"[+] Url is corrected to : ", new_url)  # corectly formated url is new_url
            file_2.append(new_url)
        # file_2.append(line)
        # file_2.append("\n")

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
print(f"{args.File_Name}")
func1(args.File_Name)
func2()
