import tkinter as tk
from tkinter.font import families
import os.path
from PIL import ImageTk , Image
from PasswordManager.GUI.login import LoginFrame
from PasswordManager.GUI.setup import SetupFrame
from PasswordManager.GUI.searchpass import SearchPassFrame
from PasswordManager.GUI.addpass import AddPassFrame
from PasswordManager.GUI.home import HomeFrame
from PasswordManager.Database.MPwd import MPassword
from PasswordManager.Database.PManagerDatabase import Database
from PasswordManager.Backend.PManagerEncryption import Encryption


Masterpass = MPassword()

Pdb = Database()
Pdb.createPwdTable()

en = Encryption()
#en.generate_key()

class PasswordManagerApp(tk.Tk):
	def __init__(self, *args , **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		tk.Tk.geometry(self, '550x500+450+120')
		tk.Tk.title(self, 'Password Manager')
		tk.Tk.resizable(self, width=False, height=False)
		pwmLogo = tk.PhotoImage(file="images/lock.png")
		pwmLogo = (pwmLogo.zoom(25)).subsample(32)
		tk.Tk.iconphoto(self, True , pwmLogo)

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (LoginFrame, SetupFrame, HomeFrame, SearchPassFrame, AddPassFrame):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		# This will raise setupFrame if opened for first time(means user doesn't exist)
		# And raise loginFrame the rest of the time
		if(not os.path.exists('mpHash.json')):
			self.show_frame(SetupFrame)
		elif(os.path.exists('mpHash.json')):
			self.show_frame(LoginFrame)

	# Raises Frame in all files
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()