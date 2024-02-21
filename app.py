import streamlit as st
import nltk
from nltk.corpus import words
from enchant.utils import levenshtein

nltk.download("words")

english_words = set(words.words())

class editDistance():
    def __init__(self, misspelled_word, content):
        self.misspelled = misspelled_word
        self.content = content
        
    def get_unique_words(self):
        return self.content.split()
        
    def edit_distance(self, word2):
        calculted_distance = levenshtein(self.misspelled, word2)
        return calculted_distance
    
    def suggest_correct_word(self):
        unique_list = self.get_unique_words()

        set_distance = set()
        for word in unique_list:
            tup = ((word, self.edit_distance(word)))
            set_distance.add(tup)
        min_distance_word = min(set_distance, key = lambda x: x[1])[0]
        return min_distance_word

def rule_based_spelling_correction(input_text):
    
    return input_text

def main():
    st.title("Spelling Check App")
    
    data = open('words_alpha.txt', 'r')
    content=data.read()

    user_input = st.text_area("Enter some text:")
    
    suggested_word = editDistance(user_input, content)
    suggested_word = suggested_word.suggest_correct_word()

    method = st.selectbox("Select Spelling Correction Method", ["Rule-Based", "Edit Distance Based"])

    if method == "Rule-Based":
        corrected_text = rule_based_spelling_correction(user_input)
    elif method == "Edit Distance Based":
        corrected_text = suggested_word
    else:
        st.error("Invalid method selected")

    st.subheader("Corrected Text:")
    st.write(corrected_text)

if __name__ == "__main__":
    main()

