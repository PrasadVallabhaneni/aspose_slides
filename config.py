import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PPTX_PATH = os.path.join(BASE_DIR, "assets", "assignment.pptx")
OUTPUT_PATH = os.path.join(BASE_DIR, "output", "modified-assigment.pptx")
CAR_IMAGE_PATH = os.path.join(BASE_DIR, "assets", "car-image.jpeg")

NUM_TO_ALPHA = {"01": "A", "02": "B", "03": "C", "04": "D", "05": "E", "06": "F"}

TARGET_CHART_COLOR = (0, 32, 96)  
NEW_CHART_COLOR = (255, 0, 0) 