# Research Paper Analysis Tool

## Overview

This Python script automates the extraction and analysis of research papers. It processes PDF files, extracts text, analyzes the content using OpenAI's GPT-4 model, and saves the results to a DOCX file. The analysis focuses on extracting key details from research papers, including titles, journal details, publication year, tools, frameworks, algorithms, methodologies, inferences, and research gaps.

## Features

- **PDF Text Extraction**: Extracts text from PDF files using PyPDF2.
- **Text Analysis**: Utilizes OpenAI's GPT-4 model to analyze text and extract relevant details.
- **Document Creation**: Saves the analysis results to a DOCX file using the `python-docx` library.

## Prerequisites

- Python 3.7 or later
- Required Python packages:
  - `openai`
  - `PyPDF2`
  - `python-docx`

You can install the required packages using pip:

```bash
pip install openai PyPDF2 python-docx
