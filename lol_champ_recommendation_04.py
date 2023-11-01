#단어 시각화
import pandas as pd
import collections

from wordcloud import WordCloud as wd
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 폰트
font_path = './malgun.ttf'
font_name = font_manager.FontProperties(fname = font_path).get_name()
plt.rc('font', family='NanumBarunGothic')

# 전처리한 데이터 읽어오기
df = pd.read_csv('./cleaned_review.csv')

# 몇번째에 있는지 찾기위한 변수
counter = 0

for i in df.iloc:
    if '쉬바나' == i[0]: break #찾으면 종료
    counter+=1

# counter번째의 단어들 선택
words = df.iloc[counter,1].split()
#print(df.iloc[counter,0])

# 단어의 빈도수 카운터
worddict = collections.Counter(words)
# 딕셔너리 형태로 저장
worddict = dict(worddict)

# 워드 클라우드 생성
wordcloud_img = wd(
    background_color='white', max_words=2000, font_path=font_path
    ).generate_from_frequencies(worddict)

# 워드 클라우드 화면에 표시
plt.figure(figsize=(12,12))
plt.imshow(wordcloud_img, interpolation='bilinear')
plt.axis('off')
plt.show()