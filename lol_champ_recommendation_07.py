import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from scipy.io import mmread
import pickle
from konlpy.tag import Okt
import re
from gensim.models import Word2Vec

def getRecommendation(cosin_sim):
    simScore = list(enumerate(cosin_sim[-1]))
    simScore = sorted(simScore, key=lambda x:x[1], reverse=True)
    simScore = simScore[:11]
    moviIdx = [i[0] for i in simScore]
    recMovieList = df_reviews.iloc[moviIdx, 0]
    return recMovieList

df_reviews = pd.read_csv('./cleaned_review.csv')
Tfidf_matrix = mmread('./models/Tfidf_champ_review.mtx').tocsr()
with open('./models/tfidf.pickle','rb') as f:
    Tfidf = pickle.load(f)

champNum = 383

# print(df_reviews.iloc[champNum,0])
# cosine_sim = linear_kernel(Tfidf_matrix[champNum],Tfidf_matrix)
#
# print(cosine_sim[0])
# print(len(cosine_sim[0]))
#
# print(getRecommendation(cosine_sim))

#keyword 기반 추천
embedding_model = Word2Vec.load('./models/word2vec_movie_review.model')
# keyword = ('홍길동')
# try:
#     sim_word = embedding_model.wv.most_similar(keyword, topn = 10)
# except :
#     print("제가 모르는 단어에요")
#     exit()
#
# print(sim_word)
#
# words = [keyword]
# for word in sim_word:
#     words.append(word)
# print(words)
#
# sentesce = []
# count = 10
# for word in words:
#     if isinstance(word, tuple):  # sim_word에서 단어만 추출
#         word = word[0]
#     sentesce.extend([word] * count)  # 여기서 extend를 사용하여 단어를 추가합니다.
#     count -= 1
# sentesce = ' '.join(sentesce)
# print(sentesce)
#
# sentesce_vec = Tfidf.transform([sentesce])
# cosin_sim = linear_kernel(sentesce_vec, Tfidf_matrix)
# recommendation = getRecommendation(cosin_sim)
# print(recommendation)

# 문장 기반 추천
sentence = '차원문'
X = sentence

okt = Okt()
X = re.compile('[^가-힣]').sub(' ',X)
X = okt.pos(X, stem= True)

print([x[0] for x in X if x[1] in['Noun', 'Verb', 'Adjective']])

X = ' '.join([x[0] for x in X if x[1] in ['Noun', 'Verb', 'Adjective']])

print(X)

sentence_vec = Tfidf.transform([X])
cosin_sim = linear_kernel(sentence_vec, Tfidf_matrix)
recommendation = getRecommendation(cosin_sim)
print(recommendation)