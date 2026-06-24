import sys
from stats import (
    get_num_words,
    get_num_sentences,
    get_avg_word_length,
    get_longest_words,
    get_shortest_words,
    get_reading_time,
    get_top_words,
    count_characters,
    sort_characters,
)


def get_book_text(path):
    """Reads the entire book text from the given file path."""
    with open(path) as f:
        return f.read()


def print_header(title):
    """Prints a formatted section header."""
    print(f"\n{'─' * 40}")
    print(f"  {title}")
    print(f"{'─' * 40}")


def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)

    print("╔════════════════════════════════════════╗")
    print("║            📖 BOOKBOT v2.0            ║")
    print("╠════════════════════════════════════════╣")
    print(f"║  Analyzing: {book_path:<26}║")
    print("╚════════════════════════════════════════╝")

    # --- Summary Stats ---
    print_header("📊 Summary")
    num_words = get_num_words(text)
    num_sentences = get_num_sentences(text)
    avg_word_len = get_avg_word_length(text)
    reading_time = get_reading_time(text)

    print(f"  Words:              {num_words:,}")
    print(f"  Sentences:          {num_sentences:,}")
    print(f"  Avg word length:    {avg_word_len} characters")
    print(f"  Est. reading time:  {reading_time}")

    # --- Top Words ---
    print_header("🔤 Top 10 Most Frequent Words")
    top_words = get_top_words(text, 10)
    for rank, (word, count) in enumerate(top_words, 1):
        bar = "█" * min(count // (num_words // 50 or 1), 20)
        print(f"  {rank:>2}. {word:<15} {count:>6,}  {bar}")

    # --- Longest & Shortest Words ---
    print_header("📏 Longest Words")
    longest = get_longest_words(text, 5)
    for word in longest:
        print(f"  • {word} ({len(word)} chars)")

    print_header("📐 Shortest Words")
    shortest = get_shortest_words(text, 5)
    for word in shortest:
        print(f"  • {word} ({len(word)} chars)")

    # --- Character Frequency ---
    print_header("🔡 Character Frequency")
    count = count_characters(text)
    sorted_chars = sort_characters(count)

    for item in sorted_chars:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():
            print(f"  {ch}: {num:,}")

    # --- Footer ---
    print(f"\n{'═' * 42}")
    print("  Analysis complete. Happy reading!")
    print(f"{'═' * 42}\n")


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()
