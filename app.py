import google.generativeai as genai
import time
import os
from datetime import datetime
import json
from dotenv import load_dotenv

class PythonBookGenerator:
    def __init__(self, api_key=None):
        """Initialize the book generator with Gemini API."""
        # Load environment variables
        load_dotenv()
        
        # Use provided API key or get from environment
        if api_key is None:
            api_key = os.getenv('GEMINI_API_KEY')
            
        if not api_key:
            raise ValueError("Gemini API key not found. Please set GEMINI_API_KEY in .env file or provide it directly.")
            
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        self.book_title = "Building Blocks: Guide To Python, One Pie At A Time"
        self.chapters = []
        self.delay_between_requests = 5  # seconds to avoid rate limits
        
    def generate_book_outline(self):
        """Generate a comprehensive outline for the Python book."""
        print("🔍 Generating book outline...")
        
        outline_prompt = f"""
        Create a detailed outline for a Python programming book titled "{self.book_title}".
        
        The book should use pie/baking metaphors throughout to make Python concepts accessible and fun.
        Include:
        - 12-15 chapters covering Python from basics to intermediate concepts
        - Each chapter should have 3-5 main sections
        - Use cooking/baking analogies to explain programming concepts
        - Progress from basic ingredients (variables) to complex recipes (functions, classes, etc.)
        - Include practical projects that build throughout the book
        
        Format as a structured outline with chapter titles and brief descriptions.
        Make it comprehensive but approachable for beginners.
        """
        
        try:
            response = self.model.generate_content(outline_prompt)
            outline = response.text
            print("✅ Book outline generated!")
            return outline
        except Exception as e:
            print(f"❌ Error generating outline: {e}")
            return None
    
    def generate_chapter(self, chapter_num, chapter_title, chapter_description, previous_context=""):
        """Generate a full chapter with detailed content."""
        print(f"📝 Generating Chapter {chapter_num}: {chapter_title}...")
        
        chapter_prompt = f"""
        Write a complete chapter for the Python book "{self.book_title}".
        
        Chapter {chapter_num}: {chapter_title}
        Description: {chapter_description}
        
        Requirements:
        - Write 3000-4000 words for this chapter
        - Use pie/baking metaphors consistently throughout
        - Include practical Python code examples
        - Add exercises at the end of each major section
        - Make it beginner-friendly but comprehensive
        - Include real-world applications
        - Use humor and engaging analogies
        
        Previous context: {previous_context[:500] if previous_context else "This is the first chapter."}
        
        Structure:
        1. Chapter introduction with baking metaphor
        2. 3-4 main sections with code examples
        3. Practical project/recipe
        4. Chapter summary
        5. Exercises (3-5 problems)
        
        Write in a conversational, encouraging tone. Make Python feel as approachable as baking a pie!
        """
        
        try:
            response = self.model.generate_content(chapter_prompt)
            chapter_content = response.text
            print(f"✅ Chapter {chapter_num} completed!")
            return chapter_content
        except Exception as e:
            print(f"❌ Error generating chapter {chapter_num}: {e}")
            return None
    
    def parse_outline_to_chapters(self, outline):
        """Extract chapter information from the generated outline."""
        print("🔍 Parsing outline into chapters...")
        
        parse_prompt = f"""
        Parse this book outline and extract exactly the chapter titles and descriptions:
        
        {outline}
        
        Return ONLY a JSON array of objects with this exact format:
        [
          {{"title": "Chapter Title", "description": "Brief description of what this chapter covers"}},
          ...
        ]
        
        No additional text, just the JSON array.
        """
        
        try:
            response = self.model.generate_content(parse_prompt)
            chapters_json = response.text.strip()
            
            # Clean up the response to extract JSON
            if "```json" in chapters_json:
                chapters_json = chapters_json.split("```json")[1].split("```")[0].strip()
            elif "```" in chapters_json:
                chapters_json = chapters_json.split("```")[1].strip()
            
            chapters = json.loads(chapters_json)
            print(f"✅ Parsed {len(chapters)} chapters from outline!")
            return chapters
        except Exception as e:
            print(f"❌ Error parsing outline: {e}")
            # Fallback with default chapters
            return self.get_default_chapters()
    
    def get_default_chapters(self):
        """Fallback chapter structure if outline parsing fails."""
        return [
            {"title": "Getting Started: Your First Pie Crust", "description": "Introduction to Python basics, variables, and data types"},
            {"title": "Mixing the Ingredients: Working with Data", "description": "Lists, dictionaries, and basic data manipulation"},
            {"title": "Following the Recipe: Control Flow", "description": "If statements, loops, and program flow control"},
            {"title": "Custom Recipes: Functions", "description": "Creating and using functions in Python"},
            {"title": "The Baker's Toolkit: Modules and Libraries", "description": "Importing and using Python modules"},
            {"title": "Organizing Your Kitchen: File Handling", "description": "Reading, writing, and managing files"},
            {"title": "Advanced Techniques: Object-Oriented Baking", "description": "Classes, objects, and OOP concepts"},
            {"title": "Handling Kitchen Disasters: Error Management", "description": "Exception handling and debugging"},
            {"title": "The Professional Kitchen: Best Practices", "description": "Code style, documentation, and testing"},
            {"title": "Sharing Your Recipes: Final Projects", "description": "Building complete applications and next steps"}
        ]
    
    def save_progress(self, filename, content):
        """Save generated content to file."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"💾 Saved progress to {filename}")
        except Exception as e:
            print(f"❌ Error saving to {filename}: {e}")
    
    def generate_introduction_and_conclusion(self):
        """Generate book introduction and conclusion."""
        print("📖 Generating introduction and conclusion...")
        
        intro_prompt = f"""
        Write a compelling introduction for "{self.book_title}".
        
        Include:
        - Welcome message to readers
        - Why Python is like baking
        - What readers will learn
        - How to use this book
        - Encouragement for beginners
        
        Make it warm, welcoming, and exciting. About 800-1000 words.
        """
        
        conclusion_prompt = f"""
        Write a motivating conclusion for "{self.book_title}".
        
        Include:
        - Congratulations to readers
        - Summary of journey
        - Next steps in Python learning
        - Resources for continued learning
        - Final encouragement
        
        About 600-800 words with a celebratory tone.
        """
        
        try:
            intro_response = self.model.generate_content(intro_prompt)
            time.sleep(self.delay_between_requests)
            
            conclusion_response = self.model.generate_content(conclusion_prompt)
            
            return intro_response.text, conclusion_response.text
        except Exception as e:
            print(f"❌ Error generating intro/conclusion: {e}")
            return None, None
    
    def generate_complete_book(self):
        """Generate the complete book with all chapters."""
        start_time = datetime.now()
        print(f"🚀 Starting book generation at {start_time.strftime('%H:%M:%S')}")
        print(f"📚 Book: {self.book_title}")
        print("=" * 60)
        
        # Create output directory
        output_dir = "python_pie_book"
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate outline
        outline = self.generate_book_outline()
        if outline:
            self.save_progress(f"{output_dir}/01_outline.txt", outline)
            time.sleep(self.delay_between_requests)
        
        # Parse chapters from outline
        chapter_info = self.parse_outline_to_chapters(outline) if outline else self.get_default_chapters()
        
        # Generate introduction and conclusion
        introduction, conclusion = self.generate_introduction_and_conclusion()
        if introduction:
            self.save_progress(f"{output_dir}/02_introduction.txt", introduction)
        time.sleep(self.delay_between_requests)
        
        # Generate each chapter
        full_book_content = []
        previous_content = ""
        
        if introduction:
            full_book_content.append(f"# {self.book_title}\n\n## Introduction\n\n{introduction}\n\n")
        
        for i, chapter_info_item in enumerate(chapter_info, 1):
            chapter_title = chapter_info_item['title']
            chapter_desc = chapter_info_item['description']
            
            # Generate chapter content
            chapter_content = self.generate_chapter(i, chapter_title, chapter_desc, previous_content)
            
            if chapter_content:
                # Save individual chapter
                chapter_filename = f"{output_dir}/{i+2:02d}_chapter_{i:02d}.txt"
                self.save_progress(chapter_filename, chapter_content)
                
                # Add to full book
                full_book_content.append(f"# Chapter {i}: {chapter_title}\n\n{chapter_content}\n\n")
                previous_content = chapter_content[-1000:]  # Keep last 1000 chars for context
            
            # Delay between chapters to avoid rate limits
            time.sleep(self.delay_between_requests)
            
            # Progress update
            elapsed = datetime.now() - start_time
            print(f"⏱️  Progress: {i}/{len(chapter_info)} chapters | Elapsed: {elapsed}")
        
        # Add conclusion
        if conclusion:
            self.save_progress(f"{output_dir}/{len(chapter_info)+3:02d}_conclusion.txt", conclusion)
            full_book_content.append(f"# Conclusion\n\n{conclusion}\n\n")
        
        # Save complete book
        complete_book = "\n".join(full_book_content)
        self.save_progress(f"{output_dir}/COMPLETE_BOOK.txt", complete_book)
        
        # Generate final summary
        end_time = datetime.now()
        total_time = end_time - start_time
        
        summary = f"""
