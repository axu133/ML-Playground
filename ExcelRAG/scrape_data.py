import requests
from bs4 import BeautifulSoup
import json
import time
from urllib.parse import urljoin

def get_soup(url):
    """Fetches a URL and returns a BeautifulSoup object."""
    try:
        # User-agent header is often needed to avoid being blocked
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_section_content(soup, header_text):
    """
    Finds a header containing specific text and extracts the content 
    that follows it until the next header.
    """
    content = []
    # Find h2 or h3 headers containing the target text
    header = soup.find(lambda tag: tag.name in ['h2', 'h3'] and header_text.lower() in tag.get_text().lower())
    
    if header:
        for sibling in header.next_siblings:
            # Stop if we hit another header
            if sibling.name in ['h2', 'h3']:
                break
            if sibling.name: # Ignore NavigableStrings like newlines usually
                # specialized handling for tables in examples
                if sibling.name == 'table':
                    # Parse table into a list of lists or string representation
                    rows = []
                    for tr in sibling.find_all('tr'):
                        cells = [td.get_text(strip=True) for td in tr.find_all(['td', 'th'])]
                        rows.append(" | ".join(cells))
                    content.append("\n".join(rows))
                else:
                    text = sibling.get_text(strip=True)
                    if text:
                        content.append(text)
    
    return "\n\n".join(content)

def extract_examples(soup):
    """
    Specifically extracts content from the 'Example' section.
    Returns a list of strings/tables found in that section.
    """
    examples = []
    header = soup.find(lambda tag: tag.name in ['h2', 'h3'] and 'example' in tag.get_text().lower())
    
    if header:
        current_example_block = []
        for sibling in header.next_siblings:
            if sibling.name in ['h2', 'h3']:
                break
            
            if sibling.name == 'table':
                # Convert table to a formatted string
                table_rows = []
                for tr in sibling.find_all('tr'):
                    cells = [td.get_text(strip=True) for td in tr.find_all(['td', 'th'])]
                    table_rows.append(" | ".join(cells))
                examples.append("Table:\n" + "\n".join(table_rows))
            elif sibling.name:
                text = sibling.get_text(strip=True)
                if text:
                    # Append text to the list
                    examples.append(text)
                    
    return examples

def scrape_statistical_functions():
    base_url = "https://support.microsoft.com/en-us/office/statistical-functions-reference-624dac86-a375-4435-bc25-76d659719ffd"
    print(f"Fetching main list from: {base_url}")
    
    soup = get_soup(base_url)
    if not soup:
        return

    # Find the main table containing the functions. 
    # Usually it's the first large table in the article content.
    # We look for the table that contains "Function" and "Description" in headers/first row.
    tables = soup.find_all('table')
    target_table = None
    
    for table in tables:
        if "Description" in table.get_text():
            target_table = table
            break
    
    if not target_table:
        print("Could not find the functions table on the main page.")
        return

    functions_data = []
    
    # Iterate over table rows (skip header if present)
    rows = target_table.find_all('tr')
    
    # Detect if first row is header
    start_index = 1 if "Function" in rows[0].get_text() else 0
    
    # For testing purposes, you might want to slice rows[:5] to test quickly
    # for row in rows[start_index:5]: 
    for row in rows[start_index:]:
        cols = row.find_all('td')
        if len(cols) < 2:
            continue
            
        link_tag = cols[0].find('a')
        if not link_tag:
            # sometimes the function name is just text or in a different structure
            continue
            
        func_name = link_tag.get_text(strip=True)
        # Handle relative URLs
        func_url = urljoin(base_url, link_tag['href'])
        short_summary = cols[1].get_text(strip=True)
        
        print(f"Scraping {func_name}...")
        
        # Scrape the individual function page
        func_soup = get_soup(func_url)
        
        if func_soup:
            documentation = extract_section_content(func_soup, "Description")
            syntax_guide = extract_section_content(func_soup, "Syntax")
            usage_examples = extract_examples(func_soup)
            
            entry = {
                "function": func_name,
                "url": func_url,
                "short_summary": short_summary,
                "documentation": documentation,
                "syntax_guide": syntax_guide,
                "usage_examples": usage_examples
            }
            
            functions_data.append(entry)
        else:
            print(f"Failed to scrape details for {func_name}")
            # Add partial data if page load fails
            functions_data.append({
                "function": func_name,
                "url": func_url,
                "short_summary": short_summary,
                "documentation": "Error fetching page",
                "syntax_guide": "",
                "usage_examples": []
            })
        
        # Sleep to be polite to the server
        time.sleep(0.5)

    # Save to JSON
    output_filename = 'statistical_functions.json'
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(functions_data, f, indent=4, ensure_ascii=False)
    
    print(f"Scraping complete. Data saved to {output_filename}")

if __name__ == "__main__":
    scrape_statistical_functions()