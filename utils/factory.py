from datetime import datetime
from random import randint

from faker import Faker

arquivo = open("sqlsInserts.txt", "a")
sqls = list()

def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker(locale='pt-br')
# print(signature(fake.random_number))


for i in range(4, 210):
    id = i
    data_criacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    nome = fake.first_name()
    sobrenome = fake.last_name()
    telefone = fake.phone_number()
    email = nome.replace(' ', '').lower() + telefone[-4:-1] + '@email.com'
    descricao = fake.sentence()
    categoria_id = randint(1, 3)

    valores = (f"INSERT INTO contatos_contato (id, nome, sobrenome, telefone, email, data_criacao, descricao, categoria_id) "
          f"VALUES ({id}, '{nome}', '{sobrenome}', '{telefone}', '{email}', '{data_criacao}', '{descricao}', {categoria_id});")

    sqls.append(str(valores))
 
arquivo.writelines(sqls)
arquivo.close()
print(f"Feito, foram inseridos {len(sqls)} no arquivo txt!")