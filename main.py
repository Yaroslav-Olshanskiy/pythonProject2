from bs4 import BeautifulSoup
with open('index.html', encoding = 'UTF8') as file:
    src = file.read()
soup = BeautifulSoup(src, 'html.parser')
r = soup.find('div', class_ = 'top_block').text
print(r)