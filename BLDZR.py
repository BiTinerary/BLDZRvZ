import os
import subprocess
import time
import Tkinter as tk
from PIL import ImageTk
import win32api
import win32con
import SendKeys

def Center(toplevel):
	toplevel.update_idletasks()
	w = toplevel.winfo_screenwidth()
	h = toplevel.winfo_screenheight()
	size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
	x = w/2 - size[0]/2
	y = h/2 - size[1]/2
	toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

global icondirectory
icondirectory = "./ProgFiles/Icons/"

class KeyboardTester(tk.Tk): # Custom keyboard tester.
	def __init__(self):
		tk.Tk.__init__(self)

		LABEL1 = tk.Label(self, compound="left", text="Test the keyboard using the four main rows of ASCII characters 0-9 and a-z.")
		LABEL1.grid(row=0, column=0, columnspan=3)

		LABEL2 = tk.Label(self, compound="left", text="ie: 1234567890qwertyuiopasdfghjklzxcvbnm                               ")
		LABEL2.grid(row=1, column=0, columnspan=2)

		INPUTRETURN = tk.Entry(self, bd=5, width=58) # create GUI prompt for end user/character input
		INPUTRETURN.grid(row=2, column=0, columnspan=3) # create ^ and store in a grid

		def ButtonPressVerification(input):
			VERIFICATION = INPUTRETURN.get() # grabs whatever input provided by enduser and assigns it as "VERIFICATION" variable
			qwertyuiop = "1234567890qwertyuiopasdfghjklzxcvbnm" # dynamic/hardcoded string for cross referencing enduser input.

			if VERIFICATION.lower() == qwertyuiop: # decapitalize all characters in VERIFICATION string (end user input) and `IF` it's exactly equal to `qwertyuiop` string...
				#print "VERIFIED"
				self.destroy() #.... allow the end user access to initial window by "destroying" keyboard tester window. Similar to the exit() command but for individual child/GUI windows.

			else:
				#print "TRY AGAIN!!"
				self.destroy() #... destroy current keyboard tester window (for visual notification)
				KeyboardTester() #.... and restart the entire function.

			BUTTON = tk.Button(self, width=50, height=2, text="Click or Press Enter", command=lambda: ButtonPressVerification()) # button for Enduser to "submit" characters to `VERIFICATION` variable
			BUTTON.grid(row=3, column=0, columnspan=3) # creates this button and assigns to grid placement

			self.bind('<Return>',(lambda event: ButtonPressVerification(INPUTRETURN.get()))) # connect/BIND the "Return" (aka enter) key with the previously mentioned button.

			Center(self)
			self.resizable(0,0)
			self.title("KeyBoard Testing")
			self.mainloop()

