print('============Tipos Permitidos=============')
print('')

dados = input('Digite o valor: ')

print('O tipo permitdos desse valor é: ', type(dados))
print('O tipo permitdos desse é espaço : ', dados.isspace())
print('O tipo permitdos desse valor é numerico: ', dados.isnumeric())
print('O tipo permitdos desse valor é Spring: ', dados.isalpha())
print('O tipo permitdos desse valor é alfanumerico: ', dados.isalnum())
print('O tipo permitdos desse valor é maiusculas: ', dados.isupper())
print('O tipo permitdos desse valor é minusculas: ', dados.islower())