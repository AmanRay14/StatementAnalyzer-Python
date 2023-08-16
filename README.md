# StatementAnalyzer-Python

This project is a simple text processor that analyzes the sentiment of a given text using the TextBlob library in Python. It determines whether the sentiment of the text is positive, negative, or neutral.

## How it Works

The program takes an input text from the user and uses the TextBlob library to perform sentiment analysis on the text. It calculates the polarity of the text, which represents the sentiment's positivity or negativity. If the polarity is greater than 0, the sentiment is considered positive; if less than 0, the sentiment is negative; and if 0, the sentiment is neutral.

## Prerequisites

- Python 3.{version}
- TextBlob library (`pip install textblob`)

## Usage

1. Install the required library using the following command:
pip install textblob




2. Clone this repository to your local machine.

3. Navigate to the project directory:
cd text-processor-sentiment-analysis



4. Run the script:
python sentiment_analysis.py


5. Enter the text when prompted and the program will display the sentiment analysis result.

## Example

Input:
Enter a text: I love spending time in nature. The fresh air is so refreshing.




Output:
Sentiment: Positive 
