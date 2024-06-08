from collections import Counter
import re

def word_counter_text_analysis(text):
    text = re.sub(r'[^\w\s]', '', text).lower()
    words = text.split()
    word_counter = Counter(words)
    sequential_words = sorted(word_counter.items(), key=lambda x: x[1], reverse=True)
    return sequential_words

def word_emulation(words, n):
    words_nli = zip(*[words[i:] for i in range(n)])
    word_counter = Counter(words_nli)
    sequential_words = sorted(word_counter.items(), key=lambda x: x[1], reverse=True)
    return sequential_words

def sentence_counter_text_analysis(text):
    sentences = re.split(r'[.!?]', text)
    sentences = [sentence.strip().lower() for sentence in sentences if sentence.strip()]
    sentence_counter = Counter(sentences)
    sequential_sentences = sorted(sentence_counter.items(), key=lambda x: x[1], reverse=True)
    return sequential_sentences

file_name = 'your-file.txt'

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        word_list = word_counter_text_analysis(text)
        binary_word_list = word_emulation(words, 2)
        triple_word_list = word_emulation(words, 3)
        sentence_list = sentence_counter_text_analysis(text)
        
        print("Total number of words:", len(words))
        print("Total number of different words:", len(word_list))
        print("Most used words:")
        for word, number in word_list[:10]:
            print(f"'{word}' word used {number} times")
        
        print("\nThe most used binary phrases:")
        for binary, number in binary_word_list[:10]:
            print(f"'{' '.join(binary)}' phrase used {number} times")
            
        print("\nThe most used triplet phrases:")
        for triple, number in triple_word_list[:10]:
            print(f"'{' '.join(triple)}' phrase used {number} times")

        print("\nMost used sentences:")
        for sentence, number in sentence_list[:10]:
            print(f"{sentence} sentence used {number} times")
except FileNotFoundError:
    print(f"{file_name} file not found")

