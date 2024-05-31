# coding=utf-8
# !/usr/bin/python

import requests
from bs4 import BeautifulSoup
import re
from base.spider import Spider
import sys
sys.path.append('..')
xurl = "https://www.keke6.app"
headerx = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'
}
pm=''

class Spider(Spider):
    global xurl
    global headerx

    def getName(self):
        return "首页"

    def init(self, extend):
        pass

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def fl(self,key):
        videos = []
        doc = BeautifulSoup(key, "html.parser")
        soups = doc.find('div', class_="section-main fs-margin-top")
        soup = soups.find_all('div', class_="module-item")
        for vod in soup:
            name = vod.select_one("a div div img")['alt']
            id = xurl + vod.select_one("a")["href"]
            pic = 'https://vres.miximixi.me' + vod.select_one("a div div img")['data-original']
            remark = vod.select_one("a div div span")
            remark = remark.get_text(strip=True) if remark is not None else ""

            video = {
                "vod_id": id,
                "vod_name": name,
                "vod_pic": pic,
                "vod_remarks": remark
            }
            videos.append(video)
        return videos

    def homeContent(self, filter):
        result = {}
        result = {"class":[{"type_id":"1","type_name":"电影"},{"type_id":"2","type_name":"电视剧"},{"type_id":"4","type_name":"综艺"},{"type_id":"3","type_name":"动漫"},{"type_id":"6","type_name":"短剧"}],"list":[],"filters":{"1":[{"key":"类型","name":"类型","value":[{"n":"全部","v":""},{"n":"Netflix","v":"NETFLIX"},{"n":"剧情","v":"剧情"},{"n":"喜剧","v":"喜剧"},{"n":"动作","v":"动作"},{"n":"爱情","v":"爱情"},{"n":"恐怖","v":"恐怖"},{"n":"惊悚","v":"惊悚"},{"n":"犯罪","v":"犯罪"},{"n":"科幻","v":"科幻"},{"n":"悬疑","v":"悬疑"},{"n":"奇幻","v":"奇幻"},{"n":"冒险","v":"冒险"},{"n":"战争","v":"战争"},{"n":"历史","v":"历史"},{"n":"古装","v":"古装"},{"n":"家庭","v":"家庭"},{"n":"传记","v":"传记"},{"n":"武侠","v":"武侠"},{"n":"歌舞","v":"歌舞"},{"n":"短片","v":"短片"},{"n":"动画","v":"动画"},{"n":"儿童","v":"儿童"},{"n":"职场","v":"职场"}]},{"key":"地区","name":"地区","value":[{"n":"全部","v":""},{"n":"大陆","v":"中国大陆"},{"n":"香港","v":"中国香港"},{"n":"台湾","v":"中国台湾"},{"n":"美国","v":"美国"},{"n":"日本","v":"日本"},{"n":"韩国","v":"韩国"},{"n":"英国","v":"英国"},{"n":"法国","v":"法国"},{"n":"德国","v":"德国"},{"n":"印度","v":"印度"},{"n":"泰国","v":"泰国"},{"n":"丹麦","v":"丹麦"},{"n":"瑞典","v":"瑞典"},{"n":"巴西","v":"巴西"},{"n":"加拿大","v":"加拿大"},{"n":"俄罗斯","v":"俄罗斯"},{"n":"意大利","v":"意大利"},{"n":"比利时","v":"比利时"},{"n":"爱尔兰","v":"爱尔兰"},{"n":"西班牙","v":"西班牙"},{"n":"澳大利亚","v":"澳大利亚"},{"n":"其他","v":"其他"}]},{"key":"语言","name":"语言","value":[{"n":"全部","v":""},{"n":"国语","v":"国语"},{"n":"粤语","v":"粤语"},{"n":"英语","v":"英语"},{"n":"日语","v":"日语"},{"n":"韩语","v":"韩语"},{"n":"法语","v":"法语"},{"n":"其他","v":"其他"}]},{"key":"年份","name":"年份","value":[{"n":"全部","v":""},{"n":"2024","v":"2024"},{"n":"2023","v":"2023"},{"n":"2022","v":"2022"},{"n":"2021","v":"2021"},{"n":"2020","v":"2020"},{"n":"2019","v":"2019"},{"n":"2018","v":"2018"},{"n":"2017","v":"2017"},{"n":"2016","v":"2016"},{"n":"2015","v":"2015"},{"n":"2014","v":"2014"},{"n":"2013","v":"2013"},{"n":"2012","v":"2012"},{"n":"2011","v":"2011"},{"n":"2010","v":"2010"},{"n":"2000年代","v":"2000_2009"},{"n":"90年代","v":"1990_1999"},{"n":"80年代","v":"1980_1989"},{"n":"70年代","v":"1970_1979"},{"n":"60年代","v":"1960_1969"},{"n":"更早","v":"0_1959"}]},{"key":"排序","name":"排序","value":[{"n":"综合","v":"1"},{"n":"最新","v":"2"},{"n":"最热","v":"3"},{"n":"评分","v":"4"}]}],"2":[{"key":"类型","name":"类型","value":[{"n":"全部","v":""},{"n":"Netflix","v":"NETFLIX"},{"n":"剧情","v":"剧情"},{"n":"喜剧","v":"喜剧"},{"n":"动作","v":"动作"},{"n":"爱情","v":"爱情"},{"n":"恐怖","v":"恐怖"},{"n":"惊悚","v":"惊悚"},{"n":"犯罪","v":"犯罪"},{"n":"科幻","v":"科幻"},{"n":"悬疑","v":"悬疑"},{"n":"奇幻","v":"奇幻"},{"n":"冒险","v":"冒险"},{"n":"战争","v":"战争"},{"n":"历史","v":"历史"},{"n":"古装","v":"古装"},{"n":"家庭","v":"家庭"},{"n":"传记","v":"传记"},{"n":"武侠","v":"武侠"},{"n":"歌舞","v":"歌舞"},{"n":"短片","v":"短片"},{"n":"动画","v":"动画"},{"n":"儿童","v":"儿童"},{"n":"职场","v":"职场"}]},{"key":"地区","name":"地区","value":[{"n":"全部","v":""},{"n":"大陆","v":"中国大陆"},{"n":"香港","v":"中国香港"},{"n":"台湾","v":"中国台湾"},{"n":"美国","v":"美国"},{"n":"日本","v":"日本"},{"n":"韩国","v":"韩国"},{"n":"英国","v":"英国"},{"n":"法国","v":"法国"},{"n":"德国","v":"德国"},{"n":"印度","v":"印度"},{"n":"泰国","v":"泰国"},{"n":"丹麦","v":"丹麦"},{"n":"瑞典","v":"瑞典"},{"n":"巴西","v":"巴西"},{"n":"加拿大","v":"加拿大"},{"n":"俄罗斯","v":"俄罗斯"},{"n":"意大利","v":"意大利"},{"n":"比利时","v":"比利时"},{"n":"爱尔兰","v":"爱尔兰"},{"n":"西班牙","v":"西班牙"},{"n":"澳大利亚","v":"澳大利亚"},{"n":"其他","v":"其他"}]},{"key":"语言","name":"语言","value":[{"n":"全部","v":""},{"n":"国语","v":"国语"},{"n":"粤语","v":"粤语"},{"n":"英语","v":"英语"},{"n":"日语","v":"日语"},{"n":"韩语","v":"韩语"},{"n":"法语","v":"法语"},{"n":"其他","v":"其他"}]},{"key":"年份","name":"年份","value":[{"n":"全部","v":""},{"n":"2024","v":"2024"},{"n":"2023","v":"2023"},{"n":"2022","v":"2022"},{"n":"2021","v":"2021"},{"n":"2020","v":"2020"},{"n":"2019","v":"2019"},{"n":"2018","v":"2018"},{"n":"2017","v":"2017"},{"n":"2016","v":"2016"},{"n":"2015","v":"2015"},{"n":"2014","v":"2014"},{"n":"2013","v":"2013"},{"n":"2012","v":"2012"},{"n":"2011","v":"2011"},{"n":"2010","v":"2010"},{"n":"2000年代","v":"2000_2009"},{"n":"90年代","v":"1990_1999"},{"n":"80年代","v":"1980_1989"},{"n":"70年代","v":"1970_1979"},{"n":"60年代","v":"1960_1969"},{"n":"更早","v":"0_1959"}]},{"key":"排序","name":"排序","value":[{"n":"综合","v":"1"},{"n":"最新","v":"2"},{"n":"最热","v":"3"},{"n":"评分","v":"4"}]}],"3":[{"key":"类型","name":"类型","value":[{"n":"全部","v":""},{"n":"Netflix","v":"NETFLIX"},{"n":"动态漫画","v":"动态漫画"},{"n":"剧情","v":"剧情"},{"n":"动画","v":"动画"},{"n":"喜剧","v":"喜剧"},{"n":"冒险","v":"冒险"},{"n":"动作","v":"动作"},{"n":"奇幻","v":"奇幻"},{"n":"科幻","v":"科幻"},{"n":"儿童","v":"儿童"},{"n":"搞笑","v":"搞笑"},{"n":"爱情","v":"爱情"},{"n":"家庭","v":"家庭"},{"n":"短片","v":"短片"},{"n":"热血","v":"热血"},{"n":"益智","v":"益智"},{"n":"悬疑","v":"悬疑"},{"n":"经典","v":"经典"},{"n":"校园","v":"校园"},{"n":"Anime","v":"Anime"},{"n":"运动","v":"运动"},{"n":"亲子","v":"亲子"},{"n":"青春","v":"青春"},{"n":"恋爱","v":"恋爱"},{"n":"武侠","v":"武侠"},{"n":"惊悚","v":"惊悚"}]},{"key":"地区","name":"地区","value":[{"n":"全部","v":""},{"n":"大陆","v":"中国大陆"},{"n":"香港","v":"中国香港"},{"n":"台湾","v":"中国台湾"},{"n":"美国","v":"美国"},{"n":"日本","v":"日本"},{"n":"韩国","v":"韩国"},{"n":"英国","v":"英国"},{"n":"法国","v":"法国"},{"n":"德国","v":"德国"},{"n":"印度","v":"印度"},{"n":"泰国","v":"泰国"},{"n":"丹麦","v":"丹麦"},{"n":"瑞典","v":"瑞典"},{"n":"巴西","v":"巴西"},{"n":"加拿大","v":"加拿大"},{"n":"俄罗斯","v":"俄罗斯"},{"n":"意大利","v":"意大利"},{"n":"比利时","v":"比利时"},{"n":"爱尔兰","v":"爱尔兰"},{"n":"西班牙","v":"西班牙"},{"n":"澳大利亚","v":"澳大利亚"},{"n":"其他","v":"其他"}]},{"key":"语言","name":"语言","value":[{"n":"全部","v":""},{"n":"国语","v":"国语"},{"n":"粤语","v":"粤语"},{"n":"英语","v":"英语"},{"n":"日语","v":"日语"},{"n":"韩语","v":"韩语"},{"n":"法语","v":"法语"},{"n":"其他","v":"其他"}]},{"key":"年份","name":"年份","value":[{"n":"全部","v":""},{"n":"2024","v":"2024"},{"n":"2023","v":"2023"},{"n":"2022","v":"2022"},{"n":"2021","v":"2021"},{"n":"2020","v":"2020"},{"n":"2019","v":"2019"},{"n":"2018","v":"2018"},{"n":"2017","v":"2017"},{"n":"2016","v":"2016"},{"n":"2015","v":"2015"},{"n":"2014","v":"2014"},{"n":"2013","v":"2013"},{"n":"2012","v":"2012"},{"n":"2011","v":"2011"},{"n":"2010","v":"2010"},{"n":"2000年代","v":"2000_2009"},{"n":"90年代","v":"1990_1999"},{"n":"80年代","v":"1980_1989"},{"n":"70年代","v":"1970_1979"},{"n":"60年代","v":"1960_1969"},{"n":"更早","v":"0_1959"}]},{"key":"排序","name":"排序","value":[{"n":"综合","v":"1"},{"n":"最新","v":"2"},{"n":"最热","v":"3"},{"n":"评分","v":"4"}]}],"4":[{"key":"类型","name":"类型","value":[{"n":"全部","v":""},{"n":"纪录","v":"纪录"},{"n":"真人秀","v":"真人秀"},{"n":"脱口秀","v":"脱口秀"},{"n":"剧情","v":"剧情"},{"n":"历史","v":"历史"},{"n":"喜剧","v":"喜剧"},{"n":"传记","v":"传记"},{"n":"相声","v":"相声"},{"n":"节目","v":"节目"},{"n":"歌舞","v":"歌舞"},{"n":"冒险","v":"冒险"},{"n":"运动","v":"运动"},{"n":"犯罪","v":"犯罪"},{"n":"短片","v":"短片"},{"n":"搞笑","v":"搞笑"},{"n":"晚会","v":"晚会"}]},{"key":"地区","name":"地区","value":[{"n":"全部","v":""},{"n":"大陆","v":"中国大陆"},{"n":"香港","v":"中国香港"},{"n":"台湾","v":"中国台湾"},{"n":"美国","v":"美国"},{"n":"日本","v":"日本"},{"n":"韩国","v":"韩国"},{"n":"其他","v":"其他"}]},{"key":"语言","name":"语言","value":[{"n":"全部","v":""},{"n":"国语","v":"国语"},{"n":"粤语","v":"粤语"},{"n":"英语","v":"英语"},{"n":"日语","v":"日语"},{"n":"韩语","v":"韩语"},{"n":"法语","v":"法语"},{"n":"其他","v":"其他"}]},{"key":"年份","name":"年份","value":[{"n":"全部","v":""},{"n":"2024","v":"2024"},{"n":"2023","v":"2023"},{"n":"2022","v":"2022"},{"n":"2021","v":"2021"},{"n":"2020","v":"2020"},{"n":"2019","v":"2019"},{"n":"2018","v":"2018"},{"n":"2017","v":"2017"},{"n":"2016","v":"2016"},{"n":"2015","v":"2015"},{"n":"2014","v":"2014"},{"n":"2013","v":"2013"},{"n":"2012","v":"2012"},{"n":"2011","v":"2011"},{"n":"2010","v":"2010"},{"n":"2000年代","v":"2000_2009"},{"n":"90年代","v":"1990_1999"},{"n":"80年代","v":"1980_1989"},{"n":"70年代","v":"1970_1979"},{"n":"60年代","v":"1960_1969"},{"n":"更早","v":"0_1959"}]},{"key":"排序","name":"排序","value":[{"n":"综合","v":"1"},{"n":"最新","v":"2"},{"n":"最热","v":"3"},{"n":"评分","v":"4"}]}],"6":[{"key":"类型","name":"类型","value":[{"n":"全部","v":""},{"n":"逆袭","v":"逆袭"},{"n":"甜宠","v":"甜宠"},{"n":"虐恋","v":"虐恋"},{"n":"穿越","v":"穿越"},{"n":"重生","v":"重生"},{"n":"剧情","v":"剧情"},{"n":"科幻","v":"科幻"},{"n":"武侠","v":"武侠"},{"n":"爱情","v":"爱情"},{"n":"动作","v":"动作"},{"n":"战争","v":"战争"},{"n":"冒险","v":"冒险"},{"n":"其他","v":"其他"}]},{"key":"排序","name":"排序","value":[{"n":"综合","v":"1"},{"n":"最新","v":"2"},{"n":"最热","v":"3"}]}]}}
        result['class'].append({'type_id': '/topic/detail/1-', 'type_name': '豆瓣电影 Top 250'})
        result['class'].append({'type_id': '/topic/detail/460-', 'type_name': '豆瓣2023年度度榜单'})
        result['class'].append({'type_id': '/topic/detail/3-', 'type_name': '抖音“毒舌电影”推荐'})
        result['class'].append({'type_id': '/topic/detail/13-', 'type_name': '冷门佳片推荐'})
        result['class'].append({'type_id': '/topic/detail/461-', 'type_name': 'Netflix高分'})
        result['class'].append({'type_id': '/topic/detail/458-', 'type_name': 'Netflix韩剧'})
        result['class'].append({'type_id': '/topic/detail/457-', 'type_name': 'Netflix动漫'})
        result['class'].append({'type_id': '/topic/detail/464-', 'type_name': 'Netflix日剧'})
        result['class'].append({'type_id': '/topic/detail/462-', 'type_name': 'Netflix泰剧'})
        result['class'].append({'type_id': '/topic/detail/524-', 'type_name': '日漫2024年4月新番'})
        return result

    def homeVideoContent(self):
        try:
            detail = requests.get(url=xurl + '/topic/detail/15-1.html', headers=headerx)
            detail.encoding = "utf-8"
            res = detail.text
            videos = self.fl(res)
            result = {'list': videos}
            return result
        except:
            pass

    def categoryContent(self, cid, pg, filter, ext):
        result = {}
        if pg:
            page = int(pg)
        else:
            page = 1
        page = int(pg)
        videos = []

        if '类型' in ext.keys():
            lxType = ext['类型']
        else:
            lxType = ''
        if '地区' in ext.keys():
            DqType = ext['地区']
        else:
            DqType = ''
        if '语言' in ext.keys():
            YyType = ext['语言']
        else:
            YyType = ''
        if '年份' in ext.keys():
            NfType = ext['年份']
        else:
            NfType = ''
        if '排序' in ext.keys():
            PxType = ext['排序']
        else:
            PxType = '2'

        videos = []
        if 'topic' not in cid:
            url = xurl + '/show/' + cid + '-' + lxType + '-' + DqType + '-' + YyType + '-' + NfType + '-' + PxType + '-' + str(
                page) + ".html"
        else:
            url = xurl + cid + str(page) + '.html'
        try:
            detail = requests.get(url=url, headers=headerx)
            detail.encoding = "utf-8"
            res = detail.text
            videos = self.fl(res)
        except:
            pass
        result = {'list': videos}
        result['page'] = pg
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result

    def detailContent(self, ids):
        global pm
        did = ids[0]
        result = {}
        videos = []
        playurl = ''
        res = requests.get(url=did, headers=headerx)
        res = res.text
        match = re.search(r'<title>(.*?)-可可影视', res)
        if match:
            pm = match.group(1)

        soups = BeautifulSoup(res, 'html.parser')
        dy = soups.find_all('div', class_="detail-info-row")
        actor = ''
        content = ''
        jj = soups.find('div', class_="detail-desc")
        content = jj.find('p').text.strip()
        for dy1 in dy:
            if dy1.find('div', class_="detail-info-row-side").text == '导演:':
                director = dy1.find('a').text
            if dy1.find('div', class_="detail-info-row-side").text == '演员:':
                yy = dy1.find_all('a')
                for yy1 in yy:
                    actor = actor + ' ' + yy1.text
            if dy1.find('div', class_="detail-info-row-side").text == '首映:':
                year = dy1.find('div', class_="detail-info-row-main").text
            if dy1.find('div', class_="detail-info-row-side").text == '备注:':
                area = dy1.find('div', class_="detail-info-row-main").text
        soup = soups.find('div', class_="swiper source-swiper")
        vods = soup.find_all('div', class_="swiper-slide")
        playform = ''
        for vod in vods:
            pf = vod.find('span').text
            if pf == 'HN线路' or pf == '蓝光2' or pf == '蓝光9' or pf == '蓝光7' or pf == 'XL线路' or pf == 'SB线路':
                pf = pf + '-广告'
            nb = vod.find('i', class_="source-item-num").text
            playform = playform + pf + '-' + nb + '$$$'
        playform = playform[:-3]
        soup = soups.find('div', class_="episode-box-main")
        vods = soup.find_all('div')
        purl = ''
        for vod1 in vods:
            for vod in vod1.find_all('a'):
                name = vod.text
                number = re.findall(r'\d+', name)
                if number:
                    number = int(number[0])
                else:
                    number = 0
                js = vod['href']
                purl = purl + name + '$' + str(number) + xurl + js + '#'
            purl = purl[:-1] + '$$$'
        purl = purl[:-3]

        videos.append({
            "vod_id": did,
            "vod_name": pm,
            "vod_pic": "",
            "type_name": '',
            "vod_year": year,
            "vod_area": area,
            "vod_remarks": "",
            "vod_actor": actor,
            "vod_director": director,
            "vod_content": content,
            "vod_play_from": playform,
            "vod_play_url": purl
        })

        result['list'] = videos

        return result

    def playerContent(self, flag, id, vipFlags):
        parts = id.split("http")
        if len(parts) > 1:
            before_https, after_https = parts[0], 'http' + parts[1]
        result = {}
        res = requests.get(url=after_https, headers=headerx)
        match = re.search(r'src: "(.*?)"', res.text)
        if match:
            purl = match.group(1)
        result["parse"] = 0
        result["playUrl"] = ''
        result["url"] = purl
        result["header"] = headerx
        result["danmaku"] = 'http://back1.hpnu.cn:29966/api/danmu?do=danmuku&vodName=' + pm + '&jishu=' + before_https
        return result

    def searchContentPage(self, key, quick, page):
        result = {}
        videos = []
        if not page:
            page = 1

        detail = requests.get(xurl + '/search?k=' + key + '&page=' + str(page), headers=headerx)

        detail.encoding = "utf-8"
        doc = BeautifulSoup(detail.text, "html.parser")
        soups = doc.find('div', class_="search-result-list fs-margin-section")
        soup = soups.find_all('a')
        for vod in soup:
            name = vod.select_one("div div div img")['alt']
            id = xurl + vod["href"]
            pic = 'https://vres.miximixi.me' + vod.select_one("div div div div img")['data-original']
            remark = vod.select_one("div div").text.strip()
            video = {
                "vod_id": id,
                "vod_name": name,
                "vod_pic": pic,
                "vod_remarks": remark
            }
            videos.append(video)

        result['list'] = videos
        result['page'] = page
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result

    def searchContent(self, key, quick):
        return self.searchContentPage(key, quick, '1')

    def localProxy(self, params):
        if params['type'] == "m3u8":
            return self.proxyM3u8(params)
        elif params['type'] == "media":
            return self.proxyMedia(params)
        elif params['type'] == "ts":
            return self.proxyTs(params)
        return None
