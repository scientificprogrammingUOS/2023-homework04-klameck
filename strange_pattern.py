import numpy as np

# implement the function strange pattern

def strange_pattern(shape_t:tuple):
    h = shape_t[0]
    w = shape_t[1]
    sp = np.repeat([False], h*w).reshape(shape_t)
    
    sp[0:h:3, 0:w:3] = True
    sp[1:h:3, 2:w:3] = True
    sp[2:h:3, 1:w:3] = True
    
    return sp


if __name__ == "__main__":
    # use this for your own testing!
    print(strange_pattern((2,2)))
    pass
