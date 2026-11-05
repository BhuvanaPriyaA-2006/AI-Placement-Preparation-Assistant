💼 AI Placement Preparation Assistant
An AI-powered application that helps students and job seekers prepare for technical interviews through personalized questions, answers, explanations, and practical examples.

📌 About the Project
The AI Placement Preparation Assistant uses an AI language model to generate interview questions based on the user's selected job role, experience level, difficulty, and number of questions.
Each question includes a model answer, explanation, practical example, simple implementation, important keywords, and a follow-up question.

✨ Key Features
- Supports multiple technical job roles.
- Offers four experience levels.
- Provides different difficulty levels.
- Generates 3–15 interview questions.
- Includes AI-generated answers and explanations.
- Provides practical examples and simple implementations.
- Highlights important keywords and follow-up questions.
- Allows downloading questions in JSON format.

🛠️ Technologies Used
- Python
- Streamlit
- LangChain
- OpenRouter API
- Pydantic
- Python-dotenv
- JSON

📂 Project Structure
```text
AI-Placement-Preparation-Assistant/
│
├── .streamlit/
│   └── config.toml
│
├── app.py
├── generator.py
├── prompts.py
├── schemas.py
├── uuid7_fallback.py
├── .gitignore
├── requirements.txt
└── README.md
```

⚙️ Installation and Setup

1. Clone the Repository

```bash
git clone <your-repository-url>
```

2. Navigate to the Project Folder

```bash
cd AI-Placement-Preparation-Assistant
```

3. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

4. Install Dependencies

```bash
pip install -r requirements.txt
```

5. Configure Environment Variables

Create a `.env` file in the project folder and add:

```env
OPENROUTER_API_KEY=your_api_key
MODEL_NAME=openai/gpt-4o-mini
```

Replace `your_api_key` with your actual OpenRouter API key.

6. Run the Application

```bash
streamlit run app.py
```

🚀 How to Use
- Open the application in your browser.
- Select your preferences.
- Click **Generate Interview**.
- Explore the generated questions, answers, and explanations.
- Download the questions in JSON format.

🔮 Future Enhancements
- Voice-based mock interviews.
- AI-powered answer evaluation.
- Personalized feedback and performance analysis.
- Resume-based question generation.
- Coding practice and evaluation.

🎯 Project Objective
To help students improve their technical knowledge and confidence through AI-powered interview preparation.
