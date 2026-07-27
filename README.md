# 📊 Social Media Sentiment Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NLP](https://img.shields.io/badge/NLP-Sentiment%20Analysis-green)
![Status](https://img.shields.io/badge/Project-Completed-success)

## 📌 Project Overview

Social media platforms generate a huge amount of text every day, containing valuable information about people's opinions, emotions, attitudes, and reactions toward different topics, products, services, and brands.

This project focuses on analyzing and visualizing sentiment patterns in social media data to understand public opinion and attitudes toward specific topics or brands.

Natural Language Processing (NLP) techniques are applied to process and analyze social media posts. The text data is cleaned and preprocessed before sentiment analysis is performed. Each post is classified into sentiment categories such as **Positive, Negative, or Neutral**.

Data visualization techniques are then used to identify sentiment patterns, popular topics, and frequently occurring words.

This project was completed as part of the **PRODIGY InfoTech Data Science Internship – Task 04**.

---

## 🎯 Objective

The main objective of this project is to analyze social media data and understand public opinions and attitudes toward different topics and brands.

The project aims to:

- Analyze social media posts and public opinions.
- Clean and preprocess textual data.
- Apply Natural Language Processing techniques.
- Perform sentiment analysis on social media text.
- Classify posts into Positive, Negative, and Neutral categories.
- Analyze sentiment patterns across different topics.
- Identify frequently discussed topics and brands.
- Visualize sentiment distributions using charts.
- Generate word clouds to identify frequently used words.
- Export the analyzed results for further analysis.

---

## 🧠 What is Sentiment Analysis?

Sentiment analysis is a Natural Language Processing technique used to identify and understand the emotional tone or opinion expressed in a piece of text.

It is commonly used to analyze:

- Customer reviews
- Social media posts
- Product feedback
- Brand opinions
- Customer satisfaction
- Public opinion
- Online discussions

In this project, sentiment analysis is used to classify social media posts into three categories:

### 🟢 Positive

Posts that express positive opinions, satisfaction, happiness, or appreciation.

### 🔴 Negative

Posts that express negative opinions, dissatisfaction, criticism, or complaints.

### ⚪ Neutral

Posts that do not express a clearly positive or negative opinion.

---

## 🛠️ Technologies and Libraries Used

The following technologies and Python libraries are used in this project:

| Technology / Library | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data loading, cleaning, and manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical data visualization |
| NLTK | Natural Language Processing and stopword removal |
| TextBlob | Sentiment polarity analysis |
| WordCloud | Visualization of frequently used words |

---

## 📊 Dataset

The project uses a social media sentiment dataset containing information about different topics, sentiment labels, and social media posts.

The dataset includes information such as:

- **ID** – Unique identifier for each record
- **Topic** – Topic or brand associated with the social media post
- **Sentiment** – Sentiment category
- **Tweet** – Social media post text

### Dataset Source

The dataset was provided as part of the **PRODIGY InfoTech Data Science Internship – Task 04**.

---

## 📂 Project Structure

```text
PRODIGY_DS_04/
│
├── sentiment_analysis.py
├── sentiment_results.csv
├── twitter_training.csv
└── README.md
