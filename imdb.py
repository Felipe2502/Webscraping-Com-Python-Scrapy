import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/pt/chart/top/?ref_=nv_mv_250']

    def parse(self, response):
        for filmes in response.css('.ipc-metadata-list-summary-item', '.ipc-title__text'):
            yield{
                 'titulo': filmes.css('.ipc-metadata-list-summary-item::text').get(),
                 'ano':  filmes.css('.ipc-inline-list__item ::text').get()[1:-1],
                 'nota':  response.css('strong::text').get()
            }

        pass