# coding=utf-8这样
import urllib.request as ur
import urllib.error as urerror
import sys
import re
import xlwt
from bs4 import BeautifulSoup

# 正则表达式
findLink = re.compile(r'<a href="(.*?)">')
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
findTitle = re.compile(r'<span class="title">(.*)</span>')  # 片名
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')  # 评分
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')  # 概况
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)  # 相关内容


# 得到页面内容
def askURL(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    request = ur.Request(url, headers=headers)
    response = ur.urlopen(request)
    html = response.read()
    # print(html)
    return html


def saveData(dataList, savepath):
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('豆瓣电影top250', cell_overwrite_ok=True)
    col = ('电影详情链接', '图片链接', '影片中文名', '影片外国名', '影片评分', '评价数', '概况', '相关信息')
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        data = dataList[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)


def main():
    dataList = []
    for i in range(11):
        html = askURL('https://movie.douban.com/top250?start=' + str(i * 25) + '&filter=')
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_='item'):
            data = []
            item = str(item)
            # 影片详情链接：
            link = re.findall(findLink, item)[0]
            data.append(link)

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle, item)[0]
            # 只要中文名
            if len(titles) == 2:
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(" ")

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)  # 添加评论人数
            inq = re.findall(findInq, item)
            # 可能没有概况
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd, item)[0]
            data.append(bd)
            dataList.append(data)
    # 保存
    savepath = "D:\编程\Python\codes\douban\豆瓣电影.xls"
    saveData(dataList, savepath)


if __name__ == "__main__":
    main()
