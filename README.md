# PAC-SWaP
Portable Atomic Clocks - Size, Weight and Power


# PURPOSE
- This repository is inteneded to be a resource for those interested in the growing world of portable atomic clocks. Specifically looking at the barriers to deployment: the Size, Weight and Power (SWaP) of the clock, and how these affects clock performance.

# INCLUSION
- Clocks are included that are **portable**. This might be an obvious quality (for example the CSAC), or something that is stated in a publication. In a general sense it is a clock that can be moved and operate outside of the labratory.


# FOCUS
- The main focus here is on how the SWaP of a system affects its performance. For clarification these are broken down as follows:
## SWaP
- Overall SWaP has units of cm<sup>3</sup>kgW. This comes from:
    - **Size**: Choice of volume units is arbitrary, but herein I have used the unts of cm<sup>3</sup>. Total size includes all system components required for actual operation.
        - for example: physics package + photonics + external cavity + fequency comb = total size. 
    - **Weight**: Units of kgs. I have used the weight of the entire device. As per Size,  weight of everything required for actual operation. 
    - **Power**: Units of Watts. I have used the power of the entire device. As per Size and Weight, the power demand of everything required for actual operation.

## Performance 
- Clock variability (ADEV) has been used. Plots are initially drawn using a 1 second integration time, and subsequent plots can be created using longer integration times if available.



# DATA and PLOTTING
- All data is contained in the SWAP_DATA.csv file on the main branch.
- Performance and SWaP numbers have been taken from publications, official websties, or spec sheets. Where this was not possible I contacted the authors or manufacturer. 
- In all cases I have attempted to present the numbers accurately and in good faith.
- If i have made any mistakes, or the numbers need to be updated, please let me know.

- All code for plots is kept in the PLOTTING.ipynb notebook.
- I dont claim to be an expert at python or plotly, so any help or adivce on how to make these plots 'better' would be much appreciated. 

# FUTURE
- I would like to extend SWaP to also include other barriers to deployability:
    - **Cost**: How much does the system cost? For research clocks this may be hard/not possible to determine. 
    - **Personel**: How many people are required to run the system? For many of the modern portabloe systems this may be a single person to turn the key and begin operation. Research clocks may need an entire team of people to set up and run the clock.


# DISCLAIMER
- I dont claim that this is a comprehensive database of every single device, however I plan to keep it updated as new devices/results are published/announced. As well as adding anything current or from the past that I may have missed.
- **Its not a competition!**. I dont present this as a ranking or leaderboard of performance. Just a representation of where the technology stands.

