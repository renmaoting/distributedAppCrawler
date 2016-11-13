# distributedAppCrawler

This is a distributed App crawler, it will grabs all the App informations from Google Play, including: 
  
  * App name 
  * type 
  * author 
  * update time 
  * rating 
  * download number
  * price 
  * view number
  * version 
  * URL

then store datas into mongodb

Use scrapy-redis + mongodb.

usage: scrapy crawl App -o items.json -t json

necessary package installation:

1. install Python-pip: sudo apt-get install python-pip
2. install scrapy: sudo pip install scrapy
3. install mongodb: sudo apt-get install mongodb
4. install pymongo: sudo pip install pymongo
5. linux install mongochef which is a GUI tool:

install mongochef which is a GUI tool:

1. download http://3t.io/mongochef/download/core/platform/#tab-id-3
2. tar -xvzf mongochef-linux-x64-dist.tar.gz
3. ./mongochef-4.4.2-linux-x64-dist/bin/mongochef.sh
