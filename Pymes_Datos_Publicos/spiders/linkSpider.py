import scrapy 
from scrapy.linkextractors import LinkExtractor
from scrapy import Selector

import pandas as pd


class linkSpider(scrapy.Spider): 
  name = "links" 
  start_urls = [ 
    "https://omega-sun-rise.negocio.site"
   ]
  def parse(self, response):
    dataframe = pd.DataFrame()
    xlinkExtraidos = LinkExtractor()
    link_lista=[]
    link_texto=[]
    divs = response.xpath('//div')
    texto_lista=[]
    for span in divs.xpath('text()'):
      if len(str(span.get()))>100:
        texto_lista.append(span.get())
    for link in xlinkExtraidos.extract_links(response):
      if len(str(link))>200 or 'Journal'in link.text:
        #print(len(str(link)),link.text,link,"\n")'''
        link_lista.append(link)
        link_texto.append(link.text)
    for i in range(len(link_texto)-len(texto_lista)):
      texto_lista.append(" ")
    dataframe['links']=link_lista
    dataframe['link_text']=link_texto
    dataframe['text_meta'] = texto_lista
    dataframe.to_csv('linksEncontrados.csv')
