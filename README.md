# PAC-SWaP
Portable Atomic Clocks - Size, Weight and Power repository.


# PURPOSE
- This repository is intended to be a resource for those interested in the growing world of portable atomic clocks. Specifically looking at the barriers to deployment: the Size, Weight and Power (SWaP) of the clock, and how these affects clock performance. 
- At this point I wont claim it is an authority on PAC-SWaP, but will hopefully serve as the starting point for literature reviews and the like. 
- Over time I'd like this repository to track the progress of clock technology as the new generation of optical atomic clocks leave the laboratory and become commercially available. 
- The all data and plots shown on the [IPAS](https://www.adelaide.edu.au/ipas/research-groups/precision-measurement-group/portable-atomic-clocks/precision-timing-plot) page and the [PAC-SWAP page](https://a1120960.github.io/PAC-SWaP/) will be available in this repository. 


# INCLUSION
- Clocks are included that are **portable**. This might be an obvious quality (for example the CSAC), or something that is stated in a publication. In a general sense it is a clock that can be moved and operate outside of the laboratory.
- Must have some performance measured and available - publication, pre-publication, spec sheet etc
- At this point I have only included the most common current microwave atomic clocks. There are more, however the intention is to compare the new generation of portable optical atomic clocks to those clocks that currently represent the gold standard. 
- The INCLUDE field in the SWAP_DATA.csv determines wether a clock will be in the plot. examples of why this might be set to 0:
    - There may be some clocks that have currently don't have enough data to be plotted.
    - There may be some clocks that have some debate about wether they meet the current criteria, for example the cryogenic sapphire oscillator (CSO)

## Portability vs Deployability
- At the moment the two terms will be used interchangeably. However they do have different meanings with respect to clocks:
    - **Portable**: A clock that can be taken outside the laboratory, but not necessarily taken anywhere. For example it may need specific power demands, vehicle access, extended time to setup etc. 
    - **Deployable**: A clock that can be moved and used across varied environments, can be setup and running quickly. 


# FOCUS
- The main focus here is on how the SWaP of a system affects its performance. For clarification these are broken down as follows:
## SWaP
- Overall SWaP has units of cm<sup>3</sup>kgW. This comes from:
    - **Size**: Choice of volume units is arbitrary, but herein I have used the units of cm<sup>3</sup>. Total size includes all system components required for actual operation.
        - for example: physics package + photonics + external cavity + frequency comb = total size. 
    - **Weight**: Units of kgs. I have used the weight of the entire device. As per Size,  weight of everything required for actual operation. 
    - **Power**: Units of Watts. I have used the power of the entire device. As per Size and Weight, the power demand of everything required for actual operation.

## Performance 
- Clock variability (ADEV) has been used. Plots are initially drawn using a 1 second integration time, and subsequent plots can be created using longer integration times if and where available.



# DATA and PLOTTING
- All data is contained in the SWAP_DATA.csv file on the main branch.
- Performance and SWaP numbers have been taken from publications, official websites, or spec sheets. Where this was not possible I contacted the authors or manufacturer. 
- References (where available) are all in SWAP_DATA.csv 
- In all cases I have attempted to present the numbers accurately and in good faith.
- If i have made any mistakes, or the numbers need to be updated, please let me know.

- The code for the main swap plot is the file: SWAP-PLOT-MAIN.py
- Any help or advice on how to make these plots and/or data more accessible will be much appreciated. 

# FUTURE
- I would like to extend **SWaP** to **SWaP-PC**, which would include other significant barriers to deployability:
    - **Personnel**: How many people are required to run the system? For many of the modern portable systems this may be a single person to turn the key and begin operation. Research clocks may need an entire team of people to set up and run the clock.
    - **Cost**: How much does the system cost? Obviously for the research clocks this may be hard if not possible to determine, or might not want to be revealed.

- As clock technology progresses, I would like the focus to be more on deployable clocks.



# DISCLAIMER
- I don't claim that this is a comprehensive database of every single device, however I plan to keep it updated as new devices/results are published/announced. As well as adding anything current or from the past that I may have missed.
- **Its not a competition!**. The intention isn't to present this as a ranking or leaderboard of performance. Just a representation of where the technology stands.

