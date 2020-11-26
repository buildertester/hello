def Hello(*names):
    """Function Concatenates 'Hello ' to the argument
    
    ----------
    Arguments
    names- must be a string datatype, multiple strings 
    can be provided with comma separation
    
    ----------
    Example
        Hello('buildertester', 'Bob', 'Sarah')
        
    Output
        Hello buildertester
        Hello Bob
        Hello Sarah"""
    
    for name in names:
        print('Hello '+ name)
