import scrapy 
from scrapy.linkextractors import LinkExtractor
from scrapy import Selector

import pandas as pd

class PymesSpider(scrapy.Spider):
    name = "pymes"
    start_urls = [
        "https://www.google.com.mx/search?q=scrapy+obtener+direccion&sxsrf=ALiCzsb-JnJmpkDN33_qs1WfnWBq_-9_PA%3A1666503608388&source=hp&ei=uNNUY9GiFKGxqtsPqaO3yAM&iflsig=AJiK0e8AAAAAY1ThyIGDa_rSsOPuCLfG32V1yr8tNIp2&ved=0ahUKEwjR3t3c0fX6AhWhmGoFHanRDTkQ4dUDCAg&uact=5&oq=scrapy+obtener+direccion&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABMgUIIRCgATIFCCEQoAE6BAgjECc6BggjECcQEzoECAAQQzoQCC4QsQMQgwEQxwEQ0QMQQzoKCAAQsQMQgwEQQzoOCC4QgAQQsQMQxwEQ0QM6BwgAELEDEEM6CwguEIAEELEDEIMBOhEILhCABBCxAxCDARDHARDRAzoLCAAQgAQQsQMQgwE6CAgAEIAEELEDOgoIABCABBCHAhAUOg0IABCABBCxAxCDARAKOgoIABCABBCxAxAKOgcIABCABBAKOgUIABCABDoQCC4QgAQQxwEQrwEQ1AIQCjoICAAQgAQQywE6BggAEBYQHjoICAAQFhAeEA86BAghEBVQAFjtHmD9H2gAcAB4AIABiAGIAaQTkgEFMTAuMTSYAQCgAQE&sclient=gws-wiz"
    ]

    def parse(self, response):
        dataframe = pd.DataFrame()
        xlinkExtraidos = LinkExtractor()
        link_lista = []
        link_texto = []
        divs = response.xpath('//div')
        texto_lista = []
        for span in divs.xpath('text()'):
            if len(str(span.get())) > 100:
                texto_lista.append(span.get())


        for link in xlinkExtraidos.extract_links(response):
            if len(str(link)) > 200 or 'Journal' in link.text:
                # print(len(str(link)),link.text,link,"\n")'''
                link_lista.append(link)
                link_texto.append(link.text)
        for i in range(len(link_texto)-len(texto_lista)):
            texto_lista.append(" ")
        dataframe['links'] = link_lista
        dataframe['link_text'] = link_texto
        dataframe['text_meta'] = texto_lista
        dataframe.to_csv('datosEmpresas.csv')
