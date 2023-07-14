""" Helper functions to build the scedule for the faces trial for a Hariri task 
    This file should be imported as a module.

List of Contained Functions
----------
jitter_generator(mu, size, min):
     Creates Jitters for fmri experiments following a Poisson distribution.

add_element_to_list(list_name, element, start, stop, step): function
    Adds an element to a list in specific indexes as with range function.

add_file_type(filelist, filetype): function
    Adds the type of a file at the end of the filename in a list of files.

pop_random(lst): function
    Selects and removes a random element from a list.

pair_maker(lst): function
    Makes random and unique pairs from a list.

target_and_append: function
    Creates a target and index from a list of pairs and it appends to a dataset.
    
faces_scedule(faces_males, faces_females, left_right_answer, emotion): function
    Creates and exports a scedule of trial for the faces block in Hariri task. 
"""

import random
import pandas as pd 
from scipy.stats import poisson

def jitter_generator(mu, size, min):
    """ Creates Jitters for fmri experiments following a Poisson distribution.
    Parameters
    -----------
    mu: int
        The mean of the distribution.
    size: int
        The sample size of the distribution.
    min: int
        The min value that each jitter element should have. For instane you do not want jitter = 0.
    """
    # create a variable to finish 
    check = False

    # a while loop tha runs until the correct jitters have been generated
    while not check:
        jitter_scedule = list(poisson.rvs(mu=mu, size = size))
        check = all(jitter > min for jitter in jitter_scedule) # teminate if all the elements > min
    return jitter_scedule



def add_element_to_list(list_name, element, start, stop, step):
    """ Adds an element to a list in specific indexes as with range function.

    Parameters
    ------------
    list_name: a list
        The list that the element will be added.
    element: all types
        The element that will be added
    start: int
        Starting point of the range function.
    stop: int
        Ending point of the range function.
    step: int
        Step of the range function.
    
    Returns
    -----------
    None
    """
    for i in range (start,stop, step):
        list_name.insert(i, element)

def add_file_type(filelist, filetype):
    """Adds the type of a file at the end of the filename in a list of files.
    
    Parameters
    ------------
    filelist: a list
        A list of files to be added the type.
    filetype: str
        The extension to be added to the item of the list to indicate the file type.
        example "png" or "jpeg"
    
    Returns: 
    -----------
    new_filelist: a list
        A new filelist where all the files have the prefered extension.
    """
    new_filelist = []
    for file in filelist:
        new_filename = f'{file}.{filetype}'
        new_filelist.append(new_filename)
    return new_filelist

def pop_random(lst):
    """Selects and removes a random element from a list."""

    idx = random.randrange(0,len(lst))
    return lst.pop(idx)


def pair_maker(lst):
    """ Makes random unique pairs from a list

    Parameters
    ----------
    lst: a list
    
    Returns
    ---------
    Pairs: a list
        A list contained of multiple list of 2 elements
    """
    pairs = []
    while lst:
        rand1 = pop_random(lst)
        rand2 = pop_random(lst)
        pair = [rand1, rand2]
        pairs.append(pair)

    return pairs
    

def target_and_append(pairs,df):
    """Chooses randomly one of the two elements of the pair to   
       create a target and the index for the correct answer and 
       after that in appends the four elements to a new row 
       of a dataset

       Parameters
       -----------
       lst: a list
            The list that contains the pairs
        df: a df
            A dataframe that will be appended each trial

       Returns
       -----------
       None
    """
    for pair in pairs:
        chosen_index = random.randint(0, len(pair)-1)
        target = pair[chosen_index]
        pair.append(target)
        pair.append((chosen_index+1)) # We add 1 to the index so it will be 1 if the target face is matching the left face and 2 if the target face is mathcing the right one.
        df.loc[len(df)] = pair

def faces_scedule(faces_males, faces_females, left_right_answer, emotion):
    """" A function that takes as arguments two lists and a label 
         and returns and exports a dataset as excel file. 
    Parameters
    -----------
    lst_males: list
        A list with the faces of males
    lst females: list
        A list with the faces of females
    emotion: str
        A label of the emotion in the faces
    left_right_answer: int
        Since left choice = 1 and right choice = 2 by using the sum we can compute how 
        left and right choices we want in our dataset. For example: with 6 trials to have 3 left (1)
        and 3 right (2) we need a sum = 9 = (3*1 + 3*2}
    
    Returns
    ------------
    df: pandas dataframe
        A shuffled dataframe that containes the two faces that are shuffled,
        a target (one of the two faces) and an index for the correct answer. 
        Also it exports on current directory the excel file with the name
        emotion.xlsx

    """
    # Run a 
    while True:
        # create an empty dataframe
        df = pd.DataFrame(columns = ["stimuli_left", "stimuli_right", "target", "correct_answer"])
        
        # copy the lists so the while loop does not run into an empty list after the first unsuccesful iteration 
        lst_males = faces_males.copy()
        lst_females = faces_females.copy()

        # create the scedule for male faces
        pairs_m = pair_maker(lst_males)
        target_and_append(pairs_m, df)

        #create the scedule for female faces
        pairs_f = pair_maker(lst_females)
        target_and_append(pairs_f, df)

        # check if there is the correct proportion of the right and left correct answers        
        sum_of_answers = df['correct_answer'].sum()
        if sum_of_answers == left_right_answer:
            break
 
    #shuffle the rows of the dataset
    df = df.sample(frac=1)
        
    # saving the excel
    df.to_excel(rf'{emotion}.xlsx', index=False)
    return df
