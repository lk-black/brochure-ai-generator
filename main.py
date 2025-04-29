from brochure_generator import BroucheGenerator

url = input("Send url page (https://example.com): ")
emprise_name = input("Send a company name: ")

if __name__ == "__main__":
    bg = BroucheGenerator(url)
    bg.create_brochure(emprise_name)
    bg.display_brochure()