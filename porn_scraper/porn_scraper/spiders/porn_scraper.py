import scrapy
from ..items import PornScraperItem



class PornSpider(scrapy.Spider):
    name = "ps4"

    start_urls = [
    'http://pornhub.com/video'
    ]

    custom_settings = {
        "ITEM_PIPELINES": {'scrapy.pipelines.images.ImagesPipeline': 1},
        "IMAGES_STORE": '/Users/mac/codeland/my_work/porn-dar_whole/porn_thumbnails'
    }    # page = 1

    def parse(self, response):
        for block in response.css('div.container').css('div.videoPreviewBg'):
            psi = PornScraperItem()
            psi['image_urls'] = block.css('img::attr("data-mediumthumb")').extract()
            psi['title'] = block.css('img::attr(alt)').extract_first()
            yield psi

        next_page = response.selector.xpath('//li[@class="page_current"]/following-sibling::li[1]/a/@href').extract_first()
        if next_page is not None:
            # if we find page 1000
            if next_page.find('10') != -1:
                return
            # print('page... ' + page)
            # page = page +1
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
