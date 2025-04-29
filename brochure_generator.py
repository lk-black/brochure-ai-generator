import os
import json
from utils import Website
import openai
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

MODEL = 'gpt-4o-mini'

class BroucheGenerator():
    """Class to generate custom brouches for a website"""
    url: str
    
    def __init__(self, url):
        self.url = url
        self.website = Website(url)
    
    link_system_prompt = """" You are provide with a list of links found on a webpage.
        You are able to decide wich of the links would be most relevant to include in a brochure about company.
        such as links to an About page, a Company page, or Carrers/Jobs page.\n
        You should respond in JSON as in this example:\n
        {
            "links": [
                {type: "about page": "url": "https://example.com/about"},
                {type: "careers page", "url": "https://example.com/careers"}
        ]
    }"""

    system_prompt = """You are an assistant that analyzes the contents of several relevant pages from a company website
        and creates a short brochure about the company for prospective customers, investors and recruits. Respond in markdown.
        Include details of company culture, customers and careers/jobs if you have the information."""

    def get_links_user_prompt(self):
        user_prompt = f"""Here is the list of links on the website {self.website.url}\n
        please decide which of the links would be most relevant to include in a brochure about company.
        respond with the full https:// url of the link.
        do not include terms of Service, Privacy Policy, or any other irrelevant links.\n\n
        """
        user_prompt += "\n".join(self.website.links)
        return user_prompt

    def get_links(self):
        completion = openai.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": self.link_system_prompt},
                {"role": "user", "content": self.get_links_user_prompt()}
            ],
            response_format={"type": "json_object"}
    )
        result = completion.choices[0].message.content
        return json.loads(result)

    def get_all_details(self):
        result = "Landing page:\n"
        result += Website(self.url).get_contents()
        links = self.get_links()
        print("Found links:", links)
    
        for link in links['links']:
            result += f"\n\n{link['type']}\n"
            result += Website(link['url']).get_contents()
        return result

    def get_brochure_user_prompt(self, company_name):
        user_prompt = f"You are looking at a company called: {company_name}\n"
        user_prompt += f"Here are the contents of its landing page and other relevant pages; use this information to build a short brochure of the company in markdown.\n"
        user_prompt += self.get_all_details()
        user_prompt = user_prompt[:5_000] 
        return user_prompt

    def create_brochure(self, company_name):
        response = openai.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": self.get_brochure_user_prompt(company_name)}
            ],
        )
        result = response.choices[0].message.content
        with open('brochure.md', 'w') as f:
            f.write(result)
    
    def display_brochure(self):
        console = Console()
        with open('brochure.md', 'r') as f:
            md = Markdown(f.read())
            console.print(md)