class StartPage(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)

		def AllHardwareTesterButtons():
			BATTERY = '"%CD%/ProgFiles/batteryinfoview/batteryinfoview.exe"'
			CAMERA = '"%CD%/ProgFiles/commandcam/CommandCam.exe" && "%CD%/ProgFiles/commandcam/.'
			LEFTSPKR = '"%CD%/ProgFiles/cmdmp3/cmdmp3.exe" "%CD%/ProgFiles/cmdmp3/Left.mp3"'
			RIGHTSPKR = '"%CD%/ProgFiles/cmdmp3/cmdmp3.exe" "%CD%/ProgFiles/cmdmp3/Right.mp3"'
			HDDSMART = '"%CD%/ProgFiles/crystaldiskinfo/DiskInfo.exe"'
			IMPORTWIFI = 'cd "%CD%/ProgFiles/wirelesskeyview" && WirelessKeyView.exe /import "%CD%/ProgFiles/wirelesskeyview/WiFiKeysBackup.txt"'
			ACTIVATION = 'slmgr /xpr'

			HardwareTestingCommands = [IMPORTWIFI, LEFTSPKR, RIGHTSPKR, ACTIVATION, HDDSMART, BATTERY, CAMERA]
		
			for Command in HardwareTestingCommands:
				subprocess.call(Command, shell=True)
			KeyboardTester()

		def AllAutOptimizerButtons():
			TASKMGR = 'taskmgr /0 /startup'
			WINDIRSTAT = '"%CD%/ProgFiles/WinDirStat/WinDirStatPortable.exe"'
			BULKUNINST = '"%CD%/ProgFiles/iobituninstaller/IObitUninstallerPortable.exe"'
			CCLEANER = '"%CD%/ProgFiles/ccleaner/CCleaner64.exe"'
			#CLEANMGR = 'cleanmgr /sageset99 && cleanmgr /sagerun99'
			#SERVICESANDTASKS = 'start /w services.msc && taskschd.msc'

			AutOptCommands = [TASKMGR, WINDIRSTAT, BULKUNINST, CCLEANER]
		
			for Command in AutOptCommands:
				subprocess.call(Command, shell=True)

		def RunDiagnostics():
			MALWAREBYTES = '"%CD%/ProgFiles/Malwarebytes.cameyo.exe" -SafeMode'
			SUPERANTISPYWARE = '"%CD%/ProgFiles/superantispyware/superantispyware.exe"'
			TDSSKILLER = '"%CD%/ProgFiles/TDSSKiller.exe" -accepteula'
			CRYSTALDISKINFO = '"%CD%/ProgFiles/crystaldiskinfo/DiskInfo.exe"'

			AutoDiagCommands = [TDSSKILLER, SUPERANTISPYWARE, MALWAREBYTES, CRYSTALDISKINFO]

			for Command in AutoDiagCommands:
				subprocess.call(Command, shell=True)

		def FileTransfer():
			time.sleep(0.5)

			win32api.keybd_event(win32con.VK_LWIN, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
			SendKeys.SendKeys("e")
			win32api.keybd_event(win32con.VK_LWIN, 0, win32con.KEYEVENTF_KEYUP, 0)

			time.sleep(1)

			win32api.keybd_event(win32con.VK_LWIN, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
			SendKeys.SendKeys("{LEFT}")
			win32api.keybd_event(win32con.VK_LWIN, 0, win32con.KEYEVENTF_KEYUP, 0)

			subprocess.Popen('explorer %USERPROFILE%', shell=True)

			time.sleep(1)

			win32api.keybd_event(win32con.VK_LWIN, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
			SendKeys.SendKeys("{RIGHT}")
			win32api.keybd_event(win32con.VK_LWIN, 0, win32con.KEYEVENTF_KEYUP, 0)

		def BackupReinstall():
			IMPORTWIFI = 'cd "%CD%/ProgFiles/wirelesskeyview" && WirelessKeyView.exe /import "%CD%/ProgFiles/wirelesskeyview/WiFiKeysBackup.txt"'
			DOUBLEDRIVER = '"%CD%/ProgFiles/doubledriver/dd.exe"'

			BURICommands = [IMPORTWIFI, DOUBLEDRIVER]

			FileTransfer()
			for Command in BURICommands:
				subprocess.call(Command, shell=True)

		MainButton0 = tk.Button(self, text='Diagnostics', width=34, height=5, command=lambda: RunDiagnostics())
		MainButton1 = tk.Button(self, text='Optimizer', width=34, height=5, command=lambda: AllAutOptimizerButtons())
		MainButton2 = tk.Button(self, text='Backup/Reinstall', width=34, height=5, command=lambda: BackupReinstall())

		MainButton0.grid(row=0, column=1, columnspan=2, padx=(10,10), pady=5)
		MainButton1.grid(row=0, column=3, columnspan=2, padx=(10,10), pady=5)
		MainButton2.grid(row=0, column=5, columnspan=2, padx=(10,10), pady=5)

		LineCanvas = tk.Canvas(height=1, width=785, bg="gray")
		LineCanvas.grid(row=1, column=1, columnspan=6, pady=5)

		self.ButtonImage0 = ImageTk.PhotoImage(file=icondirectory + 'MalwareBytes.png')
		self.ButtonImage1 = ImageTk.PhotoImage(file=icondirectory + 'TweakingsWindowsRepair.png')
		self.ButtonImage2 = ImageTk.PhotoImage(file=icondirectory + 'CrystalDiskInfo.png')

		self.ButtonImage3 = ImageTk.PhotoImage(file=icondirectory + 'SuperAntiSpyware.png')
		self.ButtonImage4 = ImageTk.PhotoImage(file=icondirectory + 'TDSSKiller.png')
		self.ButtonImage5 = ImageTk.PhotoImage(file=icondirectory + 'Folding@Home.png')

		self.ButtonImage6 = ImageTk.PhotoImage(file=icondirectory + 'TaskManager.png')
		self.ButtonImage7 = ImageTk.PhotoImage(file=icondirectory + 'TaskScheduler.png')
		self.ButtonImage8 = ImageTk.PhotoImage(file=icondirectory + 'Services.png')

		self.ButtonImage9 = ImageTk.PhotoImage(file=icondirectory + 'Ccleaner.png')
		self.ButtonImage10 = ImageTk.PhotoImage(file=icondirectory + 'WinDirStat.png')
		self.ButtonImage11 = ImageTk.PhotoImage(file=icondirectory + 'iobituninstaller.png')

		self.ButtonImage12 = ImageTk.PhotoImage(file=icondirectory + 'Hardware.png')
		self.ButtonImage13 = ImageTk.PhotoImage(file=icondirectory + 'Chocolatey.png')
		self.ButtonImage14 = ImageTk.PhotoImage(file=icondirectory + 'DeviceManager.png')

		self.ButtonImage15 = ImageTk.PhotoImage(file=icondirectory + 'Transfer.png')
		self.ButtonImage16 = ImageTk.PhotoImage(file=icondirectory + 'DoubleDriver.png')
		self.WifiTopImage17 = ImageTk.PhotoImage(file=icondirectory + 'wifibottomhalfz.png')
		self.WifiBottomImage18 = ImageTk.PhotoImage(file=icondirectory + 'wifitophalfz.png')

		StartPageButton0 = tk.Button(self, image=self.ButtonImage0, text='MalwareBytes', compound='bottom', command=lambda: subprocess.Popen('"%CD%/ProgFiles/Malwarebytes.cameyo.exe" -SafeMode', shell=True))
		StartPageButton1 = tk.Button(self, image=self.ButtonImage1, text='AIO Win Repair', compound='bottom', command=lambda: subprocess.Popen('"%CD%/ProgFiles/tweaking/Repair_Windows.exe"', shell=True))
		StartPageButton2 = tk.Button(self, image=self.ButtonImage2, text='CrystalDisk Info', compound='bottom', command=lambda: subprocess.Popen('"%CD%/ProgFiles/crystaldiskinfo/DiskInfo.exe"', shell=True))

		StartPageButton3 = tk.Button(self, image=self.ButtonImage3, text='SuperAnti Spyware', compound='bottom', command=lambda: subprocess.Popen('"%CD%/ProgFiles/superantispyware/superantispyware.exe"', shell=True))
		StartPageButton4 = tk.Button(self, image=self.ButtonImage4, text='TDSS Killer', compound='bottom', command=lambda: subprocess.Popen('"%CD%/ProgFiles/TDSSKiller.exe" -accepteula', shell=True))
		StartPageButton5 = tk.Button(self, image=self.ButtonImage5, text='Stress Tester', compound='bottom', command=lambda: subprocess.Popen('"%PROGRAMFILES(X86)%/Google/Chrome/Application/chrome.exe" http://folding.stanford.edu/nacl/', shell=True))

		StartPageButton6 = tk.Button(self, image=self.ButtonImage6, text='Startup Programs', compound='bottom', command=lambda: subprocess.Popen('taskmgr /0 /startup', shell=True))
		StartPageButton7 = tk.Button(self, image=self.ButtonImage7, text='Scheduled Tasks', compound='bottom', command=lambda: subprocess.Popen('"taskschd.msc"', shell=True))
		StartPageButton8 = tk.Button(self, image=self.ButtonImage8, text='Services', compound='bottom', command=lambda: subprocess.Popen('"services.msc"', shell=True))

		StartPageButton9 = tk.Button(self, image=self.ButtonImage9, text='Ccleaner', compound='bottom', command=lambda: subprocess.Popen('"%CD%/ProgFiles/ccleaner/CCleaner64.exe"', shell=True))
		StartPageButton10 = tk.Button(self, image=self.ButtonImage10, text='WinDirStat', compound='bottom', command=lambda: subprocess.Popen('"%CD%/ProgFiles/WinDirStat/WinDirStatPortable.exe"', shell=True))
		StartPageButton11 = tk.Button(self, image=self.ButtonImage11, text='Bulk Uninstaller', compound='bottom', command=lambda: subprocess.Popen('"%CD%/ProgFiles/iobituninstaller/IObitUninstallerPortable.exe"', shell=True))

		StartPageButton12 = tk.Button(self, image=self.ButtonImage12, text='Hardware Tester', compound='bottom', command=lambda: AllHardwareTesterButtons())
		StartPageButton13 = tk.Button(self, image=self.ButtonImage13, text='Chocolatey', compound='bottom', command=lambda: os.system('start %CD%/ProgFiles/FullChocoInstall.bat'))
		StartPageButton14 = tk.Button(self, image=self.ButtonImage14, text='Device Manager', compound='bottom', command=lambda: subprocess.Popen('"devmgmt.msc"', shell=True))

		StartPageButton15 = tk.Button(self, image=self.ButtonImage15, text='Backup User Folder', compound='bottom', command=lambda: FileTransfer())
		StartPageButton16 = tk.Button(self, image=self.ButtonImage16, text='Backup Drivers', compound='bottom', command=lambda: subprocess.Popen('"%CD%/ProgFiles/doubledriver/dd.exe"', shell=True))
		StartPageButton17 = tk.Button(self, image=self.WifiTopImage17, text='WiFi Import', compound='top', command=lambda: subprocess.Popen('cd "%CD%/ProgFiles/wirelesskeyview" && WirelessKeyView.exe /import "%CD%/ProgFiles/wirelesskeyview/WiFiKeysBackup.txt"', shell=True))
		StartPageButton18 = tk.Button(self, image=self.WifiBottomImage18, text='WiFi Export', compound='bottom', command=lambda: subprocess.Popen('cd "%CD%/ProgFiles/wirelesskeyview" && WirelessKeyView.exe /export "%CD%/ProgFiles/wirelesskeyview/WiFiKeysBackup.txt"', shell=True))

		StartPageButton0.grid(row=2, column=1, padx=5, pady=5)
		StartPageButton1.grid(row=3, column=1, padx=5, pady=5)
		StartPageButton2.grid(row=4, column=1, padx=5, pady=5)

		StartPageButton3.grid(row=2, column=2, padx=5, pady=5)
		StartPageButton4.grid(row=3, column=2, padx=5, pady=5)
		StartPageButton5.grid(row=4, column=2, padx=5, pady=5)

		StartPageButton6.grid(row=2, column=3, padx=5, pady=5)
		StartPageButton7.grid(row=3, column=3, padx=5, pady=5)
		StartPageButton8.grid(row=4, column=3, padx=5, pady=5)

		StartPageButton9.grid(row=2, column=4, padx=5, pady=5)
		StartPageButton10.grid(row=3, column=4, padx=5, pady=5)
		StartPageButton11.grid(row=4, column=4, padx=5, pady=5)

		StartPageButton12.grid(row=2, column=5, padx=5, pady=5)
		StartPageButton13.grid(row=3, column=5, padx=5, pady=5)
		StartPageButton14.grid(row=4, column=5, padx=5, pady=5)

		StartPageButton15.grid(row=2, column=6, padx=5, pady=5)
		StartPageButton16.grid(row=3, column=6, padx=5, pady=5)
		StartPageButton17.grid(row=4, column=6, padx=5, pady=(60,5))
		StartPageButton18.grid(row=4, column=6, padx=5, pady=(5,60))

if __name__ == "__main__":
	app = StartPage()
	app.resizable(0,0)
	Center(app)
	app.title("B.L.D.Z.R.")
	app.iconbitmap(icondirectory + 'ybldzr.ico')
	app.mainloop()
