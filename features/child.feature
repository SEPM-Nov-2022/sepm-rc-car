Feature: Basic controls for the child

	Scenario: As a child, I want to control the movement of the race car.
		Given the app is connected to the race car and the race car is charged
		When the user pushes a direction
		Then the car moves in that direction

	Scenario: As a child, I want to honk the horn.
		Given the app is connected to the race car and the race car is charged
		When the user pushes the "horn" button
		Then the car sounds the horn

	Scenario: As a child, I want to change the LED colours of the race car.
		Given the app is connected to the race car and the race car is charged
		When the user selects a LED colour scheme
		Then the car LEDs change colour to the selected scheme
		And the "colour scheme" is updated in the app

	# Scenario: As a child, I want to customise the driver’s appearance.
	# 	Given the app is connected to the race car and the race car is charged
	# 	When the user pushes the "customise driver" button
	# 	Then the user is prompted to set "driver’s appearance"
	# 	And the appearance is updated on the race car
	# 	And the "appearance" is updated in the app

	# Scenario: As a child, I want to see how much range is left in the battery.
	# 	Given the app is connected to the race car and the race car is charged
	# 	When the user pushes the "battery" button
	# 	Then the app displays the estimated range left in the battery

	Scenario: As a child, I want to see that there is no battery
		Given the race car is out of battery
		When the user tries to connect the remote
		Then the remote suggests that the race care is out of range or the battery is empty
