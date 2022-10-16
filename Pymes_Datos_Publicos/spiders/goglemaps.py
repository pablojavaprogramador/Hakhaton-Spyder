import scrapy

class GoogleMapas(scrapy.Spider):
    name='quotes'
    start_urls=['https://www.google.com.mx/maps']

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