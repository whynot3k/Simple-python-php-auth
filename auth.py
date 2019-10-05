
def auth():
    import requests
    import subprocess
    import pendulum
    import hashlib
    current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    print("HWID: " + current_machine_id)
    AUTH = input("Please enter your auth key: ")
    salt = ""
    getauth1 = requests.get(url="https://crsdgadnbfdtgnpasdrgtcsdrghh.000webhostapp.com/auth.php?AUTH=" + AUTH + "&HWID=" + current_machine_id)
    # this is  a example url ^ put your own in for where you host your php script
    today = str(pendulum.now('Europe/Paris').to_date_string())
    ha = today + AUTH + today + current_machine_id + salt

    hashed = hashlib.md5(ha.encode())

    # print(hashed.hexdigest())
    # print(getauth1.text)
    # print(today)
    if hashed.hexdigest() == getauth1.text:
        input("You are Authed.\npress enter to continue")
    else:
        if "HWID" in getauth1.text:
            print("INVALID HWID")
            input("PRESS ENTER TO CLOSE")
        else:
            print("YOU ARE NOT AUTHED")
            input("PRESS ENTER TO CLOSE")
        quit()