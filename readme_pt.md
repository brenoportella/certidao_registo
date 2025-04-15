# VERIFICAÇÃO DE PRESTAÇÃO DE CONTAS (CERTIDÃO PERMANENTE)

### Requisitos
Antes de começar, certifique-se de que tem o Python e o pip instalados no seu sistema.
- Pode verificar executando:

 ```bash
python --version
pip --version
```
ou, em sistemas Linux:

 ```bash
python3 --version
pip3 --version
```

### Para instalar (WINDOWS):

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### Para instalar (LINUX):

```bash
python3 -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python3 main.py
```

### Ficheiro de entrada
Crie um ficheiro .xlsx. Na célula A1, insira o termo "code". Na célula abaixo (A2), insira a sua lista de códigos.
Os códigos devem seguir as seguintes regras:

    -Um código por linha;
    -O código DEVE CONTER 14 dígitos (0000-0000-0000);

Antes de usar o programa, indique o caminho relativo (em relação ao main.py) para o seu ficheiro .xlsx na variável INPUT_EXCEL em src/defines.py.

### Versão em inglês
Se a "Certidão de Registo" estiver em inglês, o programa apenas notificará sobre o código na versão inglesa, mas não irá recolher as informações sobre a empresa.
Nesse caso, deverá verificar essas informações por conta própria.
