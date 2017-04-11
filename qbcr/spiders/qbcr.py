import scrapy
from ..items import QbcrItem
class qbcr(scrapy.Spider):
    name = 'qbcr'
    allowed_domains = ["www.qiubaichengren.com"]
    start_urls = ["http://www.qiubaichengren.com/1.html"]

    def parse(self, response):
        base_url = "http://www.qiubaichengren.com/{}"
        qb_item = QbcrItem()
        qb_item['img_urls'] = response.xpath("//div[@class='ui-module']/div[@class='mala-text']/p//img/@src").extract()
        page_link = response.xpath("//div[@class='page']//a[contains(text(), '下一页')]/@href").extract()
        if len(page_link)>0:
            # print(page_link, len(page_link))
            # print(base_url.format(page_link[0]))
            yield scrapy.Request(base_url.format(page_link[0]), callback=self.parse)
        else:
            print(page_link,len(page_link))
        yield qb_item
		
		
	#def parse(self, response):
		#yield scrapy.Request(url, callback=self.parse_2)
	
	#def parse_2(self, response):
		#pass