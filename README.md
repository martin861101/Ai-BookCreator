# 🥧 Python Pie Book Generator

**A whimsical and practical tool for generating a Python programming book using pie and baking metaphors, powered by the Gemini API.**

---

## 📖 About

This project uses Google's **Gemini 2.5 Flash** model to automatically generate an entire ebook by providing the System a single title & description.

> **Building Blocks: Guide To Python, One Pie At A Time**

Takes 10 minutes to write a 24 chapter book and then generates a cover using AI text to image based on the book title or story.

## 🚀 Features

- Generates a complete book outline with Gemini API
- Parses structured chapters with detailed prompts
- Writes full chapters (3000-4000 words) with examples, metaphors, and exercises
- Produces introduction and conclusion sections
- Saves all content in neatly structured `.txt` files
- Compiles/Merges .txt files into one comprehensive PDF ebook.
- Fully automatic with minimal user input
- Friendly CLI interface with progress indicators

---

## 🧰 Requirements

- Python 3.8+
- `google-generativeai`
- `python-dotenv`

Install dependencies:

```bash
pip install google-generativeai python-dotenv
```

---

## 🔑 Setup

1. **Get a Gemini API key** from [Google AI Studio](https://makersuite.google.com/app).
2. Create a `.env` file in your root directory:

```
GEMINI_API_KEY=your_api_key_here
```

---

## 🏁 Usage

```bash
python python_pie_book_generator.py
```

- If `.env` is configured, it auto-loads your API key.
- If not, you'll be prompted to enter it manually.
- Outputs are saved in the `python_pie_book/` directory.

You’ll be asked to confirm before generation starts.

---

## 📂 Output Structure

```
python_pie_book/
├── 01_outline.txt
├── 02_introduction.txt
├── 03_chapter_01.txt
├── ...
├── 17_conclusion.txt
├── COMPLETE_BOOK.txt
└── generation_summary.txt
```

---

## 🎯 Book Structure

Each chapter includes:

1. Baking-themed introduction
2. 3–4 main sections with Python code
3. A "recipe"/project
4. Chapter summary
5. Exercises

---

## 🧁 Example Chapter Titles

- Getting Started: Your First Pie Crust
- Mixing the Ingredients: Working with Data
- Following the Recipe: Control Flow
- Custom Recipes: Functions
- The Baker’s Toolkit: Modules and Libraries

---

## 🙌 Acknowledgments

Built with ❤️ and a pinch of curiosity by leveraging:

- [Google Gemini API](https://ai.google.dev)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 📘 License

MIT License. Use it, fork it, bake it, remix it! 🥧

---

## 💡 Tip

For best results, run during off-peak hours to avoid API rate limits.

---
