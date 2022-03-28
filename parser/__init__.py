import requests
from bs4 import BeautifulSoup as bs


class Parser:

    def __init__(self):
        self.url = 'https://www.consultant.ru/cons/cgi/online.cgi'
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        }

    def parse(self):
        self.session.post(self.url, headers=self.headers, data={
            't': 'КИИ, ТЭК',
            'searchPlus': '1',
            'req': 'syntax'
        })

        response = self.session.post(self.url, headers=self.headers, data={
            'req': 'query',
            'SEARCHPLUS': 'КИИ, ТЭК',
            'mode': 'splus',
            'content': 'list',
        })

        data = response.json()
        result = []

        for item in data['list']['listpanes'][0]['items']:
            title_list = list(filter(lambda x: x['class'] == 'TH', item['title']))
            if len(title_list) < 1:
                continue

            title = bs(title_list[0]['html'], 'html.parser').text
            link = f'{self.url}?req=doc&&mode=splus&base=LAW&n={item["nd"]}'

            result.append([title, link])

        return result


if __name__ == '__main__':
    parser = Parser()
    docs = parser.parse()

    print(docs)
