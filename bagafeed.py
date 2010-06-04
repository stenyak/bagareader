#!/usr/bin/python

import re
import feedparser
import locale
import htmllib
import htmlrender

def unescapeHtml(text):
    p = htmllib.HTMLParser(None)
    p.save_bgn()
    p.feed(text)
    return p.save_end()

def rmHtmlTags(text):
    p = re.compile(r'<.*?>')
    return p.sub('', text)

def htmlToSimplePlainText(htmlText):
    result = rmHtmlTags(htmlText)
    result = unescapeHtml(result)
    return result

def htmlToNicePlainText(htmlText):
    result = htmlrender.render(htmlText, 80)
    return result

def printEntry(entry):
        print "/-----------------------------------\\"
        title = ""
        content = ""

        if "title" in entry:
            title += entry["title"]

        if "author" in entry:
            title += " (by %r)" %entry["author"]

        if "summary" in entry:
            summary = entry["summary"]
            #summary = htmlToSimplePlainText(summary)
            summary = htmlToNicePlainText(summary)
            content += summary

        if "id" in entry:
            content += "\n"
            content += "[id:%r]" %entry["id"]

        print title
        print content
        print "\____________________________________/"
    
def getEntries(url):
    feed = feedparser.parse(url)
    return feed.entries

def printFeed(url):
    for entry in getEntries(url):
        printEntry (entry)
        print ""

def printLastEntry(url):
    printEntry (getEntries(url)[-1])


#printFeed ("http://www.motorpasion.com/index.xml")
printLastEntry ("http://www.elcorreodigital.com/vizcaya/rss/feeds/vizcaya.xml")

"""
---------------
------'author':	''
------'guidislink':	''
------'id':	''
------'link':	''
------'links':	''
------'title':	''
------'title_detail':	''
------'summary':	''
------'summary_detail':	''
------'updated':	''
------'updated_parsed':	''
"""
