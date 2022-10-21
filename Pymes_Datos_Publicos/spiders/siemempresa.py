import scrapy

class SiemEmpresas(scrapy.Spider):
    name='siem'
    start_urls=['https://siem.economia.gob.mx']

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