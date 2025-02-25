'''
Mini wish simulator to demonstrate Monte Carlo sampling!!
Try to guess the true probability distribution for the characters through the samples.
'''

# TODO: edit this to the number of samples you want!
# 1 will give you just the one wish
# 2+ will give you a count of how many of each character you got
trials = 1

from PIL import Image
import matplotlib.pyplot as plt
from term_image.image import AutoImage, Size
from true_probabilities import characters
import random
import numpy as np

images = {
    "qiqi": Image.open('qiqi.png'),
    "amber": Image.open('amber.png'),
    "furina": Image.open('furina.png'),
} 

mc_samples = { char: 0 for char in characters.keys() }

total_probability = sum([x for x in characters.values()])
for i in range(trials):
    result = random.randint(1, total_probability)
    cur_count = 0
    for char, count in characters.items():
        cur_count += count
        if (cur_count >= result):
            result_char = char
            break
    if trials > 1:
        mc_samples[result_char] += 1
    else:
        npimg = np.asarray(images[char])
        plt.imshow(npimg)
        plt.draw()
        plt.pause(2) 
        plt.close()
        print("you pulled " + char + "!")

if trials > 1:
    for char in characters.keys():
        img = AutoImage(images[char])
        img.size = (15,7)
        print(img, char, "was pulled", + mc_samples[char], "times")
