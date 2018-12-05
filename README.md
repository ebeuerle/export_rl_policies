# RedLock policy export 

Version: *1.0*
Author: *Eddie Beuerlein*

### Summary
This script will create a csv file that contains the policy data from the RedLock UI.

### Requirements and Dependencies

1. Python 2.7.10 or newer

2. OpenSSL 1.0.2 or newer

(if using on Mac OS, additional items may be nessessary.)

3. Pip

```sudo easy_install pip```

4. Requests (Python library)

```sudo pip install requests```

5. YAML (Python library)

```sudo pip install pyyaml```

### Configuration

1. Navigate to *export_policies_csv/config/configs.yml*

2. Fill out your RedLock username, password, and customer name - if you are the only customer in your account then leave this blank.

### Run

```
python runner.py

```
