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
    details.append(data[0].get_text())
    return details


def codeforces(username):
    details = []
    flag2 = 0
    url = "http://codeforces.com/contests/with/" + username

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    pro = []
    data = soup.find('div', class_="datatable")
    data = data.text
    data = data.strip()

    for i in range(len(data)):
        if data[i] != " " and data[i] != "\n" and data[i] != "\r":
            pro.append(data[i])

    i = 49
    if i >= len(pro):
        details.append(0)
    else:
        number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        total = ""

        while pro[i] in number:
            total += pro[i]
            i += 1

        details.append(int(total))

    url = "http://codeforces.com/profile/" + username

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    data = soup.find_all('div', class_="info")
    data = data[0].text
    data = data.strip()
    data = data.split("\n")

    for i in range(len(data)):
        data[i] = data[i].strip()

    for i in range(len(data)):
        if data[i] == "Contest rating:":
            d = data[i + 2]
            details.append(int(d[:4]))
            flag2 = 1
            break

    if flag2 == 0:
        details.append(0)

    print(details[0])
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

    url = "https://www.hackerrank.com/rest/hackers/" + username + "/rating_histories_elo"
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.findAll(text=True)
    rank = data[0][-75:-60]
    flag = 0
    total = ""
    for i in range(len(rank)):
        if rank[i] in number or flag == 1:
            total += rank[i]
            flag = 1
            if len(total) == 5:
                break
    details.append(float(total))

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

    url = "https://github.com/" + username + "?tab=repositories"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find_all('div', class_="d-inline-block mb-1")
    desc = soup.find_all('p', class_="col-9 d-inline-block text-gray mb-2 pr-4")

    if len(data) == len(desc):
        for i in range(len(data)):
            string = data[i].text
            string = string.strip()
            string = string.split(" ")
            link = "http://www.github.com/" + username + "/" + string[0]
            description = desc[i].text
            description = description.strip()
            details.append((string[0], description, link))
        return details

    else:
        return details
