from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

driver = webdriver.Chrome()
# Acessar o site
driver.get(
    'https://www.amazon.com/s?rh=n%3A16225009011&fs=true&ref=lp_16225009011_sar')
# Pegar os títulos
titulos = driver.find_elements(
    By.XPATH, "//span[@class='a-size-base-plus a-color-base a-text-normal']")
# Pegar os Preços
precos = driver.find_elements(By.XPATH, " //span[@class='a-price-whole']")
# Criando a planilha
workbook = openpyxl.Workbook()
# Criando a página produtos
workbook.create_sheet('produtos')
# Seleciona a pasta produtos
sheet_produtos = workbook['produtos']
sheet_produtos['A1'].value = 'Produtos'
sheet_produtos['B1'].value = 'Preços'

for titulo, preco in zip(titulos, precos):
    sheet_produtos.append([titulo.text, preco.text])

workbook.save('Produtos.xlsx')
