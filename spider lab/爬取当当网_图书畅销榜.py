# @author : scott
# @site : 
# @time : 2022/2/5 0:21
# @file : 爬取当当网_图书畅销榜.py
#导包
import urllib.request
from lxml import html
etree = html.etree

def create_request(page):

        #第一页 http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-1
        #第二页 http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-2
        #第二十五页 http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-25
        url = "http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-" + str(page)

        #网页headers
        headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Cookie':'ddscreen=2; ddscreen=2; from=460-5-biaoti; order_follow_source=P-460-5-bi%7C%231%7C%23www.baidu.com%252Fother.php%253Fsc.Kf0000aO75ZvJyzJIKo9s_DX9Rem2EqFANelJU82o9RB6_xq5spubAgXloEiCZN-4vRh9-w8u%7C%230-%7C-; ddscreen=2; dest_area=country_id%3D9000%26province_id%3D111%26city_id%20%3D0%26district_id%3D0%26town_id%3D0; __permanent_id=20220205000906326335681546069545394; __visit_id=20220205000906328285216974085863122; __ddc_1d=1643990946%7C!%7C_utm_brand_id%3D11106; __ddc_24h=1643990946%7C!%7C_utm_brand_id%3D11106; __ddc_15d=1643990946%7C!%7C_utm_brand_id%3D11106; __out_refer=1643990946%7C!%7Cwww.baidu.com%7C!%7C%25E5%25BD%2593%25E5%25BD%2593%25E7%25BD%2591; __ddc_15d_f=1643990946%7C!%7C_utm_brand_id%3D11106; __rpm=mix_65152...1643990950857%7C...1643992225213; __trace_id=20220205003026093265725987748110502',
            'Host':'bang.dangdang.com',
            'Referer':'http://bang.dangdang.com/books/',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
        }

        request = urllib.request.Request(url = url,headers = headers)

        return request


def get_content(request):

    response = urllib.request.urlopen(request)

    content = response.read().decode("gbk")

    return content

def download_namelist(content):

    tree = etree.HTML(content)

    #获取作品名字列表
    works_list = tree.xpath('//div[@class="name"]/a[@title]//text()')

    #print(list(set(work_list)))
    return works_list

def download_authorlist(content):

    tree = etree.HTML(content)

    #获取作者名字列表
    authors_list = tree.xpath('//div[@class="publisher_info"]/a[1]//text()')

    #print(author_list)
    return authors_list

if __name__ == '__main__':
    star_page = int(input("请输入从第几页开始获取: "))
    end_page = int(input("请输入到第几页结束获取: "))
    i = 0
    j = 0

with open(r"book_ranking_list.txt","w") as f:
    for page in range(star_page,end_page+1):
        # (1) 请求对象的定制
        request = create_request(page)
        # （2）获取网页的源码
        content = get_content(request)
        # （3）得到相应数据
        works_list = download_namelist(content)
        authors_list = download_authorlist(content)

        #将数据整理
        while(True):
            #i如果不是最后一位
            if i != len(works_list)-1:
                #分情况 有的书名名字太长 有省略号
                if works_list[i+1] == "...":

                    #写入作品名称和省略号
                    f.writelines(works_list[i])
                    f.writelines(works_list[i+1])

                    #写入作者
                    f.writelines("\t"+"作者: ")
                    f.writelines(authors_list[j])
                    f.writelines("\n")

                    i = i+2
                    j = j+2#authors_list中还有出版社我没有用
                else:
                    f.writelines(works_list[i])

                    f.writelines("\t"+"作者: ")
                    f.writelines(authors_list[j])
                    f.writelines("\n")

                    i = i+1
                    j = j+2
            else:
                f.writelines(works_list[i])

                f.writelines("\t"+"作者: ")
                f.writelines(authors_list[j])

                break
f.close()











