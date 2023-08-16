from textblob import TextBlob


def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment

    if sentiment.polarity > 0:
        return "Positive"
    elif sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"


input_text = input("Enter a text: ")
result = analyze_sentiment(input_text)
print("Sentiment:", result)
