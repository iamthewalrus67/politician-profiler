"""Module with WikiADT class for extracting politician`s image and description."""
import wikipedia
from bs4 import BeautifulSoup
import requests


class WikiADT():
    """A class for storing Wiki information about a politician."""
    def __init__(self, politician_name):
        """Initialize search and get all necessary information."""
        wikipedia.set_lang("uk")
        self.wiki_desc = wikipedia.summary(politician_name, sentences=4)

        # self.wiki_link = wiki_link = wikipedia.page(politician_name).url

        # wiki_images = wikipedia.page(politician_name).images

        # self.links = []
        # for image in wiki_images:
        #     if not image.endswith(".svg") and not image.endswith(".png"):
        #         self.links.append(image)
        
        html_data = wikipedia.page(politician_name).html()
        soup = BeautifulSoup(html_data, "html.parser")
        image_links = soup.find_all("img")
        # for link in image_links["src"]:
        #     if "Ambox-scales" not in link and "Edit-clear" not in link:
        #         self.links = link
        #         break
        for item in soup.find_all("img"):
            link = item["src"]
            if "Ambox_scales" not in link and "Edit-clear" not in link:
                self.links = link
                break
        #print(self.links)
#a=WikiADT("Володимир Гройсман")