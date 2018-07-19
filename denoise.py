
def motion_24_friston(dataframe):

    import pandas as pd
    import numpy as np 

	
    """Simple function that calculates 24 motion parameters from pandas dataframe. 
    
    Parameters
    ----------
    dataframe: pandas dataframe including 6 movement parameters with headers
    
    Returns
    -------
    motion_24_friston:  pandas dataframe including 24 motion parameters
    
    - the first 6 are the motion parameters
    - the next 6 are the temporal difference of motion parameters ('_td' suffix)
    - the next 12 are the square of the motion parameters and the differenced values ('_sqrt' suffix)
      
    """

    motion_24_friston = dataframe 

    for col in dataframe.columns:
        temp_diff = np.roll(dataframe[col], 1, axis = 0)
        temp_diff[0] = 0
        temp_diff = pd.DataFrame(temp_diff)
        motion_24_friston[col + '_td'] = temp_diff
    
    for col in motion_24_friston.columns:
        sqrt = motion_24_friston[col] ** 2
        motion_24_friston[col + '_sqrt'] = sqrt
    
    return motion_24_friston


def scrubbing(fd, thr = 0.5, before = True, after = True):
    
    """Function that calculates motion outliers (frames with motion above threshold_.
    
    Parameters
    ----------
    fd:      pandas dataframe including frame-wise displacement (FD)
    thr:     threshold (default: 0.5)
    before:  marks frames before outlier datapoint (default: True)
    after:   marks frames after outlier datapoint (default: True)
    
    Returns
    -------
    scrubbing:  pandas dataframe including all ourliers datapoints
          
    """
    
    import pandas as pd
    import numpy as np
    
    scrubbing = pd.DataFrame()
    fd.loc[0] = 0
    fd = confounds_fd.astype(float)
    
    scrub1 = confounds_fd > thr
    scrub1 = scrub1.astype(int)
    scrubbing['scrubbing'] = scrub1
    
    if before == True:
        scrub2 = np.roll(scrubbing['scrubbing'], -1, axis = 0)
        scrub2[0] = 0
        scrubbing['scrubbing_bef'] =  scrub2
        
    if after == True:
        scrub3 = np.roll(scrubbing['scrubbing'], 1, axis = 0)
        scrub3[0] = 0
        scrubbing['scrubbing_aft'] =  scrub3
        
    return scrubbing
