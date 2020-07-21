# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# 爬取到的数据写入到MySQL数据库
import pymysql
import time

class ProjectPipeline(object):
    def __init__(self):
        # 连接MySQL数据库
        self.connect=pymysql.connect(host='localhost',user='root',password='root',db='movie',port=3306)
        self.cursor=self.connect.cursor()
    def process_item(self, item, spider):

        # 查询数据库是否有这个数据
        self.cursor.execute('select * from institution where title= "{}"'.format(item['title']))
        result = self.cursor.fetchone()
        # print(result)
        # 往数据库里面写入数据
        if result == None:
            self.cursor.execute('insert into institution(title,data,extence,content,link_address,create_time)VALUES ("{}","{}","{}","{}","{}","{}")'.format(item['title'],item['data'],item['extence'],item['content'],item['link'],time.time()))
            self.connect.commit()
            return item
    # 关闭数据库
    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()
