import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def get_image_urls(url):
    image_urls = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for img in soup.find_all('img'):
            img_url = img.get('src')
            if img_url:
                img_url = urljoin(url, img_url)
                image_urls.append(img_url)
    return image_urls

def main():
    website_url = input("Enter the website URL: ")
    image_urls = get_image_urls(website_url)
    print("Image URLs found on the website:")
    for img_url in image_urls:
        print(img_url)

if __name__ == "__main__":
    main()
