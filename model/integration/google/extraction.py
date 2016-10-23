# Author: Olivier Grisel <olivier.grisel@ensta.org>
#         Lars Buitinck
#         Chyi-Kwei Yau <chyikwei.yau@gmail.com>
# License: BSD 3 clause
#
# Heavy modifications by Nate Moon at HackRU Fall 2016
#

from __future__ import print_function
from time import time

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.datasets import fetch_20newsgroups

n_samples = 5
n_features = 1000
n_topics = 10
n_top_words = 20


class TopicExtractor(object):

    @staticmethod
    def print_top_words(model, feature_names, n_top_words):
        for topic_idx, topic in enumerate(model.components_):
            print("Topic #%d:" % topic_idx)
            print(" ".join([feature_names[i]
                            for i in topic.argsort()[:-n_top_words - 1:-1]]))
        print()

    @staticmethod
    def Extract(data_samples):

        print(data_samples)

        tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2,
                                        max_features=n_features,
                                        stop_words='english')
        tf = tf_vectorizer.fit_transform(data_samples)
        lda = LatentDirichletAllocation(n_topics=n_topics, max_iter=5,
                                        learning_method='online',
                                        learning_offset=50.,
                                        random_state=0)
        lda.fit(tf)

        tf_feature_names = tf_vectorizer.get_feature_names()
        #TopicExtractor.print_top_words(lda, tf_feature_names, n_top_words)

        results = []
        for topic_idx, topic in enumerate(lda.components_):
            results.append([tf_feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])


        frequency_count = {}

        for topiclist in results:
            for topic in topiclist:
                try:
                    frequency_count[topic] = frequency_count[topic] + 1
                except:
                    frequency_count[topic] = 1

        tmp = [[key, val] for key, val in frequency_count.iteritems()]

        sortedList = sorted(tmp, key=lambda student: student[1], reverse=True)

        return sortedList