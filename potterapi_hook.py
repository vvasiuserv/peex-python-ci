import requests
import json
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


class PotterApiHook:

    def __init__(
        self,
        base_url: str = "https://potterapi-fedeperin.vercel.app",
        default_lang: str = "en",
    ):

        self.base_url = base_url
        self.default_lang = default_lang

    def set_lang(self, lang):
        self.default_lang = lang

    def get_books(self):

        url = f"{self.base_url}/{self.default_lang}/books"

        response = requests.get(url=url)

        response_json = json.loads(response.content)

        return response_json
