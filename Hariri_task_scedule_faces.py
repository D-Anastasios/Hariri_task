""" Hariri faces scedule maker

This script makes the scedule and exports it in an excel file in the current working directory for the 
blocks with faces in a Hariri task. 
@author: Anastasios Dadiotis

Attributes:
---------------------------
faces_males:  list 
    A list that containes the names of the images with the male faces
faces_females: list
     a list that containes the names of the images with the male faces
left_right_answer: int
    The sum of left answers (=1) and right answers (=2) to identify for an even number
    of trials, how many trial should have the target left and how many right.
emotion: str
    The name of the emotion to name the exported file.

This script requires that 'random', 'pandas' and 'helper_function' be istalled within the Python environment 
you are running this script in. 

"""

import random
import pandas as pd
import helper_functions as hf

# add the type of file extension to the pictures of emotions
faces_males = hf.add_file_type(["M35SU", "M11SU", "M16SU", "M28SU", "M09SU", "M01SU"], "png")
faces_females = hf.add_file_type(["F24SU", "F22SU", "F32SU", "F01SU", "F35SU", "F13SU"], "png")

# sum of left and right answers
left_right_answer = 9 # for 6 trials to have 3 left(1) and 3 right (2) choices

# name of the emotion
emotion = "Surprised" #add the name 

# create dataset
emotion_dataset = hf.faces_scedule(faces_males,faces_females,left_right_answer, emotion)
print(emotion_dataset)

