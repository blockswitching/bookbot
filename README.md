# **BookBot v2.0**

BookBot is a command-line tool that analyzes a text file (such as a book) and generates a detailed statistical report. Originally built as a [Boot.dev](https://www.boot.dev) project, now enhanced with additional analysis features.

---

## **Features**

- Total word and sentence count
- Average word length calculation
- Estimated reading time (based on 200 wpm)
- Top 10 most frequent words with visual bar chart
- Longest and shortest words in the text
- Character frequency analysis (case-insensitive, alphabetic only)
- Clean, formatted terminal output with section headers

---

## **Project Structure**

```
bookbot/
├── main.py        # CLI entry point and report display
├── stats.py       # Text analysis functions
└── README.md      # Documentation
```

---

## **Usage**

```bash
python3 main.py <path_to_text_file>
```

**Example:**

```bash
python3 main.py books/frankenstein.txt
```

If no argument is provided:

```
Usage: python3 main.py <path_to_book>
```

---

## **Example Output**

```
╔════════════════════════════════════════╗
║            📖 BOOKBOT v2.0            ║
╠════════════════════════════════════════╣
║  Analyzing: books/frankenstein.txt    ║
╚════════════════════════════════════════╝

────────────────────────────────────────
  📊 Summary
────────────────────────────────────────
  Words:              77,986
  Sentences:          3,204
  Avg word length:    4.56 characters
  Est. reading time:  6 hr 29 min

────────────────────────────────────────
  🔤 Top 10 Most Frequent Words
────────────────────────────────────────
   1. the            4,842  ████████████████████
   2. and            3,028  ████████████
   3. i              2,798  ███████████
   ...

────────────────────────────────────────
  📏 Longest Words
────────────────────────────────────────
  • accomplishments (15 chars)
  • representations (15 chars)
  ...

════════════════════════════════════════
  Analysis complete. Happy reading!
════════════════════════════════════════
```

---

## **How It Works**

### **main.py**
- Reads the file path from command-line arguments
- Calls analysis functions from `stats.py`
- Displays a formatted report with all statistics

### **stats.py**

| Function | Description |
|----------|-------------|
| `get_num_words(text)` | Counts total words |
| `get_num_sentences(text)` | Counts sentences (splits on `.!?`) |
| `get_avg_word_length(text)` | Average character count per word |
| `get_longest_words(text, n)` | Returns the N longest unique words |
| `get_shortest_words(text, n)` | Returns the N shortest unique words (min 2 chars) |
| `get_reading_time(text)` | Estimates reading time at 200 wpm |
| `get_top_words(text, n)` | Top N most frequent words |
| `count_characters(text)` | Character frequency (case-insensitive) |
| `sort_characters(count)` | Sorts characters by frequency descending |

---

## **Requirements**

- Python 3.6+
- A plain text file to analyze
- No external dependencies required
