import re
import string

import matplotlib.pyplot as plt
import nltk
import pandas as pd
import scipy.cluster.hierarchy as sch
import spacy
import spacy_spanish_lemmatizer
from nltk.stem import SnowballStemmer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from scipy.cluster.hierarchy import dendrogram, fcluster, linkage
from sklearn.cluster import KMeans
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import (CountVectorizer, TfidfTransformer,
                                             TfidfVectorizer)
from sklearn.metrics import silhouette_score
from wordcloud import WordCloud

# import es_core_new_sm

# lmm = spacy.load("es_core_news_sm")
# lmm.replace_pipe("lemmatizer", "spanish_lemmatizer")


def read_data(path, key):
    data = pd.read_csv(path, sep=';')
    list_row = data[key].values.tolist()
    return list_row


def remove_useless_data(rows, stop_words=[]):
    ''' Return clean text array '''
    new_rows = list()
    pattern1 = re.compile(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    )
    pattern2 = re.compile('[,.\"!@#$%^&*(){}?/;`~:<>+=-]')
    table = str.maketrans('', '', string.punctuation)

    for row in rows:
        row = str(row)
        row = row.lower()
        row = pattern1.sub('', row)
        row = pattern2.sub('', row)
        tokens = word_tokenize(row)
        row_no_punctuation = [w.translate(table) for w in tokens]
        row_no_num = [w for w in row_no_punctuation if w.isalpha()]
        row = [w for w in row_no_num if not w in stop_words]
        # row = [lemm(w) for w in row_no_num if not w in stop_words]
        # row = [PorterStemmer().stem(w) for w in row_no_num if not w in stop_words]
        # row = [SnowballStemmer('spanish').stem(w) for w in row_no_num if not w in stop_words]
        row = ' '.join(row)
        new_rows.append(row)
    return new_rows


def show_wordcloud(sentences, save=False, img_name=None):
    wordcloud = WordCloud(
        background_color='white',
        colormap='Set2',
        width=1000,
        height=500,
        max_words=1000,
        relative_scaling=1,
        scale=3,
        random_state=1,
        collocations=False).generate_from_frequencies(sentences)
    fig = plt.figure(1, figsize=(13, 13))
    plt.axis('off')
    plt.imshow(wordcloud)
    if save:
        wordcloud.to_file(img_name + '.png')
        # plt.savefig(img_name)
    plt.show()


def display_topics(model, feature_names, no_top_words):
    topic_dict = {}
    for topic_idx, topic in enumerate(model.components_):
        topic_dict["Topic %d words" % (topic_idx + 1)] = [
            '{}'.format(feature_names[i])
            for i in topic.argsort()[:-no_top_words - 1:-1]
        ]
        topic_dict["Topic %d weights |" % (topic_idx + 1)] = [
            '{:.1f} |'.format(topic[i])
            for i in topic.argsort()[:-no_top_words - 1:-1]
        ]
    return pd.DataFrame(topic_dict)


def lemm(word):
    lem = [w.lemma_ for w in lmm(word)]
    return lem[0]


if __name__ == '__main__':
    stop_words_file = open('/home/evil/Me/Nlp/final/spanish_stopwords.txt', 'r')

    spanish_stop_words = stop_words_file.read().splitlines()
    stop_words_file.close()

    rows = read_data(
        '/home/evil/Me/Nlp/final/Congresal_Periods/Second_congress.csv',
        'Objeto')
    rows = remove_useless_data(rows, spanish_stop_words)

    tfidf_vectorizer = TfidfVectorizer()
    # tfidf_vectorizer = CountVectorizer()
    tfidf = tfidf_vectorizer.fit_transform(rows)
    df = pd.DataFrame(tfidf.toarray(),
                      columns=tfidf_vectorizer.get_feature_names())
    freq = df.T.sum(axis=1)
    show_wordcloud(freq, save=True, img_name='wcloud_congreso2')
