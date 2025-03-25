import sys
import time
import re
import urllib.request
import winsound

# some constant values
hamal = "https://hamal.co.il"
articlePattern = r'<h2 class="styles_title__WrHVK">(.*?)</h2>'
urlPattern = r'<a class="styles_link__wjRMt" href="(.*?)">'
origArticleMatches = []
articleMatches = []
urlMatches = []

while True:
    with urllib.request.urlopen(hamal) as response:
        # get the html of the entire hamal site
        html = response.read().decode('utf-8')
        # get all the article subjects
        articleMatches = re.findall(articlePattern, html)
        # get all their urls
        urlMatches = re.findall(urlPattern, html)
        
        # only show it if there's a change in the articles
        if origArticleMatches != articleMatches:
            print("-----------------------------")
            print(time.strftime('%Y-%m-%d %H:%M:%S'))
            print("\r")
            diffs = [x for x in articleMatches if x not in origArticleMatches]
            counter = 0
            for diff in diffs:
                # makes these html chars be " or '
                diff = diff.replace("&quot;", '"').replace("&#x27;", "'")
                # show the hebrew as rtl
                print(diff[::-1])
                # print the clickable link
                print(hamal + urlMatches[counter])
                print("\r")
                counter += 1
            
            # reset the comparison lists
            origArticleMatches = articleMatches
            winsound.Beep(440, 1000)
            
        # loop every x minutes
        time.sleep(60 * int(sys.argv[1]))



