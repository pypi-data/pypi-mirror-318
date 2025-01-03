from dataharvest.purifier import AutoPurifier
from dataharvest.spider import AutoSpider


def test_auto_purifier_sohu():
    url = "https://www.sohu.com/a/325718406_120013344"
    auto_spider = AutoSpider()
    doc = auto_spider.crawl(url)
    auto_purifier = AutoPurifier()
    doc = auto_purifier.purify(doc)
    print(doc)


def test_auto_purifier_sll():
    url = "http://www.360doc.com/content/23/0613/11/72042116_1084562587.shtml"
    auto_spider = AutoSpider()
    doc = auto_spider.crawl(url)
    auto_purifier = AutoPurifier()
    doc = auto_purifier.purify(doc)
    print(doc)


def test_auto_purifier_baijiahao():
    url = "https://baijiahao.baidu.com/s?id=1800439094856373024"
    auto_spider = AutoSpider()
    doc = auto_spider.crawl(url)
    print(doc)
    auto_purifier = AutoPurifier()
    doc = auto_purifier.purify(doc)
    print(doc)


def test_auto_purifier_wangyi():
    url = "https://www.163.com/auto/article/J6361L350008856R.html?clickfrom=w_lb_4_big"
    auto_spider = AutoSpider()
    doc = auto_spider.crawl(url)
    auto_purifier = AutoPurifier()
    doc = auto_purifier.purify(doc)
    print(doc)


def test_auto_purifier_sogoubaike():
    url = "https://baike.sogou.com/v63038718.htm"
    auto_spider = AutoSpider()
    doc = auto_spider.crawl(url)
    auto_purifier = AutoPurifier()
    doc = auto_purifier.purify(doc)
    print(doc)


def test_auto_purifier_bilibili():
    url = "https://www.bilibili.com/read/cv35655718/?from=category_0&jump_opus=1"
    auto_spider = AutoSpider()
    doc = auto_spider.crawl(url)
    auto_purifier = AutoPurifier()
    doc = auto_purifier.purify(doc)
    print(doc)


def test_auto_purifier_qqnew():
    url = "https://new.qq.com/rain/a/20240703A09D9300"
    auto_spider = AutoSpider()
    doc = auto_spider.crawl(url)
    auto_purifier = AutoPurifier()
    doc = auto_purifier.purify(doc)
    print(doc)


def test_auto_purifier_sobaike():
    url = "https://baike.so.com/doc/5579340-5792710.html?src=index#entry_concern"
    auto_spider = AutoSpider()
    doc = auto_spider.crawl(url)
    print(doc)
    auto_purifier = AutoPurifier()
    doc = auto_purifier.purify(doc)
    print(doc)


def test_auto_purifier_toutiao():
    url = "https://www.toutiao.com/article/7359215340544344614/"
    auto_spider = AutoSpider()
    doc = auto_spider.crawl(url)
    auto_purifier = AutoPurifier()
    doc = auto_purifier.purify(doc)
    print(doc)


def test_auto_purifier_wechat():
    url = "https://mp.weixin.qq.com/s?__biz=MzA4Njc0OTc3Mw==&mid=2650879951&idx=1&sn=4370b54d5b06b34aeb063056f1a663d9&chksm=843670edb341f9fbfd64d6ac1c9f2a53160c4f6e8a3bdaaf15167003f95c07667bf1fcc4a0b0&token=139110043&lang=zh_CN#rd"
    auto_spider = AutoSpider()
    doc = auto_spider.crawl(url)
    auto_purifier = AutoPurifier()
    doc = auto_purifier.purify(doc)
    print(doc)


def test_auto_purifier_xiaohongshu():
    url = "http://xhslink.com/wgaRGR"
    auto_spider = AutoSpider()
    doc = auto_spider.crawl(url)
    auto_purifier = AutoPurifier()
    doc = auto_purifier.purify(doc)
    print(doc)
