"""
program: investmentcalc.py
author: trevor
"""
from breezypythongui import EasyFrame
import math

class TextAreaDemo(EasyFrame):
	# an investment calculator demonstrates the use of a multi- line text area
	def __init__(self):
		EasyFrame.__init__(self, "Investment Calculator")
		self.addLabel(text = "Initial Amount", row = 0, column = 0)
		self.addLabel(text = "Number of years", row = 1, column = 0)
		self.addLabel(text = "Interest rate in %", row = 2, column = 0)
		self.amount = self.addFloatField(value = 0.0, row = 0, column = 1)
		self.period = self.addIntegerField(value = 0, row = 1, column = 1)
		self.rate = self.addIntegerField(value = 0, row = 2, column = 1)
		
		self.outputArea = self.addTextArea("", row = 4, column = 0, columnspan = 2, width = 50, height = 15)
		self.compute = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)
		
	# event handling method
	def compute(self):
		# computeds the investment schedule based on the inputs and outputs the schedule
		#obtain and validate inputs
		startBalance = self.amount.getNumber()
		rate = self.rate.getNumber() / 100
		years = self.period.getNumber()
		if startBalance == 0 or rate == 0 or years == 0:
			return
		# set the header for the table
		result = "%4s%18s%10s%16s\n" % ("Year", "Starting Balance", "Interest", "Ending Balance")
		
		# compute and append the results for each years
		totalInterest = 0.0
		for year in range(1, years + 1):
			interest = startBalance * rate
			endBalance = startBalance + interest
			result += "%4d%18.2f%10.2f%16.2f\n" % (year, startBalance, interest, endBalance)
			startBalance = endBalance
			totalInterest += interest
			
		# append the totals for the period
		result += "Ending Balance: $%0.2f\n" % endBalance
		result += "Total Interst Earned: $%0.2f\n" % totalInterest
		
		# output the result while preserving read-only status
		self.outputArea["state"] = "normal"
		self.outputArea.setText(result)
		self.outputArea["state"] = "disabled"
		
def main():
	TextAreaDemo().mainloop()
	
if __name__ == "__main__":
	main()