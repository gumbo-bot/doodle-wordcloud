# import dependencies 

import matplotlib as mpl
import matplotlib.pyplot as plt

from wordcloud import WordCloud
'exec %matplotlib inline'


# location - input your  location here
location = r"C:\Users\graem\OneDrive\Documents\Coding\Python\Files\Doodle\guesses2.txt"

guesses = open(location, 'r', encoding="utf8").read()

# initiate a word cloud object
guesses_wc = WordCloud(
    background_color='black',
    max_words=2000,
    width = 2400,
    height = 1200,
)

# generate the word cloud
guesses_wc.generate(guesses)

fig = plt.figure()
fig.set_figwidth(20) 
fig.set_figheight(10)

# display word cloud
plt.imshow(guesses_wc, interpolation='bilinear')
plt.axis('off')
plt.show()

# uncomment to save rather than view - only use one or the other
# plt.figure( figsize=(20,10), facecolor='k')
# plt.imshow(guesses_wc)
# plt.axis("off")

# image save location
# img_location = r""