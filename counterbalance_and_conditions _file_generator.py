"""Script to generate the groups for the participants with counterbalanced block. Uses full permutations
TODO: Add a better documentation and jittered time.

"""

import itertools
import pandas as pd
from scipy.stats import poisson
from string import ascii_uppercase as aup
import helper_functions as hf

#a list of possible conditions
my_Blocks=['Fearful.xlsx', 'Angry.xlsx', 'Surprised.xlsx', 'Neutral.xlsx']

# get all permutations (of length 4)
allPerms = [list(p) for p in itertools.permutations(my_Blocks)] # also make them a list to use them in the for loop below

# a message for the instuctions in each block
ready_MSG = []
hf.add_element_to_list(ready_MSG, "Comparez les formes", 0,5,1)
hf.add_element_to_list(ready_MSG, "Comparez les visages", 1,9,2)

# generate random values from Poisson distribution with mean = 4 and sample size = 9
jitter = list(poisson.rvs(mu=4, size = 10))

# check 


# create the 
for (this_perm, letter) in zip (allPerms, aup):

    hf.add_element_to_list(this_perm, "shapes.xlsx", 0, 10,2)

    df = pd.DataFrame()
    df["condsFile"] = this_perm
    df["readyMSG"] = ready_MSG

    # saving the excel
    df.to_excel(rf'chooseBlocks{letter}.xlsx', index=False)
