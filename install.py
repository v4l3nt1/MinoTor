import os
choice = input('[+] to install MinoTor, press (Y). To uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 minotor.py')
    run('mkdir /usr/share/minotor')
    run('cp minotor.py /usr/share/minotor/minotor.py')

    cmnd=' #! /bin/sh \n exec python3 /usr/share/minotor/minotor.py "$@"'
    with open('/usr/bin/minotor','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/minotor & chmod +x /usr/share/minotor/minotor.py')
    print('''\n\nCongratulation ! MinoTor Ip Rotator is installed successfully \nfrom now just type \x1b[6;30;42mminotor\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/minotor ')
    run('rm /usr/bin/minotor ')
    print('[!] MinoTor Ip Rotator has been removed successfully')
