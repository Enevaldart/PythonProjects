#import subprocess
import subprocess

#Getting metadata
meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

#creating a list of profiles
profiles = [i.split(":")[1][1:-1] for i in meta_data if 'All User Profile' in i]

#printing the heading
print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print("---------------------------------------------")

#traverse the data
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(':')[1][1:-1] for b in results if 'Key Content' in b]

        #if there is password it will print the password
    try:
        print("{:<30}| {:<}".format(i, results[0]))

        #else it will print black in front of password
    except IndexError:
        print("{:<30}| {:<}".format(i, ""))

    #called when this process get failed
    except subprocess.CalledProcessError:
        print("Encoding error occurred")
        