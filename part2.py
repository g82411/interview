import pandas
import requests
import sqlite3 
import re
from bs4 import BeautifulSoup
from threading import Thread


HOST = "https://www.ptt.cc/bbs/"
def getMaxPage(board):
    r = requests.get("{0}{1}".format(HOST, board))
    content = r.content.decode()
    pagenum = re.findall("index(\d+).html",content)
    return pagenum[1]

def getSingleArtile(url):
    r = requests.get(url)
    content = r.content.decode()
    parsedPage = BeautifulSoup(content)
    text = parsedPage.find("div", id="main-content").text
    author = parsedPage.findAll("span", class_="article-meta-value")[0]
    label = parsedPage.findAll("span", class_="article-meta-value")[1]
    title = parsedPage.findAll("span", class_="article-meta-value")[2]
    date = parsedPage.findAll("span", class_="article-meta-value")[3]
    with open("result.txt", "a+") as result:
        result.writelines(author)
        result.writelines(label)
        result.writelines(title)
        result.writelines(date)
        result.writelines(text)
def parseArticleUrl(board):
    pageNum = getMaxPage(board)
    urls = []
    for i in range(2):
        content = requests.get("https://www.ptt.cc/bbs/{0}/index{1}.html".format(board, i),verify=False).content.decode()
        urls.extend(re.findall("M\.\w+\.A\.\w+\.html", content))
    
    return map(lambda url: "{0}/{1}/{2}".format(HOST, board, url), urls)

def main():
    urls = parseArticleUrl("Food")
    for url in urls:
        getSingleArtile(url)

if __name__ == '__main__':
    main()

