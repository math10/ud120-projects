#!/usr/bin/python

def cmp(item):
    return item[2]
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    cleaned_data = sortByError(predictions, ages, net_worths)
    tmp = int(l * .1);
    cleaned_data = cleaned_data[:(l-tmp)]
    return cleaned_data

def sortByError(predictions, ages, net_worths):
    l = len(ages)
    cleaned_data = []
    for i in range(l):
        error = abs(predictions[i] - net_worths[i])
        data = [ages[i], net_worths[i], error, i]
        cleaned_data.append(data)
    cleaned_data = sorted(cleaned_data, key=cmp)
    return cleaned_data
