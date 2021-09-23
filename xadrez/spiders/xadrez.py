import scrapy

#acessar o pontodoxadrez.com e pegar nome, preço e link de todas as peças de xadrez do site
class XadrezSpyder(scrapy.Spider):
    name = 'xadrez'

    start_urls = ['https://www.pontodoxadrez.com.br/pecas-xadrez?page=4']


    def parse(self, response):
        
        for pecas in response.xpath('//*[@id="comp-jdad2416"]/div/div/div/div/section/div/ul/li'):
            nome = pecas.xpath('.//div/a/div[2]/h3//text()').extract_first()
            preco = pecas.xpath('.//div/a/div/div/span[4]//text()').extract_first()
            link = pecas.xpath('.//a/@href').extract_first()

            yield {
                'nome': nome,
                'preco': preco,
                'link': link
            }