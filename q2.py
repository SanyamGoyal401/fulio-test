import requests
from bs4 import BeautifulSoup
import re

def get_social_links_and_phone_number(url):
    social_links = []
    phone_number = None

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract social media links
        social_media_tags = soup.find_all('a', href=re.compile(r'(facebook|twitter|instagram|linkedin|youtube|github)'))
        social_links = [tag['href'] for tag in social_media_tags]

        # Extract phone number using regex
        phone_number_pattern = re.compile(r'^(\+?\d{0,2})?[-. ]?\(?(\d{1,4})\)?[-. ]?(\d{3})[-. ]?(\d{4})$')
        phone_number_tags = soup.find_all(string=phone_number_pattern)
        for tag in phone_number_tags:
            match = phone_number_pattern.search(tag)
            print(match)
            if match:
                phone_number = match.group()
                print(phone_number)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

    return social_links, phone_number



if __name__ == "__main__":
    website_url = input("Enter url: ")
    social_links, phone_number = get_social_links_and_phone_number(website_url)

    if len(social_links):
        print("Social Links-")
        for link in social_links:
            print(link)
    else:
        print("Social links not found")

    if phone_number:
        print("Phone Number:", phone_number)
    else:
        print("Phone Number not found.")
