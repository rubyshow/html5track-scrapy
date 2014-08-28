# -*- coding: utf-8 -*-

# Scrapy settings for html5track project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import sys
import MySQLdb

BOT_NAME = 'html5track'

SPIDER_MODULES = ['html5track.spiders']
NEWSPIDER_MODULE = 'html5track.spiders'



ITEM_PIPELINES = [
    'html5track.pipelines.articleCheckPipeline'
    ]
            
       

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'html5track (+http://www.yourdomain.com)'

#mysql config
SQL_DB = 'wordpress'
SQL_HOST = '192.168.1.237'
SQL_USER = 'fb'
SQL_PASSWORD = '123'

#redis config
REDIS_SERVER = 'localhost'
REDIS_PORT = '6637'
REDIS_KEY_FORMAT = 'html5track:'

#connect mysql
try:
  CONN = MySQLdb.connect(host=SQL_HOST,user=SQL_USER,passwd=SQL_PASSWORD,db=SQL_DB)
except MySQLdb.Error, e:
    print " ERROR %d : %s "% (e.args[0], e.args[1])
    sys.exit(1)
