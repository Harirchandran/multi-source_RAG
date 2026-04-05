# generation/prompt.py

from langchain_core.prompts import ChatPromptTemplate


def get_prompt():
    """
    Returns a strict QA prompt template
    """

    prompt = ChatPromptTemplate.from_template(
        """
You are a strict question-answering system.

Rules:
1. Answer ONLY from the provided context
2. If answer is not in context, say "I don't know"
3. Do NOT guess or add extra information

<context>
{context}
</context>

Question: {input}

Answer:
"""
    )

    return prompt