📖 BOOK GENERATION COMPLETE! 📖

Title: {self.book_title}
Chapters Generated: {len(chapter_info)}
Start Time: {start_time.strftime('%H:%M:%S')}
End Time: {end_time.strftime('%H:%M:%S')}
Total Time: {total_time}

Files saved in: {output_dir}/
- Complete book: COMPLETE_BOOK.txt
- Individual chapters: chapter_XX.txt
- Introduction & Conclusion included

Word count estimate: {len(complete_book.split())} words
Character count: {len(complete_book)} characters

Your Python pie book is ready to serve! 🥧
        """
        
        print(summary)
        self.save_progress(f"{output_dir}/generation_summary.txt", summary)
        
        return complete_book

def main():
    """Main function to run the book generator."""
    print("🥧 Python Pie Book Generator 🥧")
    print("=" * 40)
    
    # Try to initialize generator with API key from .env
    try:
        generator = PythonBookGenerator()
        print("✅ Gemini API key loaded from .env file")
    except ValueError as e:
        print(f"❌ {e}")
        
        # Fallback to manual input
        api_key = input("Enter your Gemini API key manually: ").strip()
        if not api_key:
            print("❌ API key required!")
            return
        
        try:
            generator = PythonBookGenerator(api_key)
            print("✅ API key accepted")
        except Exception as e:
            print(f"❌ Error initializing generator: {e}")
            return
    
    # Confirm generation
    print(f"\n📚 About to generate: {generator.book_title}")
    print("⏱️  Estimated time: 45-60 minutes")
    print("💾 Files will be saved to: python_pie_book/")
    
    confirm = input("\nProceed with book generation? (yes/no): ").strip().lower()
    if confirm not in ['yes', 'y']:
        print("❌ Book generation cancelled.")
        return
    
    # Generate the book
    try:
        book_content = generator.generate_complete_book()
        print("\n🎉 SUCCESS! Your Python pie book has been generated!")
        
    except KeyboardInterrupt:
        print("\n⏸️  Book generation interrupted by user.")
        print("📁 Partial progress saved in python_pie_book/")
        
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("📁 Any generated content saved in python_pie_book/")

if __name__ == "__main__":
    main()
