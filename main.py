from color_detector import Color_Detector
from ui import UI
# ui = UI()
img = "oranges.jpg"
CD = Color_Detector(img)
rgb_value = CD.find_dominant_color()
color_name = CD.get_color_name(rgb_value)
print(f"The color that is repeated the most in the image is: {color_name}")
