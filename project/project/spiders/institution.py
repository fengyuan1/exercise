import scrapy
from project.items import ProjectItem
from scrapy.http import Request
import json

class MaoyanSprider(scrapy.Spider):
    name = 'institution'
    start_urls = ['http://gd.zgsydw.com/zhaopin/2.html']

    def parse(self, response):
        # print(response.text)
        # print(response.css('.gg_conl_ul').extract())
        for item in response.css('.gg_conl_ul li'):
            title = item.css('.this_title b::text').extract()
            href=item.css('a::attr(href)').extract()
            # print(href[0])

            yield Request(href[0], callback=self.parse_new_page)


    def parse_new_page(self, response):
        # print(response.text)
        link_address='';
        content_word='';
        title=response.css('.show_con_title ::text').extract()[0]
        data=response.css('.show_con_info em:nth-child(1)::text').extract()[0][-19:-1]
        extence=response.css('.show_con_info em:nth-child(3)::text').extract()[0]
        content=response.css('.show_con_box p::text').extract()
        link=response.css('.show_con_box a[href^="http"]::attr(href) ').extract()
        for link_item in link:
            if link_item.find(".doc")!= -1 or link_item.find(".xls")!=-1 or link_item.find(".xlsx")!= -1:
                link_address=link_address+link_item+';'
        for content_item in content:
            if content_item.find("报名方式")!=-1 or content_item.find("应聘方法")!=-1 or content_item.find("报名时间")!=-1 or content_item.find("资格条件")!=-1:
                content_word=content_word+content_item+'   :'

        item=ProjectItem()
        item['title']=title
        item['data']=data
        item['extence'] = extence
        item['content'] = content_word
        item['link'] = link_address

        yield item