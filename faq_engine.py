import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class FAQEngine:
    def __init__(self, faqs, threshold=0.20):
        if not faqs:
            raise ValueError("FAQ dataset is empty.")
        self.faqs = faqs
        self.threshold = threshold
        self.vectorizer = TfidfVectorizer(
            preprocessor=self.preprocess, ngram_range=(1, 2), sublinear_tf=True
        )
        self.faq_matrix = self.vectorizer.fit_transform([x["question"] for x in faqs])

    @staticmethod
    def preprocess(text):
        text = text.lower()
        text = re.sub(r"[^a-z0-9\\s]", " ", text)
        return re.sub(r"\\s+", " ", text).strip()

    def get_answer(self, question):
        if not self.preprocess(question):
            return {"answer": "Please ask a question using a few words.",
                    "matched_question": None, "confidence": 0, "matched": False}
        vector = self.vectorizer.transform([question])
        scores = cosine_similarity(vector, self.faq_matrix).flatten()
        index = int(scores.argmax())
        score = float(scores[index])
        if score < self.threshold:
            return {
                "answer": "Sorry, I couldn't find a reliable answer. Please try rephrasing your question or contact the relevant office.",
                "matched_question": None, "confidence": round(score * 100, 1),
                "matched": False
            }
        item = self.faqs[index]
        return {
            "answer": item["answer"], "matched_question": item["question"],
            "category": item.get("category", "General"),
            "confidence": round(score * 100, 1), "matched": True
        }
