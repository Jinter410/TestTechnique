from api.selenium_api import SeleniumAPI

def main():
    api = SeleniumAPI(headless=False)
    instructions = api.read_instructions("instructions.json")
    api.execute_instructions(instructions)
    api.close()

if __name__ == "__main__":
    main()
