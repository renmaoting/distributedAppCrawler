# distributedAppCrawler

This is a distributed App crawler, it will grabs all the App informations from Google Play, including: 
  
  1. App name           6. type 
  2. author             7. update time 
  3. rating             8. download number
  4. price              9. review number
  5. version            10. URL

then store datas into mongodb

Use scrapy-redis + mongodb.

usage: scrapy crawl App -o items.json -t json

necessary package installation:

install Python-pip: sudo apt-get install python-pip
install scrapy: sudo pip install scrapy
install mongodb: sudo apt-get install mongodb
install pymongo: sudo pip install pymongo
linux install mongochef which is a GUI tool:

download http://3t.io/mongochef/download/core/platform/#tab-id-3
tar -xvzf mongochef-linux-x64-dist.tar.gz
./mongochef-4.4.2-linux-x64-dist/bin/mongochef.sh
