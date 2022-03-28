import requests


class Parser:

    def __init__(self):
        self.url = 'https://www.consultant.ru/cons/cgi/online.cgi'
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        }

    def get_cookies(self):
        res = self.session.post(self.url, headers=self.headers, data={
            't': 'КИИ, ТЭК',
            'searchPlus': '1',
            'req': 'syntax'
        })

        res = self.session.post(self.url, headers=self.headers, data={
            'req': 'query',
            'SEARCHPLUS': 'КИИ, ТЭК',
            'mode': 'splus',
            'content': 'list',
        })

        print(res.text)


if __name__ == '__main__':
    parser = Parser()
    parser.get_cookies()
