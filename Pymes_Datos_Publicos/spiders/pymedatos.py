import scrapy

class PymesSpider(scrapy.Spider):
    name='pymes'
    start_urls=['https://pinata2go.mx']

    def parse(self,response):
        print('*'*10)
        print('\n\n')
        titulo=response.xpath('/html/head/title').get()
        print(f'Titulo:  {titulo}')
        print('\n\n')
        print(response)
        print(response.status,response.headers)
        print('*'*10)
        print('\n\n')
        print('*'*10)