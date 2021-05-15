"""Module with WikiADT class for extracting politician`s image and description."""
import wikipedia


class WikiADT():
    """A class for storing Wiki information about a politician."""

    def __init__(self, politician_name):
        """Initialize search and get all necessary information."""
        wikipedia.set_lang("uk")
        self.wiki_desc = info = wikipedia.summary(politician_name, sentences=4)

        # self.wiki_link = wiki_link = wikipedia.page(politician_name).url

        wiki_images = wikipedia.page(politician_name).images

        self.links = []
        for image in wiki_images:
            if not image.endswith(".svg") and not image.endswith(".png"):
                self.links.append(image)
