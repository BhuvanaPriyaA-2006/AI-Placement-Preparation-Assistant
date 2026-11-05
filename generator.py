
import os

from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter

from prompts import interview_prompt, parser
from schemas import InterviewResponse

load_dotenv()


# ==================================================
# GET LANGUAGE MODEL
# ==================================================

def get_llm():

    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        raise ValueError("OpenRouter API key not found.")

    model_name = os.getenv(
        "MODEL_NAME",
        "openai/gpt-4o-mini"
    )

    llm = ChatOpenRouter(
        model=model_name,
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
        temperature=0.3
    )

    return llm


# ==================================================
# GENERATE INTERVIEW QUESTIONS
# ==================================================

def generate_interview(
    job_role,
    experience_level,
    difficulty,
    num_questions
):

    llm = get_llm()

    chain = interview_prompt | llm | parser

    # Generate the initial questions
    response = chain.invoke({

        "job_role": job_role,
        "experience_level": experience_level,
        "difficulty": difficulty,
        "num_questions": num_questions,
        "existing_questions": "None"

    })

    # Store the generated questions
    questions = response.questions[:num_questions]

    # Generate only the missing questions
    while len(questions) < num_questions:

        missing_questions = num_questions - len(questions)

        # Pass previously generated questions
        existing_questions = "\n".join(
            question.question for question in questions
        )

        additional_response = chain.invoke({

            "job_role": job_role,
            "experience_level": experience_level,
            "difficulty": difficulty,
            "num_questions": missing_questions,
            "existing_questions": existing_questions

        })

        new_questions = additional_response.questions

        # Stop if AI does not return any questions
        if not new_questions:
            raise ValueError(
                "AI could not generate the remaining questions. "
                "Please try again."
            )

        # Add only the required number of questions
        questions.extend(
            new_questions[:missing_questions]
        )

    # Create the final interview response
    final_response = InterviewResponse(
        job_role=job_role,
        experience_level=experience_level,
        questions=questions[:num_questions]
    )

    return final_response
