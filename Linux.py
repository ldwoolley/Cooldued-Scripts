import subprocess, os

def users():
    users_actual = []
    user_passwd = []
    
    #list of default system users for Ubuntu
    users_authorized = ["root", "daemon", "bin", "sys", "sync", "games", "man", "lp", "mail", "news", "uucp", "proxy", "www-data", "backup", "list", "irc", "gnats", "nobody", "systemd-timesync", "systemd-network", "systemd-resolve", "systemd-bus-proxy", "syslog", "_apt", "messagebus", "uuidd", "lightdm", "whoopsie", "avahi-autoipd", "avahi", "dnsmasq", "colord", "speech-dispatcher", "hplip", "kernoops", "pulse", "rtkit", "saned", "usbmux", "guest-lncgoz"]
    
    #collects the list of users from the computer
    users_actual = subprocess.Popen(["cut -d: -f1 /etc/passwd"], shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8').splitlines()

    #collects the list of users that are suppost to be on the system
    users_total = (input('How many users do you have: ')
    for i in range(0, int(users_total)):

        user_name = .lower(input('What is the name of user {}: '.format(i)))
        users_authorized.append(user_name)
        users_passwd.append(user_name)
        
    #adds users missing from the system
    for user in users_authorized:
        
        add_user = 'q'
        while add_user != 'y' or 'n':
            
            if user not in users_actual:
                add_user = .lower(input('Would you like to add the user {} becuase they are not currently on this system (y, n): '.format(user)))
    
                if add_user == 'y':
                    subprocess.call('adduser {}'.format(user))
    #removes users that are not suppost to be on the system
    for user in users_actual:
        
        remove_user = 'q'
        while remove_user != 'y' or 'n':
            
            if user not in users_authorized:
                remove_user = .lower(input('Would you like to remove the user {} because they are currently on this system even though they should not (y, n): '.format(user)))
    
                if remove_user == 'y':
                    subprocess.call('deluser {}'.format(user))

def passwd():
    password = input('What password would you like to change all of your users to: ')
    
    for user in user_passwd:
        
        change_passwd = 'q'
        
        while change_password != 'y' or 'n':
            change_passwd = input('Would you like to change the password of {} to {} (y, n)'.format(user, password))
            if change_passwd == 'y':
                os.system('passwd {} --stdin {}'.format(user, password))
            elif change_passwd == 'n':
                print('Okay')
            else:
                print('Could you please follow direction and answer with a y or n')
#def groups():
    
def bad_programs():
    programs = ['aircrack-ng', 'apache', 'brutus', 'cain', 'chkrootkit', 'crack', 'ettercap', 'ftp', 'hping', 'hydra', 'John', 'kismet', 'maltego', 'metasploit', 'nessus', 'netcat', 'nikto', 'mysql', 'nmap', 'ophcrack', 'owasp-zed', 'postgresql', 'rainbow-crack', 'samba', 'snort', 'tcpdump', 'telnet', 'thc-hydra', 'winzapper', 'wireshark']
    
    
#def media_files():
options = '''
Please chose one of the following

1. Configure your users
2. Configure your groups (coming soon)
3. Find bad programs (coming soon)
4. Find unauthorized media files (coming soon)

'''
user_choice = 2
while user_choice != 1:
    
    user_choice = int(input('{}'.format(options)))

    if user_choice == 1:
        users()
    else:
        print('What part of coming soon do you not understand?')
        print('Lets try this again, maybe we should listen to directions this time.')
    
#def media_files():
mistake = '''
Sorry, this featur is not available yet
Please pick an option that is availible
'''

options = '''
Please chose one of the following

1. Configure your users
2. Change user passwords
3. Configure your groups (coming soon)
4. Find bad programs (coming soon)
5. Find unauthorized media files (coming soon)
6. Exit

'''
user_choice = 2
while user_choice != 1 or 2:
    
    user_choice = int(input('{}'.format(options)))

    if user_choice == 1:
        users()
        options = options.replace('1. Configure your users', '')
        
    elif user_choice == 2:
        passwd()
        options = options.replace('2. Change user passwords', '')
        
    elif user_choice == 3:
        print(mistake)
        options = options.replace('3. Configure your groups (coming soon)', '')
        
    elif user_choice == 4:
        print(mistake)
        options = options.replace('4. Find bad programs (coming soon)', '')
        
    elif user_choice == 5:
        print(mistake)
        options = options.replace('5. Find unauthorized media files (coming soon)', '')
        
    elif user_choice == 6:
        break
        
    else:
        print(mistake)
