import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simplex.simplex import Simplex
from simplex.utils import screenshot_to_image
from playwright.sync_api import sync_playwright

from PIL import Image, ImageDraw
import time

from dotenv import load_dotenv

load_dotenv()


def screenshot_tests():
    simplex = Simplex(api_key=os.getenv("SIMPLEX_API_KEY"))
    image = "netflix.png"
    screenshot = Image.open(image)

    start_time = time.time()
    bbox = simplex.find_element("dark mode icon", screenshot)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    print(bbox)

    start_time = time.time()
    action = simplex.step_to_action("click and enter email address", screenshot)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    print(action)


def execute_action_test():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        driver = browser.new_page()
        
        simplex = Simplex(api_key=os.getenv("SIMPLEX_API_KEY"), driver=driver)
        simplex.goto("https://www.netflix.com/")
        # actions = [['CLICK', 'email field'], ['TYPE', 'email address']]
        actions = [['WAIT', '4000'], ['SCROLL', '400']]
        for action in actions:
            simplex.execute_action(action)

        driver.wait_for_timeout(3000)
        browser.close()

def do_test():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        driver = browser.new_page()
        simplex = Simplex(api_key=os.getenv("SIMPLEX_API_KEY"), driver=driver)
        simplex.goto("https://www.netflix.com/")
        simplex.do("click and enter email address")
        driver.wait_for_timeout(3000)
        browser.close()


def cgtrader_test():
    assets = ["victorian chair", "iphone"]
    urls = []

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        driver = browser.new_page()
        simplex = Simplex(api_key=os.getenv("SIMPLEX_API_KEY"), driver=driver)
        for asset in assets:
            simplex.goto("https://www.cgtrader.com/")
            simplex.do(f"search for {asset}")  
            simplex.do("click on search button")
            simplex.do(f"click on the first product")
            driver.wait_for_timeout(3000)

            urls.append(simplex.driver.url)

        driver.close()
        browser.close()

    print(urls)

def draw_bbox(bbox, image):
    draw = ImageDraw.Draw(image)
    draw.rectangle(bbox, outline='red', width=3)
    image.save('bbox_visualization.png')


if __name__ == "__main__":
    cgtrader_test()
    
    