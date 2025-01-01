# autohint/suggestion.py

import threading
import urllib
from bs4 import BeautifulSoup
import time
from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
import requests
from functools import lru_cache

# Thread-safe global variable for storing suggestions
suggestions = []
lock = threading.Lock()

# Debounce mechanism
last_query_time = 0
debounce_interval = 0.3  # Seconds

# Cache to store recent queries and their results
@lru_cache(maxsize=100)
def fetch_suggestions_cached(query):
    """
    Fetch suggestions from the internet for a given query.
    This function is cached to prevent redundant API calls.
    """
    url = f"https://api.datamuse.com/sug?s={query}"  # Example API
    try:
        response = requests.get(url, timeout=2)
        response.raise_for_status()
        return [item['word'] for item in response.json()]
    except requests.RequestException:
        return []

def fetch_suggestions(query):
    """
    Fetch suggestions and update the global variable safely.
    Implements debouncing to reduce excessive API calls.
    """
    global suggestions, last_query_time
    current_time = time.time()
    if current_time - last_query_time < debounce_interval:
        return  # Skip fetching if debounce interval not elapsed
    last_query_time = current_time

    results = fetch_suggestions_cached(query)
    with lock:
        suggestions.clear()
        suggestions.extend(results)

class InternetSuggestionCompleter(Completer):
    def get_completions(self, document, complete_event):
        global suggestions
        word = document.text.strip()

        # Start a new thread to fetch suggestions if input changes
        if word:
            thread = threading.Thread(target=fetch_suggestions, args=(word,))
            thread.daemon = True  # Ensure thread stops with the main program
            thread.start()

        # Display available suggestions
        with lock:
            for suggestion in suggestions:
                if word.lower() in suggestion.lower():
                    yield Completion(suggestion, start_position=-len(word))
                    

def search_bar(prom):
	a= prompt(prom, completer=InternetSuggestionCompleter())
	return a
	
	
	
def content(query):
	try:
         query = urllib.parse.quote(query)
         url = f'https://en.wikipedia.org/wiki/{query}'
         response = requests.get(url)
         if response.status_code == 200:
         	soup = BeautifulSoup(response.text, 'html.parser')
         	content = soup.find_all('p')  
         	article_content = [item.get_text(strip=True) for item in content]
         	return "\n".join(article_content)
         else:
             return f"Failed to retrive"
             
            
             
             
	except Exception as e:
		 return f"An error occurred: {str(e)}"

def qta(query):
    # The URL of the page you want to extract information from
    url = f'https://www.google.com/search?q={query}'

    # Custom headers with User-Agent to mimic a real browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    
    # Send a GET request with the custom headers
    response = requests.get(url, headers=headers)

    # Parse the response content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the answer or the correct information on the page
    try:
        answer = soup.find('div', {'class': 'BNeawe iBp4i AP7Wnd'}).get_text()
        return answer
    except AttributeError:
        return "Answer not found"





    
    
    
