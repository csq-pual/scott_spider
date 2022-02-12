# scott_spider
简体中文





## 爬取当当网_图书畅销榜

# 目录

- 目标
- 快速入门
  - 安装pycharm lxml xpath
  - xpath教程
- 贡献者
- 功能

## 目标

- [ ] [当当网_图书排行榜](http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-1)

## 快速入门

### 安装

- 安装[pycharm](https://blog.csdn.net/qq_29883591/article/details/52664478?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164470389516781683994757%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=164470389516781683994757&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-1-52664478.pc_search_result_cache&utm_term=pycharm%E5%AE%89%E8%A3%85&spm=1018.2226.3001.4187) [lxml](https://blog.csdn.net/weixin_42301205/article/details/99566786?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164470392616780255266127%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=164470392616780255266127&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-1-99566786.pc_search_result_cache&utm_term=pycharm%E5%AE%89%E8%A3%85lxml&spm=1018.2226.3001.4187) [xpath](https://blog.csdn.net/weixin_30819085/article/details/94790208?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164470395116780271914452%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=164470395116780271914452&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-1-94790208.pc_search_result_cache&utm_term=%E8%B0%B7%E6%AD%8C%E5%AE%89%E8%A3%85xpath&spm=1018.2226.3001.4187)
- [xpath用法

### 用法

```python
# @author : scott
# @site : 
# @time : 2022/2/5 0:21
# @file : 爬取当当网_图书畅销榜.py
#导包
import urllib.request
from lxml import html
etree = html.etree

def create_request(page):

def get_content(request):

def download_namelist(content):

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
```

### 运行结果

```
请输入从第几页开始获取: 1
请输入到第几页结束获取: 1

Process finished with exit code 0
```

## 贡献者们

- Shiqi Chen

## 功能

### 本身功能

- [x] 爬取排行榜的图书名单 以及作者

###  可拓展功能

#### 自行添加xpath路径获取更多信息

- [ ] 单价
- [ ] 热度
- [ ] 评分
- [ ] 出版社
- [ ] 分类
