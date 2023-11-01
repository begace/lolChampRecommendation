# TF-IDF 방식으로 모델링
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.io import mmwrite, mmread
import pickle

# 리뷰 데이터를 CSV 파일로부터 불러옴
df_reviews = pd.read_csv('./cleaned_review.csv')
# 데이터의 정보를 출력 (행, 열, 누락 데이터 등의 정보 확인 가능)
df_reviews.info()

# TF-IDF 변환기를 초기화. sublinear_tf 옵션은 로그 스케일링을 적용
Tfidf = TfidfVectorizer(sublinear_tf=True)
# 리뷰 데이터에 대해 TF-IDF 값을 계산
Tfdif_matrix = Tfidf.fit_transform(df_reviews['review'])

# 계산된 TF-IDF 행렬의 크기를 출력 (문서 수 x 단어 수)
print(Tfdif_matrix.shape)

# TF-IDF 변환기 객체를 파일로 저장 (추후 사용을 위해)
with open('./models/tfidf.pickle', 'wb') as f:
    pickle.dump(Tfidf, f)

# TF-IDF 행렬을 Matrix Market 포맷으로 저장
mmwrite('./models/Tfidf_champ_review.mtx', Tfdif_matrix)
