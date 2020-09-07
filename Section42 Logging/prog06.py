import logging

a = 5
b = 0

try:
	c = a / b
except Exception as e:
	logging.error("Exception Occurred...", exc_info=True)
