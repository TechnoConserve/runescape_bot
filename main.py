import random

from PIL import Image
from PIL import ImageGrab
import pyautogui

from items import check_for_inventory_logs

# Screen coords in the form of x0, y0, x1, y1
full_screen_bbox = 1109, 309, 1917, 1074
first_item_bbox = 1707, 781, 1751, 818
second_item_bbox = 1753, 781, 1793, 818


def load_image(img_file):
    im = Image.open(img_file)


def grab_screen():
    image = ImageGrab.grab(full_screen_bbox)
    return image


def randomize_coord(bbox):
    """Return a coordinate that has been randomized within
    a given bounding box."""
    x = random.randint(bbox[0], bbox[2])
    y = random.randint(bbox[1], bbox[3])
    return x, y


def show_game_screen():
    # Get an image of the lower right corner of the screen
    screen = grab_screen()
    screen.show()


def simulate_click(bbox):
    x, y = randomize_coord(bbox)
    # Move the cursor to given cords within one to ten seconds
    pause = random.uniform(1, 3)
    print("Moving to {}, {} in {:.2f} seconds".format(x, y, pause))
    pyautogui.moveTo(x, y, pause)
    pyautogui.click(x, y)


def main():
    check_for_inventory_logs()
    #print("Activating the first inventory item")
    #simulate_click(first_item_bbox)

    #print("Activating the second inventory item")
    #simulate_click(second_item_bbox)


if __name__ == "__main__":
    main()
