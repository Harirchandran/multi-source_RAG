# generation/llm.py

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


def get_llm():
    """
    Initialize LLM (Groq)
    """

    return ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="groq/compound-mini",
        temperature=0
    )


def generate_answer(llm, prompt, documents, query):
    """
    Generate answer using LLM

    Args:
        llm: language model
        prompt: prompt template
        documents: list of Document objects
        query: user query

    Returns:
        answer string
    """

    # Combine documents into context
    context = "\n\n".join([doc.page_content for doc in documents])

    # Format prompt
    formatted_prompt = prompt.format(
        context=context,
        input=query
    )

    # Generate response
    response = llm.invoke(formatted_prompt)

    return response.content