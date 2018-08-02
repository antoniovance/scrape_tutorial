import scrapy
from scrapy_tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        "http://www.vogue.com.cn"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
    def parse(self, response):
        for sel in response.xpath('//img'):
            img_link = sel.xpath('@src').extract()[0]
            img_link = img_link[2:] if img_link[:2] == '//' else img_link
            title = sel.xpath('@title').extract()
            title = list(title)[0] if len(list(title))>0 else ''
            alt = sel.xpath('@alt').extract()
            alt = list(alt)[0] if len(list(alt))>0 else ''
            #print('img_link: {}, title: {}, alt: {}'.format(img_link, title, alt))
            if alt and title:
                item = DmozItem()
                item['title'] = title
                item['link'] = img_link
                item['desc'] = alt
                yield item
