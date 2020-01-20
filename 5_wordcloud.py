from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

with open("5c_bibel.txt") as f:
    text = f.read()

with open("5b_german_stopwords.txt") as s:
    sw = s.read().split()

for stop in sw:
    STOPWORDS.add(stop)

wordcloud = WordCloud(width=1920, height=1200)
wordcloud.generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
