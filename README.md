# joseki-pass

## Description
The purpose of this project is to create a basic password list.
A word list of terms needs to have already been created.
This program will then create a list of possible passwords from it

---
## How to Execute
**Setting up the script**
```bash
git clone https://gitlab.com/eric-keith/joseki-pass.git
cd joseki-pass
chmod u+x joseki-pass
```

**A look at the help page**
```bash
python3 joseki-pass -h
./joseki-pass -h
```
![Help Page Image](./src/images/help_page.png "Help Page")

**Executing the script**
```bash
./joseki-pass -i <termfile.txt>
```
---
## To Do
- [x] Add a time tracker function to display how long the command took to complete
- [x] Add Command Line Arguments
    - [x] Choose Output filename
    - [x] Help Page
- [x] Add possible rich tracker
- [ ] Add Threading to make process faster
