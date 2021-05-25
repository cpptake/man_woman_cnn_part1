from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time , sys

#APIキーの情報

key="write your Key numbers"
secret = "secret key"
wait_time = 1

#保存フォルダの指定
search_name = sys.argv[1]
savedir = "./" + search_name

flickr = FlickrAPI(key,secret,format = 'parsed-json')
result = flickr.photos.search(
    text = search_name,
    per_page = 400,
    media ='photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence'
)

photos = result['photos']
#pprint(photos)


for i,photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id']+'.jpg'
    if  os.path.exists(filepath):continue
    urlretrieve(url_q,filepath)
    time.sleep(wait_time)

print("done.")
