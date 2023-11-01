import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QStringListModel
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from scipy.io import mmread
import pickle
from konlpy.tag import Okt
import re
from gensim.models import Word2Vec
from tqdm import tqdm

form_window = uic.loadUiType('./champ_recommendation.ui')[0]

class Exam(QWidget, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Tfidf_matrix = mmread('./models/Tfidf_champ_review.mtx').tocsr()
        with open('./models/tfidf.pickle', 'rb') as f:
            self.Tfidf = pickle.load(f)
        self.embedding_model = Word2Vec.load('./models/word2vec_champ_review.model')

        self.df_reviews = pd.read_csv('./cleaned_review.csv')

        self.titles = list(self.df_reviews['name'])
        self.titles.sort()
        for title in self.titles:
            self.comboBox.addItem(title)

        model = QStringListModel()
        model.setStringList(self.titles)
        completer = QCompleter(model)
        completer.setModel(model)
        self.le_keyword.setCompleter(completer)

        self.comboBox.currentIndexChanged.connect(self.combobox_slot)
        self.btn_recommendation.clicked.connect(self.btn_slot)

        pass

    def sentenceBased(self, sentence):
        # 문장 기반 추천
        print('문장기반추천')
        df_stopwords = pd.read_csv('./stopwords.csv')
        stopwords = list(df_stopwords['stopword'])
        temp = sentence

        okt = Okt()

        for i in tqdm(range(len(temp))):
            print('for문 시작')
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
            if '미니언' in temp:
                temp = temp.replace('씨에스', '골드')
            if '킬데스' in temp:
                temp = temp.replace('킬데스', '킬뎃')
            if '챔' in temp:
                temp = temp.replace('챔피온', '챔피언')
                temp = temp.replace('챔피언', '챔피언')
                temp = temp.replace('챔프', '챔피언')
                temp = temp.replace('챔', '챔피언')
            if '캐릭' in temp:
                temp = temp.replace('캐릭', '챔피언')

            print("if문 통과")
            # 한글을 제외한 데이터를 모두 공백으로 처리
            temp = re.compile('[^가-힣]').sub(' ', str(temp))
            print('가힣통과')
            # 토크나이징
            tokened = okt.pos(temp, stem=True)
            print('토크나이징 통과')
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

        sentence_vec = self.Tfidf.transform([cleanSentence])
        cosin_sim = linear_kernel(sentence_vec, self.Tfidf_matrix)
        recommendation = self.getRecommendation(cosin_sim)
        recommendation = '\n'.join(recommendation)
        return recommendation

    def btn_slot(self):
        keyword = self.le_keyword.text()
        self.le_keyword.setText('')

        if keyword == '': return

        if keyword in self.titles:
            recommendation = self.recommandation_by_champ_title(keyword)
            self.lbl_recommendation.setText(recommendation[len(keyword):])
        else:
            try:
                recommendation = self.recommendation_by_keyword(keyword)
            except:
                recommendation = self.sentenceBased(keyword)

            self.lbl_recommendation.setText(recommendation)

    def recommendation_by_keyword(self, keyword):
        sim_word = self.embedding_model.wv.most_similar(keyword)

        try:
            sim_word = self.embedding_model.wv.most_similar(keyword, topn=10)
        except:
            return '다른 키워드를 입력하시오'

        print(sim_word)

        words = [keyword]
        for word in sim_word:
            words.append(word)

        sentesce = []
        count = 10
        for word in words:
            if isinstance(word, tuple):  # sim_word에서 단어만 추출
                word = word[0]
            sentesce.extend([word] * count)  # 여기서 extend를 사용하여 단어를 추가합니다.
            count -= 1
        sentesce = ' '.join(sentesce)

        sentesce_vec = self.Tfidf.transform([sentesce])
        cosin_sim = linear_kernel(sentesce_vec, self.Tfidf_matrix)
        recommendation = self.getRecommendation(cosin_sim)

        recommendation = '\n'.join(recommendation)
        print(recommendation)
        return recommendation

    def getRecommendation(self, cosin_sim):
        simScore = list(enumerate(cosin_sim[-1]))
        simScore = sorted(simScore, key=lambda x: x[1], reverse=True)
        simScore = simScore[:11]
        moviIdx = [i[0] for i in simScore]
        recChampList = self.df_reviews.iloc[moviIdx, 0]

        return recChampList

    def combobox_slot(self):
        title = self.comboBox.currentText()
        recommendation = self.recommandation_by_champ_title(title)
        self.lbl_recommendation.setText(recommendation[len(title):])

    def recommandation_by_champ_title(self, title):
        movie_idx = self.df_reviews[self.df_reviews['name'] == title].index[0]
        cosine_sim = linear_kernel(self.Tfidf_matrix[movie_idx], self.Tfidf_matrix)
        recommendation = self.getRecommendation(cosine_sim)
        recommendation = '\n'.join(recommendation)
        return recommendation


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Exam()
    mainWindow.show()
    sys.exit(app.exec_())