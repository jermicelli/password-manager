import tkinter as tk
from tkinter.constants import LEFT
from PasswordManager.Database.MPwd import MPassword
from PasswordManager.GUI.login import LoginFrame

class SetupFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		# colors
		self.primaryColor = '#4479ff'
		self.backgroundColor = '#000000'
		self.surface1Color = '#121212'
		self.surface2Color = '#212121'
		self.successColor = '#03dac6'
		self.errorColor = '#cf6679'
		self.priTextColor = '#000000'
		self.secTextColor = '#ffffff'

		# fonts
		self.entryFont = ("Rockwell", 12)
		self.labelFont = ("Rockwell", 12, "bold")

		self.controller = controller
		

		self.setupFrame = tk.LabelFrame(self, text="Setup", bg=self.backgroundColor, fg=self.secTextColor)
		self.setupFrame.place(relx=0, rely=0, relwidth=1, relheight=1)
		self.titleLabel = tk.Label(self.setupFrame, text='Setup', bg = self.backgroundColor, fg = self.primaryColor, font=("Rockwell", 18, "bold"))
		self.titleLabel.place(relx=0.25, rely=0.1, relheight=0.1, relwidth=0.5)
		# User will enter the password for the first time
		self.passLabel = tk.Label(self.setupFrame, text = "Password", font = self.labelFont, bg=self.backgroundColor, fg=self.secTextColor)
		self.passLabel.place(relx=0.25, rely=0.66, relwidth=0.5, relheight=0.07)
		self.passentry = tk.Entry(self.setupFrame, show = "*", width = 20, bd = 2, font = self.entryFont, bg=self.surface1Color, fg=self.secTextColor)
		self.passentry.place(relx=0.25, rely=0.72, relwidth=0.5, relheight=0.05)
		self.passentry.delete(0, 'end')
		self.enter = tk.Button(self.setupFrame, text = "Enter", bg=self.primaryColor, fg=self.secTextColor, font = self.labelFont, command = lambda:[self.insertPass()])
		self.enter.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.07)
	
	def insertPass(self):
		mp = MPassword()
		pwd = self.passentry.get()
		mp.create_password(pwd)
		confirmInsertLabel = tk.Label(self.setupFrame, text = "Successful", bg = self.successColor, fg = self.priTextColor, font = self.labelFont)
		confirmInsertLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
		confirmInsertLabel.after(2000, confirmInsertLabel.destroy)
		self.controller.show_frame(LoginFrame)

