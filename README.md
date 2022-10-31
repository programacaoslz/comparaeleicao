# Comparador/Simulador Algoritmo TSE x Interpretação Artigo 109 - Inciso I
Solicitação do Deputado Hildo Rocha (MA)

Antes de instalar o Pyenv e o Python 3.9.7:
```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev git python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx swig libsasl2-dev python-dev libldap2-dev
```

Após
```
pip install -r requirements.txt
```

Crie a base
```
python manage.py migrate
```

Crie um superusuario
```
python manage.py createsuperuser
```

Para importar os dados do TSE e gerar as simulações basta rodar os comandos abaixo na linha de comando em sequência:
```
python manage.py importa_csv_nominal
python manage.py importa_csv_legenda
python manage.py totaliza_partidos
python manage.py gera_quocientes
python manage.py classifica_eleitos_algoritmo_tse
python manage.py classifica_eleitos_algoritmo_corrigido
```

Para rodar a aplicação basta rodar
```
python manage.py runserver
```

Acesse no navegador em 
```
http://127.0.0.1:8000/admin e logue com o usuário criado
```