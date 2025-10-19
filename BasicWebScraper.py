import requests
from bs4 import BeautifulSoup

def scrape_wikipedia_page(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Main content div
    content_div = soup.find("div", {"class": "mw-parser-output"})
    if not content_div:
        print("Could not find the main content on the page.")
        return

    # Collect text from paragraphs, headings, list items, and table cells
    texts = []

    # Elements to include (tags commonly used for content)
    tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'td']

    for tag in tags:
        for element in content_div.find_all(tag):
            # Get text and strip excessive whitespace
            text = element.get_text(strip=True)
            if text:
                texts.append(text)

    # Join all extracted text with double newlines for readability
    full_text = "\n\n".join(texts)

    # Save to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(full_text)

    print(f"Page content scraped and saved to '{output_file}'")

# Example usage
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
output_file = "wikipedia_full_page.txt"
scrape_wikipedia_page(url, output_file)
