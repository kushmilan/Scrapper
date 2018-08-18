# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 16:59:32 2018

@author: Milan
"""

"""
Web Scrapper for scrapping gsmarena, TutorialsPoint & Wikipedia.
"""

import re
import requests
from bs4 import BeautifulSoup


def GsmArena():
    
    url=input("Enter the URL you want to scrap(GsmArena) : ")
    
    Req=requests.get(url)
    soup=BeautifulSoup(Req.text, 'html.parser')
    """Main headlines."""
    for i in soup.select(' h3'):
        print(i.text)
    print("===============================================================================")
    """Latest devices and in stories now."""
    for i in soup.select('.module-phones-link'):
        print(i.text)
    print("===============================================================================")
    """Top 10 by daily intrest and top 10 by fans."""
    for i in soup.select('nobr'):
        print(i.text)


def TutorialsPoint():
    url=input("Enter the URL you want to scrap(TutorialsPoint) : ")

    Req=requests.get(url)
    soup=BeautifulSoup(Req.text, 'html.parser')

    Choices="""
    Choose any option you want to scrap from course page(tutorials point).
    Headings      =1
    Index elements=2
    Paragraph     =3
    """
    print(Choices)
    option=input('Enter your choice : ')
    if(option=='1'):
        ChoiceOrg='.heading'
    elif(option=='2'):
        ChoiceOrg='a'
    elif(option=='3'):
        ChoiceOrg='p'
    else:
        print("You have chosen a wrong choice!")
                    
    DataList=list()
    for i in soup.select(ChoiceOrg):
        item=re.findall(r'^[A-Z].*',i.text)
        DataList.append(item)
    a=[]
    while(a in DataList):
        DataList.remove([])
    print(DataList)

def Wikipedia():
    URL=input('Enter the URL you want to scrap(Wikipedia) : ')
    URLG=requests.get(URL)
    soup=BeautifulSoup(URLG.text,'html.parser')
    for i in soup.select('h1'):
        print('Page content is based on : ',i.text)
    print('\n')
    print('headings reguarding %s are : ' %(i.text))
    for i in soup.select('.mw-headline'):
        print(i.text)


GsmArena()
TutorialsPoint()
Wikipedia()







'''url=input("Enter the URL you want to scrap : ")

Req=requests.get(url)
soup=BeautifulSoup(Req.text, 'html.parser')
"""Main headlines."""
for i in soup.select(' h3'):
    print(i.text)
print("===============================================================================")
"""Latest devices and in stories now."""
for i in soup.select('.module-phones-link'):
    print(i.text)
print("===============================================================================")
"""Top 10 by daily intrest and top 10 by fans."""
for i in soup.select('nobr'):
    print(i.text)'''
