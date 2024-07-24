# PAC-SWaP
Portable Atomic Clocks - Size, Weight and Power repository.

# Table of Contents
1. [LICENSE AND ATTRIBUTION](#license-and-attribution)
2. [PURPOSE](#purpose)
3. [INCLUSION CRITERIA](#inclusion-criteria)
4. [FOCUS](#focus)
5. [DATA AND PLOTTING](#data-and-plotting)
6. [FUTURE](#future)
7. [DISCLAIMER](#disclaimer)



# LICENSE AND ATTRIBUTION
All information and materials provided in this repository are licensed under the [CC-BY-SA-4.0 license](https://github.com/a1120960/PAC-SWaP?tab=readme-ov-file#). You are free to share and adapt the content as long as you provide appropriate credit, indicate any changes made, and distribute your contributions under the same license. 

For citation purposes, please reference our arXiv paper (UPCOMING): 


# PURPOSE
- This repository is intended to be a resource for those interested and or involved in the growing world of portable atomic clocks. Specifically looking at the barriers to deployment: the Size, Weight and Power (SWaP) of the clock, and how these affects clock performance. 
- I wont claim it is an authority on PAC-SWaP, but will hopefully serve as the starting point for literature reviews and the like. 
- Over time I'd like this repository to track the progress of clock technology as the new generation of optical atomic clocks leave the laboratory and become commercially available. 
- The all data and plots shown on the [IPAS Portable Atomic Clocks](https://www.adelaide.edu.au/ipas/research-groups/precision-measurement-group/portable-atomic-clocks/precision-timing-plot) page and the [PAC-SWAP page](https://a1120960.github.io/PAC-SWaP/) will be available in this repository. 


# INCLUSION CRITERIA 
- Clocks are included that are **portable**. This might be an obvious quality (for example the CSAC), or something that is stated as such in a publication or promotional material. In a general sense it is a clock that can be moved and operated outside of the laboratory.
- Has some performance measurements and available - publication, pre-publication, spec sheet etc
- At this point I have only included the most common current microwave atomic clocks. There are more, however the intention is to compare the new generation of portable optical atomic clocks to those clocks that currently represent the gold standard. 
- The INCLUDE field in the SWAP_DATA.csv determines wether a clock will be in the plot. examples of why this might be set to 0:
    - There may be some clocks that have currently don't have enough data to be plotted.
    - There may be some clocks that have some debate about wether they meet the current inclusion criteria, for example the cryogenic sapphire oscillator (CSO)

## Portability vs Deployability
- At the moment the two terms will be used interchangeably. However they do have different meanings with respect to clocks:
    - **Portable**: A clock that can be taken outside the laboratory, but not necessarily taken anywhere. For example it may need specific power demands, vehicle access, extended time to setup etc. 
    - **Deployable**: A clock that can be moved and used across varied environments, can be setup and running quickly. 


# FOCUS
- The main focus here is on how the SWaP of a system affects its performance. For clarification they are defined as follows:
## SWaP
- Overall SWaP has units of cm<sup>3</sup>kgW. This comes from:
    - **Size**: Choice of volume units is arbitrary, but herein I have used the units of cm<sup>3</sup>. Total size includes all system components required for actual operation.
        - for example: physics package + photonics + external cavity + frequency comb = total size. 
    - **Weight**: Units of kgs. I have used the weight of the entire device. As per Size,  weight of everything required for actual operation. 
    - **Power**: Units of Watts. I have used the power of the entire device. As per Size and Weight, the power demand of everything required for actual operation.

## Performance 
- Performance values are the clock frequency stability (ADEV). Plots are initially drawn using a 1 second integration time. Longer integration times (1000 and 10,000) are also plotted if and where that information is available. Where there are multiple ADEV integration times, these are connected with a thin vertical line to the 1 sec marker.


# DATA and PLOTTING
- All data is contained in the SWAP_DATA.csv file on the main branch.
- Performance and SWaP numbers have been taken from publications, official websites, or spec sheets. Where this was not possible I contacted the authors or manufacturer. 
- References (where available) are all in SWAP_DATA.csv, and linked on the [PAC-SWAP page](https://a1120960.github.io/PAC-SWaP/)
- In all cases I have attempted to present the numbers accurately and in good faith.
- If I have made any mistakes, or the numbers need to be updated, please let me know.

- The code for the main and focussed swap plots are in the file: SWAP-PLOT-MAIN.py
- Any suggestions or advice (or help) on how to make these plots and/or data more accessible would be much appreciated. 

# FUTURE
- I would like to extend **SWaP** to include other significant barriers to deployability. Ideally these would be something that can be easily captured as a value, so that it can be multiplied by the SWaP number. As an example **SWaP-PC** would add:
    - **Personnel**: How many people are required to run the system? For many of the modern portable systems this would be a minimum of a single person to turn the key or press a button, and begin operation. On the other hand some research clocks may need an entire team of people to set up and run the clock. 
    - **Cost**: How much does the system cost? For research clocks this may be hard, if not impossible to determine, or might not want to be revealed.
- Another factor to explore could be device manufacturability, especially at scale. However, unlike cost and personnel, it would be very difficult to assign a simple scalar value to.
 



# DISCLAIMER
- I make no claim that this is a comprehensive database of every single device, however I plan to keep it updated as new devices/results are published/announced. As well as adding anything current or from the past that I have missed.
- **Its not a competition!**. The intention isn't to present this as a ranking or leader-board of clock performance and SWaP. Rather it is just a representation of where the technology currently stands.

