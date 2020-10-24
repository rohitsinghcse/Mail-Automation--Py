# Mail-Automation--Py
Mail automation using Python

This app reads sender email ID from sender.txt file and sent to all mail id's given in receiver.txt.
If you wish you can add more senders and receivers in the text files.

Sender.txt consists of username and password separated by a comma.

Receiver.txt consists of list of receivers mail id.

.exe file location - dist folder

Generate new .exe from py file

Install the library pyinstaller.
Type below command in the command prompt.

    pip install pyinstaller

Run below command in PowerShell
pyinstaller --onefile -w '.\MailAutomation.py'

