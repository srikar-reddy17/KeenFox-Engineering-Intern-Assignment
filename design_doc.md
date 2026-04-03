
# Competitive Intelligence & Campaign Feedback System

## 1. System Architecture

The system is designed as a modular pipeline that separates data ingestion, analysis, and strategy generation.

### Architecture Overview

Scraper Layer → Data Aggregation → LLM Analysis Engine → Recommendation Engine → Output (JSON + Dashboard)

### Components

1. **Scraper Layer**
   - Collects data from:
     - Competitor websites
     - Reddit (community sentiment)
     - Capterra (user reviews)

2. **Data Aggregation Layer**
   - Combines multi-source data into a unified structure per competitor
   - Ensures consistent input format for the LLM

3. **LLM Analysis Engine**
   - Uses Gemini API to extract structured insights:
     - Features
     - Messaging
     - Customer sentiment
     - Pricing signals
     - Strategic positioning

4. **Recommendation Engine**
   - Generates actionable campaign strategies based on insights
   - Produces:
     - Messaging improvements
     - Channel strategy
     - GTM recommendations

5. **Output Layer**
   - JSON report (`report.json`)
   - Streamlit dashboard for visualization
   - Q&A interface for querying insights
---

## 2. Data Flow Diagram
[Websites] [Reddit] [Capterra]  
↓ ↓ ↓  
[Scraper Layer]  
↓  
[Aggregated Data]  
↓  
[LLM Analysis Engine]  
↓  
[Structured Insights JSON]  
↓  
[Recommendation Engine (LLM)]  
↓  
[Final Report + Dashboard]
---

## 3. Handling Noisy, Incomplete, or Conflicting Data

### Challenges
- Scraped web data is unstructured and noisy
- Reddit data may be informal or irrelevant
- Reviews may be biased or contradictory

### Approach

1. **Content Filtering**
   - Limit scraped content (top paragraphs, relevant sections)
   - Filter Reddit posts by competitor name

2. **Multi-Source Validation**
   - Combine signals from multiple sources (website + reviews + Reddit)
   - Reduces reliance on any single noisy source

3. **LLM-Based Normalization**
   - The LLM is used to:
     - Filter irrelevant information
     - Extract only meaningful signals
     - Resolve contradictions by summarizing patterns

4. **Structured Output Enforcement**
   - Prompts enforce strict JSON structure
   - Ensures consistent downstream processing
---

## 4. Prompt Strategy

The system uses carefully designed prompts to guide the LLM from raw data → strategic insights.

### Key Design Principles

1. **Structured Extraction**
   - Prompts explicitly define output schema (JSON)
   - Prevents vague or unstructured responses

2. **Reasoning over Summarization**
   - The model is instructed to:
     - Identify patterns
     - Infer positioning
     - Highlight gaps
   - Not just summarize text

3. **Multi-Signal Interpretation**
   - Prompts combine:
     - Website content
     - Reviews
     - Community sentiment
   - Enables richer insights

4. **Separation of Concerns**
   - Two-stage LLM pipeline:
     - Stage 1: Competitor analysis
     - Stage 2: Strategy generation

5. **Incremental Updates**
   - Recommendation prompts receive:
     - Previous insights
     - New insights
   - Enables updating strategies instead of recomputing blindly
---

## 5. Re-runnable Feedback Loop Design

The system supports incremental updates:

- Previous insights are stored (`report.json`)
- On re-run:
  - New data is compared with previous inputs
  - Only changed competitors are reprocessed
- Recommendations are updated using both:
  - Previous insights
  - New signals

This enables a feedback loop where strategies evolve over time as new data arrives.
---

## 6. Known Limitations

1. **Limited Data Sources**
   - No direct integration with G2 or LinkedIn APIs
   - Scraping may miss deeper insights

2. **No True Temporal Tracking**
   - Messaging “shifts” are inferred, not tracked over time

3. **Basic Scraping Logic**
   - HTML parsing is simple and may include noise

4. **LLM Dependency**
   - Output quality depends on prompt effectiveness
   - Occasional formatting inconsistencies

5. **Rate Limits**
   - API usage constrained by Gemini quotas
---

## 7. Future Improvements

With more time, the system could be significantly enhanced:

### Data Layer
- Integrate:
  - G2 / Capterra APIs
  - LinkedIn scraping or APIs
  - Product changelog feeds

### Intelligence Layer
- Use embeddings + vector database (FAISS/Pinecone)
- Semantic search over competitor data

### Temporal Analysis
- Track historical snapshots
- Detect real messaging and pricing changes over time

### Scalability
- Async pipelines
- Scheduled data ingestion (cron jobs)

### UI Improvements
- Interactive dashboards
- Trend visualizations
- Competitor comparison charts
---