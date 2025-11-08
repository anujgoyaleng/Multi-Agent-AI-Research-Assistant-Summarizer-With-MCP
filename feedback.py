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

# Initialize LLM
gemini_llm = get_llm()

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

# Classification Chain
classify_chain = classify_prompt | gemini_llm | pydantic_parse

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

# Feedback Response Chain
feedback_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", positive_prompt | gemini_llm | str_parse),
    (lambda x: x.sentiment == "negative", negative_prompt | gemini_llm | str_parse),
    RunnableLambda(lambda x: "Thank you for your feedback! We appreciate your input.")
)

# Main Chain
main_chain = classify_chain | feedback_chain

def get_feedback(feedback: str) -> str:
    """
    Analyze feedback sentiment and generate appropriate response
    
    Args:
        feedback (str): User feedback text
        
    Returns:
        str: AI-generated response based on sentiment
    """
    try:
        result = main_chain.invoke({'feedback': feedback})
        return result
    except Exception as e:
        return f"Thank you for your feedback! We appreciate your input and will use it to improve."
