# Agentic Paper Reviewer system with ADK

This repo demonstrates how to use ADK for creating a simple agentic system that emulates a review (Program Chair) commitee for an academic conference. The code demonstrates ADK workflow agents - `SequentialAgent` and `ParallelAgent` - which are useful to create deterministic pipelines. The agents are powered by Google Gemini API.

This is the workflow:

1. A PDF file with a text message stating the desired conference to submit.
2. Each reviewer agent, configured to have a different profile/emphasis, perform an independent review of the paper in parallel.
3. The meta-reviewer agent reads all the reviews, summarizes the major strengths / weaknesses of the paper and provides the final decision on acceptance/rejection.

## Installing
```bash
python3 -m venv .venv/agentic_paper_review
source .venv/agentic_paper_review/bin/activate
pip install -r requirements.txt
```

## Starting ADK Web UI
1. Start the ADK Web UI with the following command. The URL of ADK Web UI will be printed by the command.  

```bash
adk web agents/
```


P.s. If you are using Google Cloud Shell, click in the *Web Preview* button at top right of Cloud Shell and click in *Change Port* if needed (e.g. 8000) and then click in *Preview on port 8000*.  
2. When the browser loads, the ADK Web UI webapp will be presented.  
3. Select in the top-left of the webapp one of the available agents: `single_reviewer`, `review_commitee`.  
4. On the right panel, type *I would like to submit this paper to KDD*, click in the attachment button to attach a paper PDF and press enter to 4. submit. After some seconds/minutes, the reviews and meta-review will be available in the `State` tab, and eventually will also be presented in the conversation interface on the right panel.  
5. If you want reviews and meta-review to be in a standard schema format, set `OUTPUT_JSON=True`, and it will set the `output_schema` argument from `LlmAgent` constructor.         