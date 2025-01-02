import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simplex import Simplex
from simplex.utils import center_bbox

from PIL import Image, ImageDraw
import time

from dotenv import load_dotenv

load_dotenv()


if __name__ == "__main__":
    simplex = Simplex(api_key=os.getenv("SIMPLEX_API_KEY"))
    
    image = "/home/ubuntu/supreme-waffle/images/state.png"
    screenshot = Image.open(image)

    start_time = time.time()
    bbox = simplex.find_element("'Waitless", screenshot)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

    center = center_bbox(bbox)
    center_image = screenshot.copy()
    draw = ImageDraw.Draw(center_image)
    draw.ellipse((center[0] - 5, center[1] - 5, center[0] + 5, center[1] + 5), fill="red")
    center_image.save("center.png")
