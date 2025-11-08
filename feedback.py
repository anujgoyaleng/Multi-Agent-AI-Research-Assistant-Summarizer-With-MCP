"""
Feedback Analysis Module
Analyzes user feedback sentiment and generates appropriate responses
"""
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal
from llm import get_llm

# LLM will be initialized lazily when needed
_gemini_llm = None

def get_gemini_llm():
    """Lazy initialization of Gemini LLM"""
    global _gemini_llm
    if _gemini_llm is None:
        _gemini_llm = get_llm()
    return _gemini_llm

# Feedback Schema
class FeedbackSentiment(BaseModel):
    """Schema for feedback sentiment classification"""
    sentiment: Literal['positive', 'negative'] = Field(
        description="Sentiment classification of the feedback"
    )

# Parsers
pydantic_parse = PydanticOutputParser(pydantic_object=FeedbackSentiment)
str_parse = StrOutputParser()

# Sentiment Classification Prompt
classify_prompt = PromptTemplate(
    template="""Classify the sentiment of the following feedback as either 'positive' or 'negative'.
    
    Feedback: {feedback}
    
    {format_instruction}""",
    input_variables=['feedback'],
    partial_variables={"format_instruction": pydantic_parse.get_format_instructions()}
)

# Response Prompts
positive_prompt = PromptTemplate(
    input_variables=['feedback'],
    template="""You are a friendly, enthusiastic assistant. 
    Write a warm, appreciative thank-you reply to this positive feedback:

    "{feedback}"
    
    Keep it concise (1-2 sentences), genuine, and encouraging."""
)

negative_prompt = PromptTemplate(
    input_variables=['feedback'],
    template="""You are a professional, empathetic assistant. 
    Write a polite, supportive, and constructive reply to this negative feedback:

    "{feedback}"
    
    Keep it concise (1-2 sentences), acknowledge their concerns, and show commitment to improvement."""
)

def get_feedback(feedback: str) -> str:
    """
    Analyze feedback sentiment and generate appropriate response
    
    Args:
        feedback (str): User feedback text
        
    Returns:
        str: AI-generated response based on sentiment
    """
    try:
        # Get LLM instance lazily
        llm = get_gemini_llm()
        
        # Build chains dynamically
        classify_chain = classify_prompt | llm | pydantic_parse
        
        feedback_chain = RunnableBranch(
            (lambda x: x.sentiment == "positive", positive_prompt | llm | str_parse),
            (lambda x: x.sentiment == "negative", negative_prompt | llm | str_parse),
            RunnableLambda(lambda x: "Thank you for your feedback! We appreciate your input.")
        )
        
        main_chain = classify_chain | feedback_chain
        result = main_chain.invoke({'feedback': feedback})
        return result
    except Exception as e:
        return f"Thank you for your feedback! We appreciate your input and will use it to improve."
