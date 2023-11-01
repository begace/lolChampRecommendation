import pandas as pd
import re
from konlpy.tag import Okt

from tqdm import tqdm

# 파일 읽어들임
fileRead = pd.read_csv('D:\\Github\\lolChampRecommendation\\inven_champ_url\\lol_champ_repl_new.CSV', encoding='cp949', header=None, names = ['name', 'review'])

# 읽은 파일 테스트
#print(fileRead)

# 토큰화를 위한 okt 불러오기
okt = Okt()
# 스탑워드 불러오기
df_stopwords = pd.read_csv('./stopwords.csv')
stopwords = list(df_stopwords['stopword'])

# 임시 변수에 리뷰만 옮겨놓기
temp = fileRead['review']

#print(temp.head())

# 전처리가 완료된 데이터가 들어갈 리스트를 미리 만듬
cleanSentences = []

one = []

for i in tqdm(range(len(temp))):
    # 특수한 단어들을 미리 처리함
    if '그랩' in temp:
        temp = temp.replace('그랩', '잡기')
    if '맞다이' in temp:
        temp = temp.replace('맞다이', '일대일')
    if '일댈' in temp:
        temp = temp.replace('일댈', '일대일')
    if '1대1' in temp:
        temp = temp.replace('1대1', '일대일')
    if '다대1' in temp:
        temp = temp.replace('다대1', '다대일')
    if '1대다' in temp:
        temp = temp.replace('1대다', '다대일')
    if '한타' in temp:
        temp = temp.replace('한타', '대규모 교전')
    if '새기' in temp:
        temp = temp.replace('새기', '새끼')
    if '시시기' in temp:
        temp = temp.replace('시시기', '군중제어기')
    if '씨씨기' in temp:
        temp = temp.replace('씨씨기', '군중제어기')
    if '개사기' in temp:
        temp = temp.replace('개사기', '매우 강함')
    if '라인전' in temp:
        temp = temp.replace('라인전', '초반')
    if '포킹' in temp:
        temp = temp.replace('포킹', '견제')
    if '이니시' in temp:
        temp = temp.replace('이니시', '개전')
    if '날먹' in temp:
        temp = temp.replace('날먹', '쉬운')
    if '씨에스' in temp:
        temp = temp.replace('씨에스', '골드')
    if '시에스' in temp:
        temp = temp.replace('시에스', '골드')
    if '미니언' in temp:
        temp = temp.replace('미니언', '골드')
    if '킬데스' in temp:
        temp = temp.replace('킬데스', '킬뎃')
    if '챔' in temp:
        temp = temp.replace('챔피온', '챔피언')
        temp = temp.replace('챔피언', '챔피언')
        temp = temp.replace('챔프', '챔피언')
        temp = temp.replace('챔', '챔피언')
    if '캐릭' in temp:
        temp = temp.replace('캐릭', '챔피언')

    # 한글을 제외한 데이터를 모두 공백으로 처리
    temp[i] = re.compile('[^가-힣]').sub(' ', str(temp[i]))
    # 토크나이징
    tokened = okt.pos(temp[i], stem= True)
    
    # 토크나이징한 문장을 데이터프레임화
    df_token = pd.DataFrame(tokened, columns=['word', 'class'])

    # 의미있는 데이터만 남기기
    df_token = df_token[(df_token['class'] == 'Noun') |
                        (df_token['class'] == 'Verb') |
                        (df_token['class'] == 'Adjective')]

    # 단어들 전처리를 위한 리스트 미리 만들기
    words = []

    # 수업시간에는 if 1<len word를 통해 1글자 짜리 데이터를 없앴지만
    # 게임 용어 특성상 필요한 한글자 단어를 위해 생략
    for word in df_token.word:
        if word not in stopwords:
            words.append(word)
            pass
    # for word in df_token.word:
    #     if len(word) > 1:
    #         if word not in stopwords:
    #             words.append(word)
    #             pass

    cleanSentence = ' '.join(words)
    cleanSentences.append(cleanSentence)

fileRead['review'] = cleanSentences
fileRead = fileRead[['name', 'review']]
#print(fileRead.head())
#fileRead.info()

fileRead.to_csv('D:\\Github\\lolChampRecommendation\\cleaned_review.csv', index_label=False)
