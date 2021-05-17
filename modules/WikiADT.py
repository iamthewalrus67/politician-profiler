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

        html_data = wikipedia.page(politician_name).html()
        soup = BeautifulSoup(html_data, "html.parser")
        image_links = soup.find_all("img")

        for item in soup.find_all("img"):
            link = item["src"]
            if "Ambox_scales" not in link and "Edit-clear" not in link:
                self.links = link
                break
