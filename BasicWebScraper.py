"""
A Python script to scrape the main content (title and initial paragraphs) 
from a Wikipedia page using the requests and Beautiful Soup libraries.
"""
import requests
from bs4 import BeautifulSoup

# The URL of the Wikipedia page for the Python programming language
WIKI_URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"

def scrape_wikipedia_article(url):
    """
    Fetches the HTML content of the given URL and extracts the main article title 
    and the first three paragraphs of the summary.
    """
    print(f"--- Fetching data from: {url} ---")
    
    try:
        # 1. Fetch the HTML content
        # We use a user-agent to make the request look like it's coming from a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return

    # 2. Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # --- Extraction Steps ---

    # 3. Use find() to get the main article title
    # Wikipedia uses the id 'firstHeading' for the main title
    title_tag = soup.find('h1', id='firstHeading')
    article_title = title_tag.get_text() if title_tag else "Title Not Found"

    # 4. Use find() to locate the main content body (container)
    # Most Wikipedia content is inside a div with the id 'mw-content-text'
    content_div = soup.find('div', id='mw-content-text')
    
    if content_div:
        # 5. Use find_all() on the content container to get all paragraphs
        # We search specifically within the main parser output div
        main_body = content_div.find('div', class_='mw-parser-output')
        
        if main_body:
            # Find all <p> (paragraph) tags within the main body
            # We use a limit to grab only the first few summary paragraphs
            paragraphs = main_body.find_all('p', limit=5) 
            
            summary = []
            for p in paragraphs:
                # Get the cleaned text of the paragraph and add it to the summary list
                paragraph_text = p.get_text().strip()
                # Exclude empty paragraphs (sometimes due to footnotes or side elements)
                if paragraph_text:
                    summary.append(paragraph_text)
            
            # 6. Output the extracted data
            print("-" * 40)
            print(f"Article Title: {article_title}")
            print("-" * 40)
            print("Summary Snippet:")
            print("\n".join(summary))
            print("-" * 40)
        else:
            print("Could not find the main parser output content.")
    else:
        print("Could not find the main content div.")

if __name__ == "__main__":
    # Ensure you have 'requests' and 'beautifulsoup4' installed:
    # pip install requests beautifulsoup4
    
    scrape_wikipedia_article(WIKI_URL)
