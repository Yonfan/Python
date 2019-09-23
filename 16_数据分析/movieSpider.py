## 调用要使用的包
import json
import random
import requests
import time
import pandas as pd
import os
from pyecharts import Bar, Geo, Line, Overlap
import jieba        # 支持中文分词的库
import imageio
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from collections import Counter

os.chdir(r'E:\python\16_数据分析\dataDir')

## 设置headers和cookie
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Connection': 'keep-alive',
    'Cookie': 'v=3; _lxsdk_cuid=167df0ceb48c8-0ab61c9f59a1d3-b34356b-15f900-167df0ceb48c8; __mta=53769879.1545635425297.1545635425297.1545635535985.2; uuid_n_v=v1; iuuid=4C9B5260074B11E9895CE345260BD8F185745B9064AC489F813FF12A29123ABE; webp=true; ci=257%2C%E8%8D%86%E5%B7%9E; _lxsdk=4C9B5260074B11E9895CE345260BD8F185745B9064AC489F813FF12A29123ABE; __mta=53769879.1545635425297.1545635535985.1545635705933.3; from=canary',
    'Host': 'm.maoyan.com'
}


def getMovieInfo():
    movieData = pd.DataFrame(columns=['date', 'score', 'city', 'comment', 'nick'])
    for i in range(0, 1000):
        j = random.randint(1, 1000)
        print('success : ' + str(i) + ' ' + str(j))
        try:
            time.sleep(2)
            url = 'http://m.maoyan.com/mmdb/comments/movie/249342.json?_v_=yes&offset=' + str(j)
            html = requests.get(url=url, headers=headers).content
            data = json.loads(html.decode('utf-8'))['cmts']
            for item in data:
                movieData = movieData.append(
                    {'date': item['time'].split(' ')[0], 'city': item['cityName'], 'score': item['score'],
                     'comment': item['content'], 'nick': item['nick']}, ignore_index=True)
            movieData.to_excel('海王电影评论信息.xlsx', index=False)
        except:
            print('Throw Exception,Convert_to_excel Failed!!!')
            continue


# 去重
def dataProcess():
    data = pd.read_excel(r'../dataDir/海王电影评论信息.xlsx')
    data = data.drop_duplicates()
    data = pd.DataFrame(data)
    data.to_excel(r'../dataDir/海王电影评论信息new.xlsx')


# 数据分析图表
def getCharts():
    # 读取我们已经爬取到的数据进行分析
    auqaman_com = pd.read_excel(r'../dataDir/海王电影评论信息new.xlsx')
    grouped = auqaman_com.groupby(['city'])
    grouped_pct = grouped['score']

    # 全国热力图
    city_com = grouped_pct.agg(['mean', 'count'])
    city_com.reset_index(inplace=True)
    city_com['mean'] = round(city_com['mean'], 2)
    data = [(city_com['city'][i], city_com['count'][i]) for i in range(0, city_com.shape[0])]
    geo = Geo('《Aquaman海王》全国热力图', title_color="#fff",
              title_pos="center", width=1200, height=600, background_color='#404a59')
    while True:
        attr, value = geo.cast(data)
        try:
            geo.add("", attr, value, type="heatmap", visual_range=[0, 200],
                    visual_text_color="#fff", symbol_size=10, is_visualmap=True,
                    is_roam=False)
            print('data长度', len(data))
            break
        except ValueError as e:
            e = str(e)
            e = e.split("No coordinate is specified for ")[1]  # 获取不支持的城市名
            print('当前处理这个城市名：', e)
            for eve in data:
                if eve[0] == e:
                    data.remove(eve)
                    break
        print(len(data))
    geo.render('Aquaman海王全国热力图.html')

    # 主要城市评论数与评分
    city_main = city_com.sort_values('count', ascending=False)[0:20]
    attr = city_main['city']
    v1 = city_main['count']
    v2 = city_main['mean']
    line = Line("《Aquaman海王》主要城市评分")
    line.add("分数", attr, v2, is_stack=True, xaxis_rotate=30,
             mark_point=['min', 'max'], xaxis_interval=0, line_color='lightblue',
             line_width=4, mark_point_textcolor='black', mark_point_color='lightblue',
             is_splitline_show=False)

    bar = Bar("《Aquaman海王》主要城市评论数")
    bar.add("城市", attr, v1, is_stack=False, xaxis_rotate=30,
            xaxis_interval=0, is_splitline_show=False)
    overlap = Overlap()
    # 默认不新增 x y 轴，并且 x y 轴的索引都为 0
    overlap.add(bar)
    overlap.add(line, yaxis_index=1, is_add_yaxis=True)
    overlap.render('Aquaman海王主要城市评论数_平均分.html')

    # 主要城市评分降序
    city_score = city_main.sort_values('mean', ascending=False)
    attr = city_score['city']
    v1 = city_score['mean']
    line = Line("《Aquaman海王》主要城市评分")
    line.add("城市", attr, v1, is_stack=True, xaxis_rotate=30,
             mark_point=['min', 'max'], xaxis_interval=0, line_color='lightblue',
             line_width=4, mark_point_textcolor='black', mark_point_color='lightblue',
             is_splitline_show=False)
    line.render('Aquaman海王主要城市评分.html')

    # 主要城市评分全国分布
    city_score_area = city_com.sort_values('count', ascending=False)[0:30]
    city_score_area.reset_index(inplace=True)
    data = [(city_score_area['city'][i], city_score_area['mean'][i]) for i in range(0,
                                                                                    city_score_area.shape[0])]
    geo = Geo('《Aquaman海王》全国主要城市打分图', title_color="#fff",
              title_pos="center", width=1200, height=600, background_color='#404a59')
    attr, value = geo.cast(data)
    geo.add("", attr, value,
            visual_text_color="#fff", symbol_size=15, is_visualmap=True,
            is_roam=False, visual_range=[0, 200])
    geo.render('Aquaman海王全国主要城市打分图.html')

    # 绘制词云
    haoxi_str = ' '.join(auqaman_com['comment'])
    words_list = []
    word_generator = jieba.cut_for_search(haoxi_str)
    for word in word_generator:
        words_list.append(word)
    words_list = [k for k in words_list if len(k) > 1]
    back_color = imageio.imread(r'E:\怎么可开心皱着眉\素材\back.jpg')  # 解析该图片
    wc = WordCloud(background_color='white',  # 背景颜色
                   max_words=200,  # 最大词数
                   mask=back_color,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
                   max_font_size=300,  # 显示字体的最大值
                   font_path=r"E:\python\98_ttf\STKAITI.ttf",  # 解决显示口字型乱码问题，可进入C:/Windows/Fonts/目录更换字体
                   random_state=42,  # 为每个词返回一个PIL颜色
                   )
    haoxi_count = Counter(words_list)
    wc.generate_from_frequencies(haoxi_count)
    # 基于彩色图像生成相应彩色
    image_colors = ImageColorGenerator(back_color)
    # 绘制结果
    plt.figure()
    plt.imshow(wc.recolor(color_func=image_colors))
    plt.axis('off')
    plt.savefig('Aquaman海王词云分析.png', dpi=400)
    plt.show()


if __name__ == '__main__':
    # getMovieInfo() # 获取数据
    dataProcess()   # 处理数据
    getCharts()     # 绘制图表
