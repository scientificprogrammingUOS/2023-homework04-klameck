import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    for i in [loc, scale, lower_bound, upper_bound]:
        if not isinstance(i, int or float):
            raise TypeError(f"Your {i} is a {type(loc)} not a flot or an int!")
    
    if lower_bound >= upper_bound:
        raise ValueError("Your lower bound must be smaller then your upper bound!")
    
    # 100 samples of Gaussian distribution with respect to given loc, scale
    gauss = np.random.normal(loc, scale, 100)
    # Filtering first for the lower, then for the upper bound:
    gauss = gauss[gauss > lower_bound]
    gauss = gauss[gauss < upper_bound]

    return (np.mean(gauss), np.std(gauss))



if __name__ == "__main__":
    # use this for your own testing!
    print(gaussian_analysis(5, 10, 0, 10))

