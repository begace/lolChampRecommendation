# 의미공간상에 단어를 배치할 것
import pandas as pd
from gensim.models import Word2Vec

# 리뷰 데이터를 CSV 파일로부터 불러옴
df_review = pd.read_csv('./cleaned_review.csv')
# 데이터의 정보를 출력 (행, 열, 누락 데이터 등의 정보 확인 가능)
df_review.info()

# 'reviews' 컬럼의 모든 리뷰를 리스트로 저장
reviews = list(df_review['review'])
# 첫 번째 리뷰 출력
print(reviews[0])

# 각 리뷰를 토큰화하여 tokens 리스트에 저장
tokens = []
for sentence in reviews:
    token = sentence.split()
    tokens.append(token)

# 토큰화된 첫 번째 리뷰 출력
print(tokens[0])

# Word2Vec 모델 학습
# 파라미터 설명:
# vector_size: 임베딩된 벡터의 차원
# window: 현재 단어와 예측 단어 사이의 최대 거리
# min_count: 모델 학습에 사용할 단어의 최소 빈도 수
# workers: 학습을 위해 사용할 프로세서 코어의 수
embedding_model = Word2Vec(tokens, vector_size=100, window = 4, min_count=20, workers= 15)

# 학습된 Word2Vec 모델을 파일로 저장
embedding_model.save('./models/word2vec_champ_review.model')

# 모델의 어휘 목록 출력
print(list(embedding_model.wv.index_to_key))
# 모델의 어휘 크기 출력
print(len(embedding_model.wv.index_to_key))