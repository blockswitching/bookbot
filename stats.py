import re
from collections import Counter


# Returns the total number of words in the given text.
def get_num_words(text):
    words = text.split()
    return len(words)


# Counts the number of sentences by splitting on sentence-ending punctuation.
def get_num_sentences(text):
    sentences = re.split(r'[.!?]+', text)
    # Filter out empty strings from the split
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)


# Calculates the average word length (in characters).
def get_avg_word_length(text):
    words = text.split()
    if not words:
        return 0.0
    total_chars = sum(len(word.strip(".,!?;:'\"()-")) for word in words)
    return round(total_chars / len(words), 2)


# Returns the N longest unique words (alphabetic only, lowercased).
def get_longest_words(text, n=5):
    words = set(
        re.sub(r'[^a-z]', '', w.lower())
        for w in text.split()
    )
    words = [w for w in words if len(w) > 0]
    words.sort(key=len, reverse=True)
    return words[:n]


# Returns the N shortest unique words (alphabetic only, lowercased, min length 2).
def get_shortest_words(text, n=5):
    words = set(
        re.sub(r'[^a-z]', '', w.lower())
        for w in text.split()
    )
    words = [w for w in words if len(w) >= 2]
    words.sort(key=len)
    return words[:n]


# Estimates reading time based on average reading speed of 200 words per minute.
def get_reading_time(text):
    num_words = get_num_words(text)
    minutes = num_words / 200
    if minutes < 1:
        return "Less than a minute"
    hours = int(minutes // 60)
    remaining_minutes = int(minutes % 60)
    if hours > 0:
        return f"{hours} hr {remaining_minutes} min"
    return f"{remaining_minutes} min"


# Returns the top N most frequent words (case-insensitive, alphabetic only).
def get_top_words(text, n=10):
    words = re.findall(r'[a-z]+', text.lower())
    word_counts = Counter(words)
    return word_counts.most_common(n)


# Counts occurrences of every character in the text (case-insensitive).
def count_characters(text):
    my_dict = {}
    for characters in text:
        characters = characters.lower()
        if characters in my_dict:
            my_dict[characters] += 1
        else:
            my_dict[characters] = 1
    return my_dict


# Helper function used for sorting character dictionaries.
def sort_on(item):
    return item["num"]


# Converts the count dictionary into a sorted list of {"char": ..., "num": ...}
# sorted in descending order of frequency.
def sort_characters(count):
    sorted_ch = [{"char": ch, "num": num} for ch, num in count.items()]
    sorted_ch.sort(key=sort_on, reverse=True)
    return sorted_ch
