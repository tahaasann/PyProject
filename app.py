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

file_name = 'words.txt'

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        
        # Kelime analizi
        word_list = word_counter_text_analysis(text)
        binary_word_list = word_emulation(words, 2)
        triple_word_list = word_emulation(words, 3)
        
        # Cümle analizi
        sentence_list = sentence_counter_text_analysis(text)
        
        # Sonuçları yazdırma
        #print("En çok kullanılan kelimeler:")
        #for word, number in word_list[:10]:
        #    print(f"{word}: {number}")
        
        #print("\nEn çok kullanılan ikili kelime grupları:")
        #for binary, number in binary_word_list[:10]:
        #    print(f"{' '.join(binary)}: {number}")
            
        #print("\nEn çok kullanılan üçlü kelime grupları:")
        #for triple, number in triple_word_list[:10]:
        #    print(f"{' '.join(triple)}: {number}")
            
        print("\nEn çok kullanılan cümleler:")
        for sentence, number in sentence_list[:10000]:
            print(f"{sentence}: {number}")

except FileNotFoundError:
    print(f"{file_name} file not found")
