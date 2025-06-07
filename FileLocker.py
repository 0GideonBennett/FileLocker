import subprocess # This allows us run commands to the cli from are python script
#We are going to use icacls Thihs is a windows cli tool that lets us edit file permissions

#Scipt: Allow one to select a file within the current dir  and then change the security permsison to  prevent a specified user from writing/editing the file



#Get user input

fileName = input("Enter the name of the file you wish to lock: ")
user = input("Enter the name of the user you wish to restrict: ")

#Use subprocess to run the icacls command ( allow use to restrict files
subprocess.run(["icacls", f"{fileName}", "/deny", f"{user}:W"])

print(f" {user} now can't write/modify {fileName}")    
rerun = input("Would you like you like to run the script again?(type y or n):") 

if rerun == "y":
    subprocess.run(["python","FileLocker.py"])
elif rerun== "n":
    print("Have a great day!")

#V2:
# Make error handling for if the file does not exists
# Restrict another user for the same file that was just locked before askign to rerun

     