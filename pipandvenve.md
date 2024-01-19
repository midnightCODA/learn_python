# PIP
- pip in long form is preffered installer program

on windows we would use 
py -m pip install requests


which corresponds to 
python3 -m pip install requests

QN. what is the difference between `python3 -m pip install requests` and `pip install requests` 

*** the installed packages are installed globally thus we can see them by teh command ***
`py -m pip list`

Since pip installs modules globally, what if different projects needs different modules versions
we can get around that by using *** virtual environments ***  


### How to create a virtual environment


`py -m venv .venv`

---------- then we activate it by -------------

`source .venv/Scripts/activate`


and thus we can deactivate it by 

`deactivate`

*** a super cool command is ***

py -m pip freeze > requirements.txt



also is important to note that in the `.env` file its not needed to pass "" marks
i.e `API_KEY=CDCSDBCJDSCBJDBCJBSJCBJSDBJCBSDJKCBJKSDB` is fine all alone no need to
use "" marks