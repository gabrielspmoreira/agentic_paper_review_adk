from typing import List, Literal
from pydantic import BaseModel, Field
from enum import Enum

from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent

class RecommendationEnum(str, Enum):
    strong_reject = "strong reject"
    weak_reject = "weak reject"
    borderline = "borderline"
    weak_accept = "weak accept"
    strong_accept = "strong accept"

class ReviewScores(BaseModel):
    """Defines the 1-5 scoring criteria for a paper review."""
    relevancy: int = Field(description="1-5 score for Relevance of the Work for a given conference.", ge=1, le=5)
    originality: int = Field(description="1-5 score for Originality of Work.", ge=1, le=5)
    technical_soundness: int = Field(description="1-5 score for Technical Soundness.", ge=1, le=5)
    presentation_quality: int = Field(description="1-5 score for Quality of Presentation.", ge=1, le=5)
    impact: int = Field(description="1-5 score for Impact of Ideas or Results.", ge=1, le=5)
    citations_adequacy: int = Field(description="1-5 score for Adequacy of Citations.", ge=1, le=5)
    reproducibility: int = Field(description="1-5 score for Reproducibility of Methods.", ge=1, le=5)
    recommendation: RecommendationEnum = Field(description="Recommendation according to `RecommendationEnum` enum.")

class DescriptiveReview(BaseModel):
    """Defines the descriptive part of a review."""
    summary: str = Field(description="A brief summary of the paper's main contributions.")
    target_conference: str = Field(description="The target conference chosen by the user.")
    suggested_conferences: str = Field(description="Suggestion of conferences where this paper could be relevant.")
    strenghts: List[str] = Field(description="A list of strengths or positive aspects of the paper.")
    weaknesses: List[str] = Field(description="A list of weaknesses or negative aspects of the paper.")
    detailed_comments: List[str] = Field(description="A list of detailed comments about the paper.")
    suggestions: List[str] = Field(description="Actionable suggestions for the authors to improve the paper.")
    typos_grammar_errors: List[str] = Field(description="List of typos or grammar errors found.")

class FullReview(BaseModel):
    """The complete output from a single reviewer agent."""
    reviewer_persona: str = Field(description="The persona or main focus of this reviewer.")
    scores: ReviewScores
    review: DescriptiveReview