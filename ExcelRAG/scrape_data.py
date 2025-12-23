import requests
from bs4 import BeautifulSoup
import json
import time
from urllib.parse import urljoin

def get_soup(url):
    try:
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
    content = []
    # Find h2 or h3 headers containing target text
    header = soup.find(lambda tag: tag.name in ['h2', 'h3'] and header_text.lower() in tag.get_text().lower())
    
    if header:
        for sibling in header.next_siblings:
            if sibling.name in ['h2', 'h3']:
                break
            if sibling.name: # Ignore NavigableStrings
                # Table Handling
                if sibling.name == 'table':
                    # Parse table
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
                    examples.append(text)
                    
    return examples

def scrape_statistical_functions():
    base_url = "https://support.microsoft.com/en-us/office/statistical-functions-reference-624dac86-a375-4435-bc25-76d659719ffd"
    print(f"Fetching main list from: {base_url}")
    
    soup = get_soup(base_url)
    if not soup:
        return

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
    
    # Iterate over table rows
    rows = target_table.find_all('tr')
    
    # Detect if first row is header
    start_index = 1 if "Function" in rows[0].get_text() else 0
     
    for row in rows[start_index:]:
        cols = row.find_all('td')
        if len(cols) < 2:
            continue
            
        link_tag = cols[0].find('a')
        if not link_tag:
            continue
            
        func_name = link_tag.get_text(strip=True)
        func_url = urljoin(base_url, link_tag['href']) # type: ignore
        short_summary = cols[1].get_text(strip=True)
        
        print(f"Scraping {func_name}...")
        
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
        
        time.sleep(0.5)

    output_filename = 'statistical_functions.json'
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(functions_data, f, indent=4, ensure_ascii=False)
    
    print(f"Scraping complete. Data saved to {output_filename}")

if __name__ == "__main__":
    scrape_statistical_functions()