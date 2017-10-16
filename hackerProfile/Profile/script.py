import requests
from bs4 import BeautifulSoup


def codechef(username):
    details = []
    url = "https://www.codechef.com/users/"
    page = requests.get(url + username)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find_all('div', class_="rating-number")
    problems = soup.select('div h5')
    solved = problems[0].get_text()
    details.append(int(solved[14:len(solved) - 1]))
    details.append(int(data[0].get_text()))
    return details


def github(username):
    details = []
    url = "https://github.com/"
    page = requests.get(url + username)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find_all('span', class_="Counter")
    details.append(int(data[0].get_text()))
    return details


def hackerEarth(username):
    details = []
    url = "https://www.hackerearth.com/"
    page = requests.get(url + username)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find_all('a', class_="large darker float-right weight-600")
    details.append(int(data[2].get_text()))
    return details
