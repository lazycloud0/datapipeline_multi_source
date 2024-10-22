# Datapipeline for multiple sources

# Project Overview

The goal of this project is to create a data pipeline that ingests data from various sources, processes it, and stores it in a structured format for analysis. We will focus on a basic pipeline that includes data ingestion, processing, and storage.

# Project Structure

data_pipeline_project/
├── data/ # Directory for raw and processed data
├── scripts/ # Directory for Python scripts
├── notebooks/ # Directory for Jupyter notebooks
└── README.md # Project documentation

# Data Ingestion

Ingest data from different sources.

    Zoom Lecture Transcripts: Say they are text files in the data/ directory.

    eBooks: Say they are PDF files in the data/ directory.

    Articles: Use a list of URLs to scrape article content.

    Quizzes: Say they are CSV files in the data/ directory.

    Git Repository: Clone a Git repository to access code files.

    Coding Workshops: Say they are links to workshop resources.

# Data Processing

A simple processing script to clean and structure the data.

# Data Storage

For simplicity, store the processed data in CSV files.

# Data Analysis

Now that you have stored the processed data, you can perform some basic analysis

## Running the Pipeline

To run the data pipeline, follow these steps:

### Ingest Data: Run the ingest_data.py script to read the data from the sources.

`python scripts/ingest_data.py`

### Process Data: Run the process_data.py script to process the ingested data.

`python scripts/process_data.py`

### Store Data: Run the store_data.py script to save the processed data to CSV files.

`python scripts/store_data.py`

### Analyze Data: Open the Jupyter notebook data_analysis.ipynb to explore and analyze the processed data.

## Requirements

- Python 3.x
- Required libraries: `pandas`, `requests`, `beautifulsoup4`, `PyPDF2`

## How to Run

1. Place your Zoom transcripts, eBooks (PDFs), and quizzes (CSV files) in the `data/` directory.
2. Update the `article_urls` list in `ingest_data.py` with the URLs of the articles you want to scrape.
3. Run the following scripts in order:
   - `ingest_data.py` to ingest data.
   - `process_data.py` to process the ingested data.
   - `store_data.py` to store the processed data.
4. Use the Jupyter notebook `data_analysis.ipynb` to analyze the processed data.

## Future Improvements

- Implement more advanced data processing and analysis techniques.
- Add error handling and logging for better robustness.
- Explore using a database for data storage instead of CSV files.
