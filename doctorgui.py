"""
Program: doctorGUI.py
Author: Letisha Rahming
Date Created
Date Completed
Last Updated
Description: 

"""

from breezypythongui import EasyFrame
import random

#  Global variables and constants
hedges = ("Please tell me more.", "Many of my patients tell me the same thing", "Please continue.", "Go on.")
qualifiers = ("Why do you say that ", "You seem to think that ", "Can you explain why ")
replacements = { "I": "you", "I am": "you are","my": "your", "I'm": "you're", "me":"you", "mine":"yours", "I've": "You've" "I've"}

class doctorCrane(EasyFrame):
	def __init__(self):
		EasyFrame.__init__(self, title = "Doctor F. Crane")
		self.addLabel(text = "Good Morning.  Hope you are well.", row = 0, column = 0, sticky = "NSEW")
		self.addLabel(text = "This is Dr. Fraiser Crane, how can I help you today?", row = 1, column = 0, sticky = "NSEW")
		self.userText = self.addTextField(text = "", row = 2, column = 0, sticky = "NSEW")
		#Bind the userText field to the enter key
		self.userText.bind("<Return>", lambda event: self.reply())
		self.responseLabel = self.addLabel(text = "", row = 3, column = 0, sticky = "NSEW")
		self.addButton(text = "Submit", row = 4, column = 0, command = self.reply)

	def reply(self):
		sentence = self.userText.getText()
		"""builds and returns a reply sentence"""
		probability = random.randint(1,4)
		if probability == 1:
			self.responseLabel["text"] = random.choice(hedges)
		else:
			self.responseLabel["text"] = random.choice(qualifiers)+ changePerson(sentence)
def changePerson(sentence):
	words = sentence.split()
	replywords = []
	for word in words:
		replywords.append(replacements.get(word, word))
	return " ".join(replywords)
def main():
	doctorCrane().mainloop()
main()