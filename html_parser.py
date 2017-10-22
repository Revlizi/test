# coding=utf-8
import urllib2
import datetime
from bs4 import BeautifulSoup



class HtmlPaser(object):
    def parse(self, ssdPath,html_cont, setName, modelName):
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding="utf-8")
        print "获取\n"
        links = soup.find_all('div')
        links = links[1:len(links)-1]
        count = 0
        for link in links:
            restoflinks = len(links) - count
            print link['data-image_url'] + "  " + str(restoflinks) + " photos remains"

            #打开url时间
            timeUrlOpenS = datetime.datetime.now()
            response = urllib2.urlopen(link['data-image_url'])
            timeUrlOpenE = datetime.datetime.now()

            #读取html时间
            timeHtmlReadS = datetime.datetime.now()
            data = response.read()
            timeHtmlReadE = datetime.datetime.now()

            #图片保存操作时间
            timePhotoSaveS = datetime.datetime.now()
            filename = ssdPath + str(count) + ".jpg"
            f = open(filename, 'wb')
            f.write(data)
            f.close()
            timePhotoSaveE = datetime.datetime.now()

            print "UrlOpen: "+str((timeUrlOpenE-timeUrlOpenS).seconds)+"s --->HtmlData: "+str((timeHtmlReadE-timeHtmlReadS).seconds)+"s --->PhotoSave: "+str((timePhotoSaveE-timePhotoSaveS).seconds)+"s                                                            Set: 《"+setName+"》    Model: "+modelName+"\n"

            count = count + 1
        timeEnd = datetime.datetime.now()
        return len(links), timeEnd