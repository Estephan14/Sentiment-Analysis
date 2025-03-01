import string
from collections import Counter # A container that keeps track of how many times equivalent values are added
import matplotlib.pyplot as plt

def get_tweets():
    import GetOldTweets3 as got
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('CoronaOutbreak') \
        .setSince("2020-01-01") \
        .setUntil("2020-04-01") \
        .setMaxTweets(1000)
    # Creation of list that contains all tweets
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    # Creating list of chosen tweet data
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets

# reading text file
text = "" # It concatenates all the tweet texts into a single string.
text_tweets = get_tweets()
length = len(text_tweets)

for i in range(0, length):
    text = text_tweets[i][0] + " " + text

# converting to lowercase
lower_case = text.lower()

# Removing punctuations
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# splitting text into words
tokenized_words = cleaned_text.split()

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Removing stop words from the tokenized words list
final_words = [word for word in tokenized_words if word not in stop_words]

# Get emotions text
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)

w = Counter(emotion_list)
print(w)

# Sort Counter object by emotion names
sorted_w = dict(sorted(w.items()))

# Print type and contents of sorted_w keys and values
print("Type of sorted_w keys:", type(sorted_w.keys())) #'sorted_w' is a dict. that holds emotions and used for analysis visualizing data 
print("Contents of sorted_w keys:", sorted_w.keys()) # keys are emotion names
print("Type of sorted_w values:", type(sorted_w.values())) # values are the counts of each emotion
print("Contents of sorted_w values:", sorted_w.values())

# Convert dict_keys to a list
x_values = list(sorted_w.keys()) 
y_values = list(sorted_w.values())

# Print after sorting
print("Emotion List:", emotion_list)
print("Sorted Keys:", x_values)

fig, ax1 = plt.subplots()
ax1.bar(x_values, y_values)
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
