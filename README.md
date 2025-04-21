# VERIFY CERTIDÃO DE REGISTO (PORTUGAL)

 🇵🇹 [Portuguese version](https://github.com/brenoportella/certidao_registo/blob/main/readme_pt.md)
### Requirements
Before starting, make sure you have Python and pip installed on your system.
- You can check by running:

 ```bash
python --version
pip --version
```
or, on Linux:

 ```bash
python3 --version
pip3 --version
```

### To install (WINDOWS):

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### To Install (LINUX):

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

### Input File
Create a xlsx file. In the cell A1 insert the term "code". In the cell bellow (A2), insert your list of codes.
The codes must follow the following rules:

    -One code per row;
    -The code MUST HAVE 14 digits (0000-0000-0000);

Before using the program, please indicate the relative path (relative to main.py) to your codes file (.xlsx) on the INPUT_EXCEL declaration in src/defines.py

### English Version
If the "Certidão de Registo" is in english, the program only will notificate about the code in english version, but will not collect the information about the company. You should check it by yourself.
