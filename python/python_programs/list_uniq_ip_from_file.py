import os
import re

# clearing the terminal
os.system('cls' if os.name == 'nt' else 'clear')


# creating a function to read the logfile.
def get_ip_from_file_and_add_to_set(logfile):

    ip_address_set = set()

    ip_regex = r"(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"

    with open(logfile,'r') as logfile_handler:
        for line in logfile_handler:
            ips = re.findall(ip_regex, line)
            ip_address_set.update(ips)

    return ip_address_set
    



# taking user input for a file with default logfile options:
logfile = input("Please do enter the valid logfile path (or enter for the default value of 'testing_log_file.log' on the same dir location.): ")
# TODO: file error handle
if not logfile:
    logfile = "testing_log_file.log"



print(f"\n\033[31mEnterd log file: {logfile}.\033[0m\n")

# adding the return to a variable and printing the output
ipaddress = get_ip_from_file_and_add_to_set(logfile)
print(ipaddress)

