import pandas as pd
from matplotlib import pyplot as plt


#num_measurements = int(input("Specify the number of measurements."))
num_measurements = 25

# read data from file
data = pd.read_csv('temperatures.csv', nrows=num_measurements)
temperatures = data['Air temperature (degC)']


# compute statistics
def mean_temperature(temperatures,num_measurements):
	return sum(temperatures)/num_measurements

mean=mean_temperature(temperatures,num_measurements)


#plotting function
def plotting(mean):
	plt.plot(temperatures, 'r-')
	plt.axhline(y=mean, color='b', linestyle='--')
	plt.savefig('25.png')
	plt.clf()

#test function
def test_mean_temperature():
	temperatures = [15,20,25]
	expected_mean = 20
	resulted_mean = mean_temperature(temperatures,3)
	assert(abs(expected_mean-resulted_mean)<1e-06)