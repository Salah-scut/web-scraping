from bs4 import BeautifulSoup
import lxml
import requests

# appointing url and U-A
url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

# get the main page
response = requests.get(url=url,headers=headers)
page_text = response.text.encode('ISO-8859-1').decode('utf-8')

# create a soup instance
soup = BeautifulSoup(page_text,'lxml')

title_list = [x.text for x in soup.select('.book-mulu>ul>li')]
href_list = ['https://www.shicimingju.com/' + x['href']
             for x in soup.select('.book-mulu>ul>li>a')]


print(len(title_list), ' titles')
print(len(href_list), ' href')


content_list = []
for href in href_list:
    chapter_text = requests.get(href,headers).text.encode('ISO-8859-1').decode('utf-8')
    soup_chap = BeautifulSoup(chapter_text,'lxml')
    paragraph_list = str.split(soup_chap.select('body #main .chapter_content')[0].text, '　　')
    content_list.append(['　　' + x + '<br><br>' for x in paragraph_list])



with open('三国.html', 'w', encoding='UTF-8') as fp:
    for i in range(len(href_list)):
        print(title_list[i])
        print(content_list[i])
        fp.write('<hr><b>' + title_list[i] + '</b></hr><br><br>')
        for x in content_list[i]:
            fp.write(x)
