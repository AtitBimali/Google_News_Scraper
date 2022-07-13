
from requests_html import HTMLSession
import pandas as pd

Session = HTMLSession()
url = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'
data = []
result = Session.get(url)
result.html.render(sleep=4, timeout=110,keep_page=True, scrolldown=5)
content = result.html.find('article.MQsxIb.xTewfe')
for i in content:
    try:
        news = i.find('h3',first=True).text
        url = i.find('h3 a',first=True).attrs['href']
        posted_by = i.find('div.SVJrMe a',first=True).text
        posted_on = i.find('time.WW6dff.uQIVzc',first=True).text
        data.append([news,url,posted_by,posted_on])
    except:
        pass

output = pd.DataFrame(data, columns=['News','URL','News Posted By','News Posted On'])
output.to_csv('GoogleNews.csv',index=False)


