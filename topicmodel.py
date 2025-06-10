import pandas as pd
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from gensim.models import Phrases, LdaModel
from gensim.corpora import Dictionary
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nltk.download('stopwords')
nltk.download('wordnet')

# 1. 데이터 로딩
df = pd.read_csv("spotify_reviews_labeled.csv")
df['at'] = pd.to_datetime(df['at'], errors='coerce')
df = df.dropna(subset=['at'])
df['content'] = df['content'].fillna('')


# 2. 필터링 함수
def filter_reviews(df, score, start_date=None, end_date=None):
    filtered = df[df['score'] == score]
    if start_date:
        filtered = filtered[filtered['at'] >= start_date]
    if end_date:
        filtered = filtered[filtered['at'] <= end_date]
    return filtered


# 3. 전처리 함수
def preprocess_texts(texts):
    tokenizer = RegexpTokenizer(r'\w+')
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    # 토큰화
    tokenized = [tokenizer.tokenize(text) for text in texts]
    # 불용어 제거
    tokenized = [[t for t in doc if t.lower() not in stop_words] for doc in tokenized]
    # 숫자 제거
    tokenized = [[t for t in doc if not t.isnumeric()] for doc in tokenized]
    # 한 글자 제거
    tokenized = [[t for t in doc if len(t) > 1] for doc in tokenized]
    # 표제어 추출
    tokenized = [[lemmatizer.lemmatize(t) for t in doc] for doc in tokenized]

    # Bigram 모델 생성 후 적용
    bigram = Phrases(tokenized, min_count=20)
    texts_with_bigram = []
    for doc in tokenized:
        new_doc = doc[:]
        for token in bigram[doc]:
            if '_' in token:
                new_doc.append(token)
        texts_with_bigram.append(new_doc)
    return texts_with_bigram


# 4. LDA 모델링 함수
def lda_modeling(texts, num_topics=6, passes=20, iterations=400):
    dictionary = Dictionary(texts)
    dictionary.filter_extremes(no_below=20, no_above=1.0)
    corpus = [dictionary.doc2bow(text) for text in texts]

    model = LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=num_topics,
        passes=passes,
        iterations=iterations,
        alpha='auto',
        eta='auto',
        eval_every=None,
        chunksize=2000,
    )
    return model, dictionary, corpus


# 5. 워드클라우드 그리기 함수
def draw_wordcloud_from_lda(model, topic_num, topn=20, title=None):
    topic_words = dict(model.show_topic(topic_num, topn=topn))
    wc = WordCloud(width=600, height=400, background_color='white', colormap='viridis')
    wc.generate_from_frequencies(topic_words)
    plt.figure(figsize=(8, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    if title:
        plt.title(title)
    plt.show()


# === 부정 리뷰 분석 (2018-09-01 ~ 2019-06-30) ===
df_neg = filter_reviews(df, score=0, start_date='2018-09-01', end_date='2019-06-30')
texts_neg = preprocess_texts(df_neg['content'].tolist())
model_neg, dict_neg, corpus_neg = lda_modeling(texts_neg)

print("부정 리뷰 토픽별 워드클라우드")
for t in range(model_neg.num_topics):
    draw_wordcloud_from_lda(model_neg, topic_num=t, title=f'Negative Topic {t + 1} Word Cloud')

# === 긍정 리뷰 분석 (2023-10-01 이후) ===
df_pos = filter_reviews(df, score=1, start_date='2023-10-01')
texts_pos = preprocess_texts(df_pos['content'].tolist())
model_pos, dict_pos, corpus_pos = lda_modeling(texts_pos)

print("긍정 리뷰 토픽별 워드클라우드")
for t in range(model_pos.num_topics):
    draw_wordcloud_from_lda(model_pos, topic_num=t, title=f'Positive Topic {t + 1} Word Cloud')
