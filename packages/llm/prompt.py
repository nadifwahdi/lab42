from llm.types import Prompt

"""
Create a Prompt instance by providing a main prompt message, and optionally, specific instructions
to guide the model's response.

Recommendation:
    To create a powerful prompt, be clear and specific about what you want. Use context or examples
    when needed, and provide instructions that set expectations for tone, length, or audience.

Example:
>>>>    prompt = Prompt(
>>>>        prompt="Explain the theory of relativity",
>>>>        instructions="Use simple language suitable for high school students."
>>>>    )

"""


class ExamplePrompt:
    grammar_checker_prompt = Prompt(
        instructions="""
        You are a grammar checker. Fix errors related to verb tense, article usage, and pluralization.
        Also explain each correction in simple terms.
        """,
        prompt="""
        The people is goes to market to buys vegetable.
        """,
    )


def ielts_tutor_prompt(student_answer: str) -> Prompt:
    return Prompt(
        instructions="""
        You are an experienced IELTS tutor who specializes in grammar and sentence structure.
        Your task is to evaluate student answers for grammatical accuracy, sentence structure, punctuation, and clarity.
        For each sentence, identify and explain any grammar or structural issues and suggest a corrected version.
        Then, provide brief overall feedback and a personalized recommendation for improving their grammar skills.
        Be constructive, clear, and encouraging in your response.
        """,
        prompt=f"""
        Student's answer: {student_answer}
        """,
    )
