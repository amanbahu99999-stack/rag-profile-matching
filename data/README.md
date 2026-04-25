# RAG Based Profile Matching System

## Overview
This project is an AI-powered resume screening system that matches resumes with job descriptions using Retrieval-Augmented Generation (RAG), embeddings, and vector search.

## Features
- Resume ingestion from local folder
- Resume embeddings using Sentence Transformers
- Vector storage using ChromaDB
- Semantic search for job descriptions
- Candidate ranking based on similarity

## Tech Stack
- Python
- ChromaDB
- Sentence Transformers
- VS Code

## Files
- resume_rag.py → indexes resumes
- job_matcher.py → matches candidates to job descriptions

## How to Run

### Install Dependencies
pip install chromadb sentence-transformers pymupdf python-docx pandas

### Index Resumes
python3 resume_rag.py

### Run Matcher
python3 job_matcher.py

## Sample Query
Need Python developer with SQL and AWS experience

## Future Improvements
- UI dashboard
- PDF resume support
- Experience filters
- LLM reasoning summaries