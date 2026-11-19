# Setup

## GCloud auth
# Deploy
```bash
gcloud config set project agentic-demos-463018
gcloud auth application-default login
```

## Setup uv

### To setup uv for first time
```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt 
```
## Next time
```bash
uv sync
```

# Running

```bash
cd /home/gspmoreira/projects/agentic_paper_review_adk_2
```

# Test locally
```bash
agents-cli playground
# or equivalently:
adk web agents/ --allow_origins="*"
```

# Deploys package (single_reviewer)
```bash
agents-cli deploy --no-confirm-project
# add --clear-env-vars or --config agents-cli-manifest.yaml if needed
```

# Runs remote inference
```bash
agents-cli run \
  --url "https://us-east1-aiplatform.googleapis.com/v1/projects/agentic-demos-463018/locations/us-east1/reasoningEngines/1487514987566989312" \
  --mode adk \
  --file paper/NV-Retriever.pdf \
  "Please review this paper for CIKM."
```

# Publishes to Gemini Enterprise app
```bash
agents-cli publish gemini --interactive
```