import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader

# Function to read Zoom transcripts
def read_transcripts(directory):
    """
    Read all transcript files from the specified directory.

    Parameters:
    directory (str): Path to the directory containing transcript files.

    Returns:
    list: List of transcript contents.
    """
    transcripts = []
    try:
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                try:
                    with open(os.path.join(directory, filename), 'r') as file:
                        transcripts.append(file.read())
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")
    except Exception as e:
        print(f"Error accessing directory {directory}: {e}")
    return transcripts

# Function to read eBooks (PDFs)
def read_ebooks(directory):
    """
    Read all eBook files from the specified directory.

    Parameters:
    directory (str): Path to the directory containing eBook files.

    Returns:
    list: List of eBook contents.
    """
    ebooks = []
    try:
        for filename in os.listdir(directory):
            if filename.endswith('.pdf'):
                try:
                    with open(os.path.join(directory, filename), 'rb') as file:
                        reader = PdfReader(file)
                        text = ''
                        for page in reader.pages:
                            text += page.extract_text()
                        ebooks.append(text)
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")
    except Exception as e:
        print(f"Error accessing directory {directory}: {e}")
    return ebooks

# Function to scrape articles
def scrape_articles(urls):
    """
    Scrape articles from the provided URLs.

    Parameters:
    urls (list): List of URLs to scrape articles from.

    Returns:
    list: List of article contents.
    """
    articles = []
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            soup = BeautifulSoup(response.text, 'html.parser')
            articles.append(soup.get_text())
        except requests.RequestException as e:
            print(f"Error scraping URL {url}: {e}")
    return articles

# Function to read quizzes
def read_quizzes(directory):
    """
    Read all quiz files from the specified directory.

    Parameters:
    directory (str): Path to the directory containing quiz files.

    Returns:
    list: List of DataFrames containing quiz data.
    """
    quizzes = []
    try:
        for filename in os.listdir(directory):
            if filename.endswith('.csv'):
                try:
                    quizzes.append(pd.read_csv(os.path.join(directory, filename)))
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")
    except Exception as e:
        print(f"Error accessing directory {directory}: {e}")
    return quizzes

# Main function to ingest data
def ingest_data():
    """
    Ingest data from various sources.

    Returns:
    dict: Dictionary containing ingested data.
    """
    try:
        transcripts = read_transcripts('data/')
        ebooks = read_ebooks('data/')
        article_urls = ['https://example.com/article1', 'https://example.com/article2']  # Replace with actual URLs
        articles = scrape_articles(article_urls)
        quizzes = read_quizzes('data/')
        
        return {
            'transcripts': transcripts,
            'ebooks': ebooks,
            'articles': articles,
            'quizzes': quizzes
        }
    except Exception as e:
        print(f"An error occurred during data ingestion: {e}")
        return {}

if __name__ == "__main__":
    try:
        data = ingest_data()
        print("Data ingestion completed successfully.")
    except Exception as e:
        print(f"An error occurred in the main execution: {e}")