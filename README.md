# Simple_Title_fetcher
A python script to fetch title, status and content of urls in a list. The script uses beautiful soup for html parsing. 

The script takes filename as a input and fetch list of urls from the user-defined filename. Currently the script fetches below details from the url :
"list.txt" which contains following links:
www.github.com
www.replit.com
www.youtube.com
www.facebook.com
www.twitter.com


Example :
The URL's are in "list.txt" 
![2021-07-27 20_09_06-](https://user-images.githubusercontent.com/82680541/127174896-06c88481-7ffc-48a6-99c5-35cc5379b73c.png)


Now we will run main.py and give the input as "list.txt":

python main.py list.txt

![2021-07-27 20_07_57-task2 - Replit and 29 more pages - Personal - Microsoft​ Edge](https://user-images.githubusercontent.com/82680541/127175372-e426ec76-aaca-44e7-a267-d33451d8370c.png)

When we run this we will be welcomed with a banner "Title Fetcher"
![2021-07-27 20_12_10-task2 - Replit and 30 more pages - Personal - Microsoft​ Edge](https://user-images.githubusercontent.com/82680541/127175618-d7bd35e8-c465-43db-aae2-a8a45e411360.png)

Now the program will start to fetch data from the urls given

Once the program completely runs a new "responce.csv" file will be created
![2021-07-27 20_13_09-task2 - Replit and 30 more pages - Personal - Microsoft​ Edge](https://user-images.githubusercontent.com/82680541/127176734-7a42a8e5-4708-4901-aebf-d2d2e3d80ab1.png)

"responce.csv" will contain all the fetched data from the urls:
![2021-07-27 20_13_19-task2 - Replit and 30 more pages - Personal - Microsoft​ Edge](https://user-images.githubusercontent.com/82680541/127179285-74dae0c1-2985-4956-86b4-a6d2872590a6.png)

python3 
