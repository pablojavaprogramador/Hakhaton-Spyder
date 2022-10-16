import scrapy
import pandas as pd
from . import utils

class SpiderGobierno(scrapy.Spider):
    name='quotes'
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
        for link in response.xpath('//h3/a'):
            url = link.xpath('.//@href').get()
            final_url = self.base_url + url.replace('../..', '')
            yield {
                "link": final_url
            }
        print(link)    
        print('*'*10)