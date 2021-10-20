# G-Auth
## _Get your Google Authenticator 2FA code in linux with ease_

With G-Auth you can get the Google Authenticator code in linux by simply running a python file.

## How to Use
Clone the repository
```sh
git clone 
```
Install the requirements using pip
```sh
cd gauth
pip -r requirements.txt
```
Change the value of secret parameter in [auth.py](https://github.com/auth.py) with your token value.

```sh
import time
import sys

'''Replace XXXX with your token value'''
secret = b'XXXXXXXXXXXXXXXX' 
```
Save the file and run [auth.py](https://github.com/auth.py)
```sh
python auth.py
```


## License

MIT

**Free Software, Hell Yeah!**

