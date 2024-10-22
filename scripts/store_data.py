import pandas as pd

def store_data(processed_data):
    """
    Store processed data into CSV files.

    Parameters:
    processed_data (dict): Dictionary containing processed data with keys 'processed_quizzes' and 'processed_transcripts'.
    """
    try:
        # Store processed quizzes in a CSV file
        processed_quizzes = processed_data['processed_quizzes']
        processed_quizzes.to_csv('data/processed_quizzes.csv', index=False)
        print("Quizzes have been saved to 'data/processed_quizzes.csv'")
    except KeyError:
        print("Error: 'processed_quizzes' key not found in processed_data.")
    except Exception as e:
        print(f"An error occurred while saving quizzes: {e}")

    try:
        # Process transcripts and save them
        processed_transcripts = processed_data['processed_transcripts']
        df = pd.DataFrame({'transcripts': processed_transcripts})
        
        # Save the processed transcripts to a CSV file
        df.to_csv('data/processed_transcripts.csv', index=False)
        print("Transcripts have been saved to 'data/processed_transcripts.csv'")
    except KeyError:
        print("Error: 'processed_transcripts' key not found in processed_data.")
    except Exception as e:
        print(f"An error occurred while saving transcripts: {e}")

    # Additional storage steps for other data types (e.g., ebooks, articles) can be added here

if __name__ == "__main__":
    try:
        from process_data import process_data
        from ingest_data import ingest_data

        # Ingest raw data
        data = ingest_data()
        
        # Process the ingested data
        processed_data = process_data(data)
        
        # Store the processed data
        store_data(processed_data)
    except ImportError as e:
        print(f"Error importing modules: {e}")
    except Exception as e:
        print(f"An error occurred in the main execution: {e}")