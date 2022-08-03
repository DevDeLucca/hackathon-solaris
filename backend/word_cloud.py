import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv('./data_example.csv', index_col=0)

nltk.download('stopwords')

from nltk.corpus import stopwords

stop = stopwords.words('portuguese')

df['content'] = df['content'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

wordcloud = WordCloud(background_color='white').generate(' '.join(df['content']))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()