import numpy as np 

# implement your function to combine two numpy arrays 

def combination(arr1:np.array, arr2:np.array, axis = 0):
    # Remove unnecessary dimensions:
    arr1 = arr1.squeeze()
    arr2 = arr2.squeeze()

    try:
        return np.concatenate((arr1, arr2), axis)
    except :
        raise ValueError(f"""Your arrays are out of shape! 
            Your first array has the dimensions {arr1.shape}, 
            your second array has the shape {arr2.shape}. 
            You can't combine them on axis {axis}.""")


if __name__ == "__main__":
    # use this for your own testing!
    a = np.arange(10).reshape((2,5))
    b = np.arange(15).reshape((3,5))
    print(combination(a,b))
