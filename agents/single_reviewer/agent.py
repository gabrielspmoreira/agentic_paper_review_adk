import logging
import os

from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from .output_models import FullReview

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)

load_dotenv()

MODEL = "gemini-2.5-flash"
OUTPUT_JSON = False

def create_reviewer_agent() -> LlmAgent:
    """Constructs the reviewer agent."""
    logger.info("--- 🤖 Creating ADK Reviewer agent... ---")


    reviewer_prompt_template = f"""
        You are an expert academic reviewer of a top-tier academic conference.
        If user mentions the conference name in the message, please review according to the emphasis of that conference.
        Your task is to provide a detailed, critical, and constructive review of the following research paper.   
        Please read the paper provided and generate a complete review. 
    """
    
    reviewer_agent = LlmAgent(
        model=MODEL,
        name="academic_reviewer",
        description="An academic reviewer for a conference",
        instruction=reviewer_prompt_template,
        output_schema=FullReview if OUTPUT_JSON else None,
        output_key="review",
        tools=[],
    )    

    return reviewer_agent

root_agent = create_reviewer_agent()