📖 AI Story Generator
Every Choice Creates a New Story
💭 The Idea

This project started with a simple question I kept thinking about: "What if a story wasn't written just once, but regenerated every time based on the reader's own choices?"

I wanted to turn that idea into something real, combining my love for storytelling with what I've been learning in my AI major. The result is this simple tool: it asks you five questions, and based on your answers, it generates a short, unique story — one that never repeats, even if the same person tries it twice.

The project is intentionally simple. The goal wasn't to build something overly complex on my first try, but to genuinely understand and apply how generative AI integrates with straightforward programming logic.

⚙️ How It Works
The program asks the user 5 questions:
Story type
Location
The main character's age
The character's goal
The type of ending they want
The answers are automatically turned into a carefully structured prompt, which is passed to a generative AI model.
The model returns a complete story (250–350 words, divided into 5–7 paragraphs) built entirely around the user's choices — with a clear beginning, main events, and ending.
🛠️ Tech Stack
Technology	Purpose
Python	Core programming language for the entire project
Google Gemini API	The generative model responsible for writing the story
google-generativeai	Python library used to communicate with the Gemini API
python-dotenv	Manages the API key securely, keeping it out of the source code
f-strings	Used to dynamically build the prompt from the user's answers


🚀 How to Run It Locally

1. Download the project and navigate into its folder

2. Install the required libraries:

bash
pip install -r requirements.txt

3. Get a free API key from Google AI Studio

4. Create a .env file in the same folder and add:

GOOGLE_API_KEY=your_key_here

5. Run the program:

bash
python main.py

Answer the five questions, and enjoy your own generated story ✨

🌱 Why This Project Matters to Me

As an AI major, it was important to me not to stop at just the theory. I wanted to see how a concept like Prompt Engineering could turn into something real that anyone could use and see a tangible result from.

This is my first project of its kind, and I ran into real challenges along the way (like access issues with some commercial models). I learned to research alternatives, read documentation, and implement things step by step on my own. For me, the real value isn't just in the final code — it's in the process that got me there.

🔮 Future Improvements
Add a simple graphical interface instead of terminal-based interaction
Save generated stories to a text file or a lightweight database
Add a "regenerate" option in case the user doesn't like the first story
Support generating stories in multiple languages (Arabic/English)

Built by Ghaidaa Alzahrani, AI student at Imam Abdulrahman Bin Faisal University.