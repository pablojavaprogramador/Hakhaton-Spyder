import scrapy 
from scrapy.linkextractors import LinkExtractor
from scrapy import Selector
import pandas as pd
class DmozSpider(scrapy.Spider): 
  name = "DmozSpider" 
  start_urls = [ 
    "https://omega-sun-rise.negocio.site"
   ]
  def parse(self, response):
    dataframe = pd.DataFrame()
    xlinkExtraidos = LinkExtractor()
    titulo=  response.xpath('//*[@id="details"]/div[2]/div[1]/div/ul/li').get()
    print('\n\n')
    print(f'telefono:  {titulo}')
    print('\n\n')

