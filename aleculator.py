#Attempt at quick and dirty Python script for use as a simple ABV calculator

BEER_CONSTANT = 131.25

print('\nWelcome to the Command Line Aleculator!!!\n')

og = float(input('Enter OG: '))

fg = float(input('Enter FG: '))

if fg > og:
	print('\nUh oh! There appears to be an error...your Final Gravity should be less than your Original Gravity. Please check your readings and try again.')
else:
	abv = ((og - fg) * BEER_CONSTANT)

	print('\nYour alcohol by volume is: ' + str(abv))
print('\nThank you for using Aleculator! Good bye!\n')

