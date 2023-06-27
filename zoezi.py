import requests
from bs4 import BeautifulSoup
import _pyinstaller_hooks_contrib.tests.scripts  

while True:
    password=input("please input your password:.....")
    try:
        password=int(password)

    except:
        print("please put in numbers alone")
        continue
    if password==123456:
        print("welecome to your website")
        # Making a GET request
        url=str(input("please input url of the site you want to scrap:"))
        r = requests.get(url)
        # Parsing the HTML
        soup = BeautifulSoup(r.content, 'html.parser')

        s = soup.find('div')
        content = s.find_all('p')
        link=s.find_all('a')
        for i in soup.title:
            print(soup.title.text)
        for lines in content:
            print(lines.text)
        print("\033[4mTHE LINKS FOUND IN THIS PAGE ARE\033[0m'")
        for i in link:
            print(i.get("href"))

        break
    else:
        print("incorrect password try again")
        continue
