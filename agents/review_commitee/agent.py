import logging
import os

from dotenv import load_dotenv
from google.adk.agents import LlmAgent

from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent
from .output_models import FullReview, MetaReview

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)

load_dotenv()

MODEL = "gemini-2.5-flash"
OUTPUT_JSON = False


def create_reviewer_agent(persona_prompt, output_key):
    reviewer_prompt_template = f"""
        You are an expert academic reviewer of a top-tier AI conference.
        If the user mentions the conference name in his message, please review according to the emphasis of that conference.
        Be demanding and judicious in your review, as only the top 20% of papers are accepted at this conference on average. 

        {persona_prompt}

        Your task is to provide a detailed, critical, and constructive review of the following research paper.   
        Please read the paper provided and generate a complete review. 
        ---
    """

    return LlmAgent(
            name="ReviewerAgent",
            description="An academic reviewer for a conference",
            instruction=reviewer_prompt_template,
            model=MODEL,
            output_schema=FullReview if OUTPUT_JSON else None,
            output_key=output_key,
            tools=[],
        )


def create_conf_review_pipeline_agent() -> LlmAgent:
    """Constructs the ADK currency conversion agent."""
    logger.info("--- 🤖 Creating ADK Reviewer and Meta-Reviewer agents... ---")

    reviewer_personas = [
        {
            "persona": "Expert in Theory and Foundations",
            "prompt": "Your primary focus is on the THEORETICAL and a 'pure science' contribution of the paper. "
                    "Scrutinize the mathematical formulations, proofs, and underlying assumptions. "
                    "Is the core idea truly novel and elegant? Is the technical soundness of the theory impeccable?"
        },
        {
            "persona": "Expert in Empirical Methods and Reproducibility",
            "prompt": "Your primary focus is on the SCIENTIFIC METHOD and EXPERIMENTAL VALIDATION. "
                    "Assess the experimental design, the choice of baselines, ablation studies, and statistical significance. "
                    "Is the work easily reproducible? Are the claims well-supported by the evidence provided?"
        },
        {
            "persona": "Domain Expert in Related Work and Novelty",
            "prompt": "Your are an expert in the domain of this paper, your primary focus is on the paper's positioning within "
                    "the EXISTING LITERATURE. "
                    "Evaluate the adequacy of citations and the 'related work' section. How does this work "
                    "differentiate from prior art? Have they missed any crucial citations or misrepresented previous work?"
        },
        {
            "persona": "Expert in Presentation and Impact",
            "prompt": "Your primary focus is on the CLARITY OF WRITING and POTENTIAL IMPACT. "
                    "Assess the quality of the presentation, including figures, tables, and overall structure. "
                    "Is the paper easy to understand? How significant is the potential impact of these ideas on the field or in practice?"
        }
    ]


    # --- 1. Create reviewers with different personals / perspectives ---
    reviewers = dict()
    for idx, rp in enumerate(reviewer_personas):
        reviewer_id = f"reviewer_{idx}"
        reviewers[reviewer_id] = create_reviewer_agent(f'{rp["persona"]} - {rp["prompt"]}', reviewer_id)

    # --- 2. Create the ParallelAgent (Runs researchers concurrently) ---
    # This agent orchestrates the concurrent execution of the researchers.
    # It finishes once all researchers have completed and stored their results in state.
    parallel_research_agent = ParallelAgent(
        name="ParallelReviewsAgent",
        sub_agents=list(reviewers.values()),
        description="Runs multiple review agents in parallel.",        
    )


    # --- 3. Define the MetaReviewer agent (Runs *after* the parallel agents) ---
    instruction=f"""
            You are the Meta-Reviewer (or Area Chair) for a prestigious academic conference.
            If the user mentions the conference name in his message, please elaborate your meta-review according to the emphasis of that conference.
            You have received reviews for a paper. Your job is to synthesize these reviews into a meta-review that will be sent to the authors.
            Do not re-review the paper yourself. Your task is to consolidate the existing feedback.

            Your tasks are:
            1. Summarize the key points of agreement and disagreement among the reviewers.
            2. Identify the most critical strengths and weaknesses mentioned.
            3. Formulate a final recommendation (e.g., "Accept", "Reject", etc.).
            4. Write a clear, constructive message to the authors explaining the decision and guiding their next steps.

            Please transcribe all the original reviews in the end of your answer.
            """

    meta_reviewer_agent = LlmAgent(
        name="MetaReviewer",
        model=MODEL,
        instruction=instruction,
        description="Combines research findings from parallel agents into a structured, cited report, strictly grounded on provided inputs.",
        output_schema=MetaReview if OUTPUT_JSON else None,
        output_key="meta_review"
    )

    # --- 4. Create the SequentialAgent (Orchestrates the overall flow) ---
    # This is the main agent that will be run. It first executes the ParallelAgent
    # to populate the state, and then executes the MetaReviewer to produce the final output.
    sequential_pipeline_agent = SequentialAgent(
        name="ResearchAndSynthesisPipeline",
        sub_agents=[parallel_research_agent, meta_reviewer_agent],
        description="Coordinates parallel reviewers and synthesizes the meta-review."
    )

    return sequential_pipeline_agent

root_agent = create_conf_review_pipeline_agent()