import os
import tempfile

import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageGrab
from skimage.color import rgb2gray
from skimage.feature import match_template
from skimage.io import imread

inventory_screen_bbox = 1706, 780, 1887, 1038


def get_inventory_image():
    image = ImageGrab.grab(inventory_screen_bbox)
    return image


def get_log_image():
    script_dir = os.path.dirname(__file__)
    rel_log_path = "assets" + os.sep + "Logs.png"
    log_image = imread(os.path.join(script_dir, rel_log_path))
    # Drop channels
    log_image = log_image[:, :, :3]
    #log_image = rgb2gray(log_image)
    return log_image


def check_for_inventory_logs():
    inv = get_inventory_image()
    inv.save(tempfile.gettempdir() + os.sep + 'inventory.png')
    inv_image = imread(tempfile.gettempdir() + os.sep + 'inventory.png')
    #inv_image = rgb2gray(inv_image)
    log_image = get_log_image()

    print(inv_image.shape, log_image.shape)
    result = match_template(inv_image, log_image)
    print(result.shape)
    print(result.ndim)
    ij = np.unravel_index(np.argmax(result), result.shape)
    x, y, rgb = ij[::-1]

    fig = plt.figure(figsize=(8, 3))
    ax1 = plt.subplot(1, 3, 1)
    ax2 = plt.subplot(1, 3, 2)
    ax3 = plt.subplot(1, 3, 3, sharex=ax2, sharey=ax2)

    ax1.imshow(log_image, cmap=plt.cm.gray)
    ax1.set_axis_off()
    ax1.set_title('template')

    ax2.imshow(inv_image, cmap=plt.cm.gray)
    ax2.set_axis_off()
    ax2.set_title('image')
    # highlight matched region
    hlogs, wlogs, rgblogs = log_image.shape
    rect = plt.Rectangle((x, y), wlogs, hlogs, edgecolor='r', facecolor='none')
    ax2.add_patch(rect)

    ax3.imshow(result.squeeze())
    ax3.set_axis_off()
    ax3.set_title('`match_template\nresult')
    # highlight matched region
    ax3.autoscale(False)
    ax3.plot(x, y, 'o', markeredgecolor='r', markerfacecolor='none', markersize=10)

    plt.show()
