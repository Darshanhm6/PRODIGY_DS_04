import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
import string

# Download NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

# Load Dataset
df = pd.read_csv("twitter_training.csv", header=None)

# Rename Columns
df.columns = ['ID','Topic','Sentiment','Tweet']

# Remove missing values
df.dropna(inplace=True)

# Function to clean text
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()

    text = ''.join([char for char in text if char not in string.punctuation])

    words = text.split()

    words = [word for word in words if word not in stop_words]

    return " ".join(words)

df['Clean_Tweet'] = df['Tweet'].astype(str).apply(clean_text)

# Function to calculate sentiment polarity
def get_polarity(text):
    return TextBlob(text).sentiment.polarity

df['Polarity'] = df['Clean_Tweet'].apply(get_polarity)

# Classify sentiment
def classify_sentiment(score):
    if score > 0:
        return 'Positive'
    elif score < 0:
        return 'Negative'
    else:
        return 'Neutral'

df['Predicted_Sentiment'] = df['Polarity'].apply(classify_sentiment)

print(df.head())

# -----------------------------
# Visualization 1
# -----------------------------
plt.figure(figsize=(8,5))

sns.countplot(
    x='Predicted_Sentiment',
    data=df,
    palette='Set2'
)

plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")

plt.show()

# -----------------------------
# Visualization 2
# -----------------------------
plt.figure(figsize=(10,6))

sns.countplot(
    y='Topic',
    data=df,
    order=df['Topic'].value_counts().index[:10],
    palette='viridis'
)

plt.title("Top 10 Topics")

plt.show()

# -----------------------------
# Visualization 3
# -----------------------------
positive_text = " ".join(df[df['Predicted_Sentiment']=="Positive"]['Clean_Tweet'])

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white'
).generate(positive_text)

plt.figure(figsize=(12,6))

plt.imshow(wordcloud)

plt.axis("off")

plt.title("Positive Tweets Word Cloud")

plt.show()

# -----------------------------
# Visualization 4
# -----------------------------
negative_text = " ".join(df[df['Predicted_Sentiment']=="Negative"]['Clean_Tweet'])

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='black'
).generate(negative_text)

plt.figure(figsize=(12,6))

plt.imshow(wordcloud)

plt.axis("off")

plt.title("Negative Tweets Word Cloud")

plt.show()

# Save Results
df.to_csv("sentiment_results.csv", index=False)

print("\nAnalysis Completed Successfully!")
print("Results saved as sentiment_results.csv")