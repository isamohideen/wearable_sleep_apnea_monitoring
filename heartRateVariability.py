import pandas as pd
import numpy as np

rr = []

# reads the data from the csv file
df = pd.read_csv("Book5.csv", skipinitialspace=True)

# takes the heart rate data from the csv, calculates RR intervals and adds it to a list
for x in df.HR:
     x = 60000/x
     rr.append(x)

# converts it to an numpy array
rr = np.array(rr)

# calculates HRV metrics
def timeDomain(rr):
    results = {}

    hr = df.HR

    results['Mean RR (ms)'] = np.mean(rr)
    results['STD RR/SDNN (ms)'] = np.std(rr)
    results['Mean HR (Kubios style) (beats/min)'] = 60000 / np.mean(rr)
    results['Mean HR (beats/min)'] = np.mean(hr)
    results['STD HR (beats/min)'] = np.std(hr)
    results['Min HR (beats/min)'] = np.min(hr)
    results['Max HR (beats/min)'] = np.max(hr)
    results['RMSSD (ms)'] = np.sqrt(np.mean(np.square(np.diff(rr))))
    results['NNxx'] = np.sum(np.abs(np.diff(rr)) > 50) * 1
    results['pNNxx (%)'] = 100 * np.sum((np.abs(np.diff(rr)) > 50) * 1) / len(rr)
    return results


# outputs HRV metrics
print("Heart Rate Variability Metrics: ")
for k, v in timeDomain(rr).items():
    print("- %s: %.2f" % (k, v))

testArray = np.array([800, 850, 860, 880, 810, 790])

# verifies that the length of the array storing rr intervals is equal to the length of the dataframe storing heart rates
def test_one():
    assert len(rr) == df.HR.size

# verifies that the equation used to calculate RMSDD is accurate
def test_two():
    assert np.sqrt(np.mean(np.square(np.diff(testArray)))) == 40.74309757492672

# checks that the outputted SDNN value is correct
def test_three():
    assert timeDomain(rr).get("STD RR/SDNN (ms)") == np.std(rr)
