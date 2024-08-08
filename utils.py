from nltk.sentiment import SentimentIntensityAnalyzer
import logging


def read_file_content(filename):
    """
    Reads the content of a file and returns it as a string.

    Args:
        filename (str): The path to the file.

    Returns:
        str: The content of the file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except Exception as e:
        logging.error(f"Error reading {filename}: {e}")
        raise


def get_sentiment(contents):
    """
    Analyzes the sentiment of the given text content.

    Args:
        contents (str): The text content to analyze.

    Returns:
        dict: A dictionary containing the sentiment scores.
    """
    try:
        analyzer = SentimentIntensityAnalyzer()
        scores = analyzer.polarity_scores(contents)
        logging.info(f"Sentiment scores: {scores}")
        return scores
    except Exception as e:
        logging.error(f"Error analyzing sentiment: {e}")
        raise
