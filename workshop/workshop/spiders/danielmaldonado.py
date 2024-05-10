import scrapy


class DanielmaldonadoSpider(scrapy.Spider):
    name = "danielmaldonado"
    allowed_domains = ["danielmaldonado.com.ar"]
    start_urls = ["https://danielmaldonado.com.ar/blog"]

    def parse(self, response):
        enlaces = response.css("h2 > a::attr(href)").extract()
        for url in enlaces:
            yield(scrapy.Request(url, self.parser_noticia))

    def parser_noticia(self, response):
        titulo = response.css("h1::text").extract()
        contenido = response.css(".entry-content > p").extract()
        fecha = response.css("time.entry-date::attr(datetime)").extract()
        autor = response.css("h4 > a > strong::text").extract()
        print(titulo, "|", contenido, "|", fecha, "|", autor)
