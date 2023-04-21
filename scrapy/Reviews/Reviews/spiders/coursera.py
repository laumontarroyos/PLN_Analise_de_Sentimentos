# -*- coding: utf-8 -*-

# Programa para recuperar os dados de comentários com as estrelas de
# pontuação correspondentes diretamente do site da 'Coursera'
# autor: Laureano L. Montarroyos Fo
# data: março/2023
# linha de comando para executar este spider: scrapy runspider Reviews/Reviews/spiders/coursera.py -o coursera.csv

import scrapy


class Coursera(scrapy.Spider):
    name = "Coursera"

    myBaseUrl = 'https://www.coursera.org/learn/nlp-sequence-models/reviews?page='
    start_urls=[]
    pagina = 1
    indice = 1

    # Creating list of urls to be scraped by appending page number at the end of base url
    for i in range(1,141):
        start_urls.append(myBaseUrl+str(i))

    def parse(self, response):
        
        for review in response.xpath('//div[@class="cds-9 css-1ktinjm cds-11 cds-grid-item cds-80"]'):
        	comentario = review.xpath('.//div[@class="css-18w79dz"]/p/span/span/text()').get()
        
        	estrelas=''
        	for titulo in review.xpath('.//title'):
        		aux = titulo.xpath('.//text()').get()
        		estrelas = estrelas + aux + ":"
        	#estrela= estrela + '"'

        	        	
        	yield {
                	'indice': self.indice,
                	'estrelas': estrelas,
                	'comentario': comentario
        	}
        	self.indice = self.indice +1
        self.pagina = self.pagina +1
        if(self.pagina<141):
        	yield scrapy.Request(response.urljoin(self.myBaseUrl+str(self.pagina)))
        	#pass



