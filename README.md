# 📚 Natural Language Processing (NLP) Projects Repository 🗣️

Welcome to my Natural Language Processing (NLP) Projects Repository! This collection includes various NLP techniques, focusing on text preprocessing, document similarity, embeddings, and recommendation systems. Each project is implemented in Jupyter Notebooks, covering data preprocessing, feature extraction, model training, and evaluation.

📌 Key Features

✔️ Covers text processing, sentiment analysis, document similarity, and classification.

✔️ Uses real-world text datasets for building NLP applications.

✔️ Implements TF-IDF, Word Embeddings, FastText, and Machine Learning Models.

✔️ Deep learning techniques applied in sentiment analysis and recommendation systems.

# 📂 Project Overview

## 1. Sentiment Analysis on Movie Reviews

📌 Objective: Classify movie reviews as positive or negative using Natural Language Processing (NLP) techniques.

🔹 Models Used
  - Convolutional Neural Networks (CNNs) – Leverages convolutional filters to capture local patterns in text.
  - Recurrent Neural Networks (RNNs) – Designed for sequential data processing:
  - GRU (Gated Recurrent Units) – Efficiently captures sequential dependencies with fewer parameters.
  - LSTM (Long Short-Term Memory) – Captures long-term dependencies in text sequences.
  - Stacked LSTM – A multi-layered LSTM model for learning hierarchical representations.

🔗 File: 1_NLP_Movie_Review_Sentiment_Analysis.ipynb

## 2. Movie Recommendation System using Document Similarity

📌 Objective: Build a content-based movie recommendation system by analyzing movie descriptions and finding similar movies using text similarity techniques.

🔹 Methods Used:
  - TF-IDF for text vectorization.
  - Cosine Similarity to measure similarity between movie descriptions.
  - Pairwise Document Similarity for recommendation generation.

✔️ Outcome: A content-based recommender system that suggests similar movies based on textual similarity.

🔗 File: 2_NLP_Movie_Recommendation_System.ipynb

## 3.  Language Detector

🔹 Introduction: Language detection is a fundamental task in Natural Language Processing (NLP), aimed at identifying the language of a given text. This project builds a machine learning-based language detection model to classify text into multiple languages.

🔹 Methodology
  - Text Preprocessing
  - Model Training
  - Evaluation & Performance Metrics

🔍 Conclusion: CountVectorizer Outperform TF-IDF in Language Detection
why?

- Language detection focus on detecting common features of an language, rather than some important features. 
- CountVectorizer is better to capture patterns in certain language like:
   - Common words: "el", "de", "la" (Spanish); "le", "de", "la" (French).
   - Character n-grams: "th", "he", "ing" (English); "en", "de", "que" (Spanish).
- TF-IDF would reduce the weight of these patterns since they are frequent across documents, potentially reducing the model's ability to distinguish between languages. TF-IDF de-emphasizes common features of languages.

In short, TF-IDF is great for topic-related tasks, while CountVectorizer is better for capturing linguistic structures, making it the better choice for language detection.

🔗 Folder: NLP_Language_Detector/

