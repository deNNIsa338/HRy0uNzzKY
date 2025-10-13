# 代码生成时间: 2025-10-13 23:21:32
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline

class TextSummaryGenerator:
    """
    A class for generating text summaries.
    """
    def __init__(self, text, summary_ratio=0.1):
        """
        Initialize the TextSummaryGenerator with a text and summary ratio.
        
        Args:
            text (str): The text to generate a summary for.
            summary_ratio (float): The ratio of the text to include in the summary.
        """
        self.text = text
        self.summary_ratio = summary_ratio
        self.summary = ""
        self.sentences = self.text.split(").")
        
    def generate_summary(self):
        """
        Generate a summary of the text.
        """
        try:
            # Preprocess the text
            self.sentences = [sentence.strip() + '.' for sentence in self.sentences if sentence.strip()]
            
            # Split the text into sentences
            if not self.sentences:
                raise ValueError("No sentences found in the text.")
            
            # Calculate TF-IDF scores for each sentence
            vectorizer = TfidfVectorizer(stop_words='english')
            sentence_vectors = vectorizer.fit_transform(self.sentences)
            
            # Calculate the similarity of each sentence to the overall text
            overall_text_vector = vectorizer.transform([self.text])
            similarities = cosine_similarity(overall_text_vector, sentence_vectors).flatten()
            
            # Get the indices of the top sentences based on their similarity
            top_sentence_indices = sorted(range(len(similarities)), key=lambda i: similarities[i], reverse=True)[:int(len(self.sentences) * self.summary_ratio)]
            
            # Join the top sentences to form the summary
            self.summary = ' '.join(self.sentences[i] for i in top_sentence_indices)
            
            return self.summary
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

# Example usage
if __name__ == "__main__":
    text = "This is a sample text. This text has multiple sentences. Each sentence has different information. This sentence is particularly important."
    generator = TextSummaryGenerator(text, summary_ratio=0.3)
    summary = generator.generate_summary()
    if summary:
        print("Summary: ", summary)
