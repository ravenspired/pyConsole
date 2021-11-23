


from console_resources import *
# Import the resources needed for the console to function





consoleSetup(False, True, True, True) 
#Set up the console. Each boolean controls whether an aspect of the console
#should be displayed. The syntax is as follows: 
# consoleSetup(display_info, display_ok, display_warning, display_error)
#A few notes: The values passed should all be integers.
#Failing to setup the console will have it default to display everything.



console("a test failed", "warning")
console("a test passed", "ok")
console("a test infoed", "info")
console("fatal error", "error")
#Print the console message. The syntax is as follows:
# console("MESSAGE", "STATUS_CODE")
#Supported messages include strings and integers. 
#Supported status codes include "warning", "ok", "error", and "info"
#If the status code is not recognized it defaults to an INFO message.