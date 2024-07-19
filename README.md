<div align="center">

[<img src="https://i0.wp.com/blog.meuid.com.br/wp-content/uploads/2020/12/CPF-irregular_-Saiba-como-resolver-1.jpg?fit=2340%2C1030&ssl=1" width="750" />](https://i0.wp.com/blog.meuid.com.br/wp-content/uploads/2020/12/CPF-irregular_-Saiba-como-resolver-1.jpg?fit=2340%2C1030&ssl=1)

</div>

### Gerador de CPF/Verificador:

Tendo sido usado defs, e manipulação de texto para colocar num formato de CPF e de mais alguns truques para fazer uma geração de numeros com o padrão da vida real usando funções básicas do random como sample e join, para conseguirmos editar ele, apenas precisamos manipulação de texto.

 ### Exemplo:

   ```py
cpf = cpf[0:3] + "." + cpf [2:5] + "." + cpf [5:8] + "-" + "".join(random.sample(numero, 2))
#Aqui vemos que a cada 3 caracteres, eu corto e adiciono um "." para separar e ficar igual
#a vida real, e no final como os numeros eram limitados, eu fiz criar 2 numeros random. 


