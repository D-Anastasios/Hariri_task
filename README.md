Author: Anastasios Dadiotis 
4/2023
Lyon

# Hariri Task

This is a Hariri Task. Participants have to either match emotional faces or match shapes. The emotions in the face stimuli are Fearful, Surprised, Angry and Neutral. The task is about 10 minutes. There are 4 groups for counterbalancing the participants [A, B, C, D] following a Latin Balanced Square. (To make schedules with a foul counterbalance see the python script 'counterbalance_and_conditions \_file_generator.py'). For more information about the Hariri Task see: [@hariri2002; @nikolova2016; @ahs2013; @herrmann2020] but also see: [@nord2017].

### Face Images:

Faces stimuli have been used from [@goeleven2008]. To create the stimuli for each trial see the python script 'Hariri_task_scedule_faces.py' and the script 'helper_functions.py'.

### Jitters:

There is a jitter after each block of trials. All jitters follow the poisson distribution with mu = 4 and no jitter \< 1. For a python script to create jitters see 'helper_functions.py'.

### References:

Ahs, Fredrik, F. Davis, Adam Gorka, and Ahmad Hariri. "Feature-Based Representations of Emotional Facial Expressions in the Human Amygdala." *Social Cognitive and Affective Neuroscience* 9 (July 24, 2013). <https://doi.org/10.1093/scan/nst112>.

Goeleven, Ellen, Rudi De Raedt, Lemke Leyman, and Bruno Verschuere. "The Karolinska Directed Emotional Faces: A Validation Study." *Cognition & Emotion* 22, no. 6 (September 2008): 1094--1118. <https://doi.org/10.1080/02699930701626582>.

Hariri, Ahmad R., Alessandro Tessitore, Venkata S. Mattay, Francesco Fera, and Daniel R. Weinberger. "The Amygdala Response to Emotional Stimuli: A Comparison of Faces and Scenes." *NeuroImage* 17, no. 1 (September 2002): 317--23. <https://doi.org/10.1006/nimg.2002.1179>.

Herrmann, Luisa, Petya Vicheva, Vanessa Kasties, Lena V. Danyeli, Gregor R. Szycik, Dominik Denzel, Yan Fan, et al. "FMRI Revealed Reduced Amygdala Activation after Nx4 in Mildly to Moderately Stressed Healthy Volunteers in a Randomized, Placebo-Controlled, Cross-Over Trial." *Scientific Reports* 10 (March 2, 2020): 3802. <https://doi.org/10.1038/s41598-020-60392-w>.

Nikolova, Yuliya S., Annchen R. Knodt, Spenser R. Radtke, and Ahmad R. Hariri. "Divergent Responses of the Amygdala and Ventral Striatum Predict Stress-Related Problem Drinking in Young Adults: Possible Differential Markers of Affective and Impulsive Pathways of Risk for Alcohol Use Disorder." *Molecular Psychiatry* 21, no. 3 (March 2016): 348. <https://doi.org/10.1038/mp.2015.85>.

Nord, C.L., A. Gray, C.J. Charpentier, O.J. Robinson, and J.P. Roiser. "Unreliability of Putative FMRI Biomarkers during Emotional Face Processing." *NeuroImage* 156 (August 2017): 119--27. <https://doi.org/10.1016/j.neuroimage.2017.05.024>.

## 
