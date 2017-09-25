import requests

search_query = input("Please enter searche: ")

url = str('https://zvooq.com/api/search/?_page=1&query=' + search_query)  # url для второй страницы
r = requests.get(url)
#with open('test.json', 'wb') as output_file:
 #   output_file.write(r.text.encode('utf-8'))
    # print (r.text)
