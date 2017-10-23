# coding=utf-8
import urllib2
import datetime

import sys
from bs4 import BeautifulSoup



class HtmlPaser(object):
    def parse(self, ssdPath,html_cont, setName, modelName):
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding="utf-8")
        print "获取\n"
        links = soup.find_all('div')
        links = links[1:len(links)]
        count = 0
        setSize = 0.0
        for link in links:
            restoflinks = len(links) - count

            response = urllib2.urlopen(link['data-image_url'])

            #读取html时间
            timeHtmlReadS = datetime.datetime.now()
            data = response.read()
            timeHtmlReadE = datetime.datetime.now()

            filename = ssdPath + str(count) + ".jpg"
            f = open(filename, 'wb')
            f.write(data)
            f.close()

            photoSize = round((float(sys.getsizeof(data)))/1024/1024, 2)
            HtmlDataTime = (timeHtmlReadE - timeHtmlReadS).seconds
            if HtmlDataTime == 0:
                HtmlDataTime = 1
            photoDownSpeed = round(float(photoSize/HtmlDataTime),2)

            HtmlDataTimeStrControl = (str(HtmlDataTime)+"s ")[0:2]
            setNameStrControl = (setName+"》                                       ")[0:35]
            modelNameStrControl = (modelName+"               ")[0:10]
            restoflinksStrControl = (str(restoflinks - 1) + "  ")[0:2]

            print "Set: 《"+setNameStrControl+"                Model: "+modelNameStrControl+"      HtmlData: "+HtmlDataTimeStrControl+"            photoSize: "+(str(photoSize)+" ")[0:4]+"M"+" ("+(str(photoDownSpeed)+" ")[0:4]+" M/s)      "+restoflinksStrControl + " photos remains\n"

            setSize = setSize + photoSize
            count = count + 1
        timeEnd = datetime.datetime.now()
        return len(links), timeEnd, setSize