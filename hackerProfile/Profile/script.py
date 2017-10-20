import requests
from bs4 import BeautifulSoup
import datetime


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


def hackerEarth(username):
    details = []

    if username[0] == "@":
        username = username[1:]

    url = "https://www.hackerearth.com/users/pagelets/" + username + "/coding-data/"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    data = soup.find_all('div', class_="line-height-18")
    pro = data[0].text
    ratings = data[1].text

    pro = pro.split(" ")
    pro = pro[2].split("\n")
    details.append(int(pro[0]))

    ratings = ratings.split(" ")
    ratings = ratings[1].split("\n")
    details.append(int(ratings[0]))

    return details


def hackerrank(username):
    def valid_date(datestring):
        try:
            datetime.datetime.strptime(datestring, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    details = []

    url = "https://www.hackerrank.com/rest/hackers/" + username + "/submission_histories"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    data = soup.find(text=True)

    dd = 0
    string = ""
    pro = []
    for i in data:
        if dd == 2:
            dd = 0
            if not valid_date(string):
                pro.append(int(string))
            string = ""
        elif i == '"':
            dd += 1
        elif dd == 1:
            string += i

    details.append(sum(pro))

    url = "https://www.hackerrank.com/rest/hackers/" + username + "/hacker_level"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.findAll(text=True)

    dd = 0
    string = ""
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    for i in range(len(data[0])):
        if dd == 2:
            dd = 0
            if string == "contest_points":
                string = ""
                j = i + 1
                while j < len(data[0]) and data[0][j] != ',':
                    if data[0][j] in number:
                        string += data[0][j]
                    j += 1
                details.append(float(string))
                break
            string = ""
        elif data[0][i] == '"':
            dd += 1
        elif dd == 1:
            string += data[0][i]

    return details


def spoj(username):
    details = []
    url = "http://www.spoj.com/users/"
    page = requests.get(url + username)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find_all('div', class_="col-md-6 text-center valign-center")
    data = data[0].text
    data = data.split("\n")

    details.append(int(data[3]))

    ranking = soup.find_all('div', class_="col-md-3")
    ranking = ranking[0].text
    ranking = ranking.split("\n")
    ranking = (ranking[4])[14:]
    ranking = ranking.split(" ")
    details.append(int(ranking[0]))

    return details


def github(username):
    details = []
    url = "https://github.com/"
    page = requests.get(url + username)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find_all('span', class_="Counter")
    details.append(int(data[0].get_text()))

    return details
