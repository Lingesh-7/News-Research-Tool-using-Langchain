# 📰 AI-Powered News Research Tool  

## Overview  
This project utilizes **LangChain and Large Language Models (LLMs)** to analyze and summarize **news articles from URLs**. It provides efficient **retrieval-augmented generation (RAG)** and **question-answering (QA) capabilities**, helping users extract meaningful insights from articles.  

## Features  
- **Automated article analysis** using NLP techniques.  
- **RetrievalQA and SourceChain implementation** for accurate summaries.  
- **Hosted on Streamlit** for real-time access.  
- **User-friendly interface** for seamless news exploration.  

## Technologies Used  
- **LangChain & LLMs** – Text processing & analysis.  
- **Python & Pandas** – Data handling.  
- **Streamlit** – Interactive web deployment.  

## Installation  
```bash
git clone https://github.com/Lingesh-7/News-Research-Tool
cd News-Research-Tool
pip install -r requirements.txt
```

## Usage  
### 1. Running the News Analysis  
```bash
python analyze.py --url "https://example.com/news_article"
```

### 2. Web-Based News Retrieval (Streamlit App)  
```bash
streamlit run app.py
```

## Results  
The tool extracts **key insights** from news articles and generates **summaries & answers** to user queries in real time.  

## Future Improvements  
- Enhance **fact-checking capabilities** for credibility analysis.  
- Expand dataset for **better contextual understanding**.  
- Integrate **multi-source comparison** for diverse viewpoints.
