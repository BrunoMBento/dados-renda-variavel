
from requests import get
from selenium import webdriver
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np

import time
import re

def setupDriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    return browser

def getUrlSoup(browser):
    url = 'https://www.fundsexplorer.com.br/ranking'
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    return soup

def processarLinha(l, tag, colunasUteis):
	str = ''
	colunas = l.findChildren(name=tag)
	numCol = 1
	for c in colunas:
		if numCol in colunasUteis:
			str += c.text+'\t'
		numCol = numCol + 1
	return str

browser = setupDriver()

soup = getUrlSoup(browser)

tabela_fiis = soup.find(class_='default-fiis-table__container__table')
linhas = tabela_fiis.findChildren('tr')

lista_fiis = [
	'AFHI11',
	'ALZR11',
	'BTLG11',
	'GARE11',
	'HGLG11',
	'HGRE11',
	'HGRU11',
	'HSML11',
	'PVBI11',
	'KDIF11',
	'KNRI11',
	'RBRP11',
	'RZTR11',
	'XPML11',
]

#colunasUteis = [1,3,4,5,6,7,8]

numLinha = 1
for l in linhas:
	if numLinha == 1: 
		str = processarLinha(l, 'th', [1,2,3,5,6,7])
		print(str)
	else:
		if l.td.text in lista_fiis:
			str = processarLinha(l, 'td', [1,2,3,5,6,7])
			print(str)
	numLinha = numLinha + 1

