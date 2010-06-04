#!/usr/bin/python

import re
import feedparser
import locale
import htmllib
import htmlrender

def unescapeHtml(htmlText):
    p = htmllib.HTMLParser(None)
    p.save_bgn()
    p.feed(htmlText)
    return p.save_end()

def rmHtmlTags(htmlText):
    p = re.compile(r'<.*?>')
    return p.sub('', htmlText)

def htmlToSimplePlainText(htmlText):
    result = rmHtmlTags(htmlText)
    result = unescapeHtml(result)
    return result

def htmlToNicePlainText(htmlText):
    result = htmlrender.render(htmlText, 80)
    return result

def printEntry(entry):
        print "/-----------------------------------"
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
        print "\____________________________________"
    

def getFeed(url):
    result = None
    feed = feedparser.parse(url)
    if feed:
        statusText = " >>> Feed reply: %r" %feed.status
        if feed.status == 200:
            result = feed
            #all OK, continue
            print statusText
        elif feed.status == 301:
            statusText += " (feed permanently moved to %r)" %(feed.href)
            print statusText
            result = getFeed(feed.href)
        elif feed.status == 302:
            statusText += " (feed temporarily moved)"
            print statusText
            result = getFeed(feed.href)
        elif feed.status == 404:
            statusText += " (feed not found)"
            print statusText
        elif feed.status == 410:
            statusText += " (feed permanently removed)"
            print statusText
        else:
            statusText += " (unkown status %r)" %feed.status
            print statusText
    else:
        print "Got no feed."
    return result

def getEntries(url):
    feed = getFeed(url)
    if feed:
        return feed.entries
    else:
        print "Couldn't get feed."

def printFeed(url):
    entries = getEntries(url)
    if entries:
        if len(entries) > 0:
            for entry in entries:
                printEntry (entry)
                print ""
        else:
            print "Empty feed."
    else:
        print "Got no feed."

def printLastEntry(url):
    entries = getEntries(url)
    if entries:
        if len(entries) > 0:
            printEntry (entries[-1])
        else:
            print "Empty feed."


if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    app = sys.argv[0]

    type = ""
    url = ""

    if len(args) > 1:
        type = args[0]
        url =  args[1]

        if type == "all":
            printFeed(url)
        if type == "last":
            printLastEntry(url)
    else:
        print "%r: missing parameters" %app
        print "Usage: %r <all | last> URL" %app
        print ""
        print "E.g. %r last http://www.motorpasion.com/index.xml" %app
        print "E.g. %r all http://www.elcorreodigital.com/vizcaya/rss/feeds/vizcaya.xml" %app
    
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
