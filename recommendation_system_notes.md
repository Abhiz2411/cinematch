# 🎯 Main Logic of the Recommendation System

---

## 📌 Cosine Similarity

1. We will use **cosine similarity** to find the similarity between movies.  
2. Cosine similarity is a **metric** used to measure how similar two vectors are.  
3. It is calculated as the **cosine of the angle between two vectors**.  
4. The formula is:
   \[
   \text{Cosine Similarity} = \frac{A \cdot B}{\|A\| \cdot \|B\|}
   \]
5. The result is a value between **0 and 1** (closer to 1 means more similar).

---

## 📊 Getting Vectors from Text

6. To compute cosine similarity, we need **vectors**.  
7. These vectors represent text data and contain values ranging from **0 to 1**.  
8. How do we get these vectors from text columns?  
9. We **count the frequency of each word** in the combined text column called 'tags'
    tags column will be concatenation of columns overview, genres, keywords, cast and crew
10. Then divide by total words in the column → gives **normalized frequency**.

---

## 🧰 Bag of Words (BoW)

11. This technique is known as the **Bag of Words model**.  
12. Bag of Words converts **text data into numerical data** based on word frequency.

---

## 🧹 Stop Words

13. Some common words (e.g., *the*, *is*, *are*) are **not useful** for recommendations.  
14. These words appear in almost all movies and don't help distinguish them.  
15. So, we **remove stop words** from the text columns.  
16. We will use the **NLTK library** for this.  
17. NLTK is used for **natural language processing (NLP)**.  
18. It has a pre-defined list of stop words we can filter out.

---

## 🌱 Stemming

19. A word can appear in different forms:  
    - e.g., *play*, *playing*, *played*  
20. These are variations of the same root concept.  
21. So, we apply **stemming** to convert words to their **root form**.  
22. Stemming helps in reducing word redundancy.  
23. Again, we’ll use **NLTK** for this.  
24. It provides a **PorterStemmer**, a popular stemming algorithm.  
25. **PorterStemmer** reduces words to their base/root forms.

---

## 🧠 TF-IDF Vectorizer

26. Instead of simple frequency, we use **TF-IDF Vectorizer** for better accuracy.  
27. **TF-IDF** stands for **Term Frequency - Inverse Document Frequency**.  
28. It’s a widely used method to convert text into numerical data.  
29. **TF** measures how frequently a term appears in a document.  
30. **IDF** reduces the weight of terms that appear in **many documents**.  
31. Combined, TF-IDF highlights **important and unique words**.

---

## 🔍 Similarity Calculation

32. Once we have the TF-IDF matrix, we use **cosine similarity** to compute pairwise similarity between movies.  
33. We will use the **scikit-learn (`sklearn`) library** to do this.  
34. **Scikit-learn** is a Python library used for **machine learning**.  
35. It provides a built-in `cosine_similarity` function to compare vectors.