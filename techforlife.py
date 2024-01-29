
import requests
from bs4 import BeautifulSoup

# links e head 
for y in range(12):
    url= "https://www.tek4life.pt/pt/informatica?p={y}"
    head= {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

    #Verificar se entramos no site
    site=requests.get(url, headers=head)
    print(site.status_code)

    #Html formatado 
    cont=BeautifulSoup(site.content,  'html.parser')
    
    #Sacar o bloco de todos os acessorios
    acessorios=cont.find_all('div', class_='category-products-grid')
    for x in acessorios:
        #Sacar as informaçoes de  todos os acessorios 
        desc=x.find('h2', class_='product-name').getText()
        desc=desc.strip("\n")
        preco=x.find('span', class_='price').getText()
        preco=preco.strip("\n")
        link_prod=x.find('h2', class_='product-name').find('a').get('href')

        with open('tech4life.csv', 'a',encoding='utf-8') as file:
            file.write(f'{desc};{preco};{link_prod};\n')

    