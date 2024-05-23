SENTIMENT ANALYSIS 
    Code for the AMS Engineering Teamwork Course

AUTHORS:
    Jonathan Estephan
    Matriculation Number: 3119742

CODE
**Lists
    1 - final_words is used to get rid of any irrelevant words (stop_words) from the analysis.
    2 - stop_words contains all unnecessary words consisting of pronouns, articles and common verbs.
    3 - emotion_list opens the emotions.txt file in order to read non stop_words and analyse the emotions behind the words.
**Functions
    1 - get_tweets (), which is imported from GetOldTweets3, retrieves a list of tweet texts related to the "CoronaOutbreak" between January and April 1 of 2020.
    2 - sentiment_analyse(sentiment_text) is defined to perform sentiment analysis on the provided 'sentiment_text'. SentimentIntensityAnalyzer().polarity_scores(sentiment_text) is used to get the sentiment scores for the text. This method returns a dictionary with the following keys:
        'neg': Negative sentiment score.
        'neu': Neutral sentiment score.
        'pos': Positive sentiment score.
        'compound': Compound sentiment score, which combines the others into a single value.
    
