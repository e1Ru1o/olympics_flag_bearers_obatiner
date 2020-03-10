import requests, os
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs


def main(args):
    pages_dir = "pages/contries/"
    wiki = "https://en.wikipedia.org/"
    page = f"{wiki}wiki/Category:Nations_at_the_{args.year}_Summer_Olympics"
    suffix = f" at the {args.year} Summer Olympics"
    
    os.makedirs(pages_dir, exist_ok=True)

    def valid_tags(tag):
        return tag.name == 'a' and tag.has_attr('title') and tag['title'][-len(suffix):] == suffix

    req = requests.get(page)
    soup = bs(req.content, 'lxml')
    tags = soup.findAll(valid_tags)

    for tag in tags:
        link = tag['href']
        file_name = link.split('/')[-1]
        req = requests.get(urljoin(wiki, link))
        with open(f'{pages_dir}{file_name}.html', 'w') as fd:
            fd.write(req.text)


if __name__ == "__main__":
    import argparse 

    parser = argparse.ArgumentParser(description='Download Contries details related to an Olimpic Game year')
    parser.add_argument('-y', '--year', type=str, default='1936', help='Olympic Game year')

    args = parser.parse_args()
    main(args)
