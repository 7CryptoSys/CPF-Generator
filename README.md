<div align="center">

[<img src="https://i0.wp.com/blog.meuid.com.br/wp-content/uploads/2020/12/CPF-irregular_-Saiba-como-resolver-1.jpg?fit=2340%2C1030&ssl=1" width="750" />](https://i0.wp.com/blog.meuid.com.br/wp-content/uploads/2020/12/CPF-irregular_-Saiba-como-resolver-1.jpg?fit=2340%2C1030&ssl=1)

</div>

### Gerador de CPF

Tendo sido usado defs, e manipulação de texto para colocar num formato de CPF e de mais alguns truques para fazer uma geração de numeros com o padrão da vida real usando funções básicas do random como sample e join, para conseguirmos editar ele, apenas precisamos manipulação de texto além de for, não é nada muito avançado, mas é o básico que funciona, se quiser organizar o cpf bonitinho faça igual ao exemplo 

 ### Exemplo:

   ```py
 cpf = cpf[0:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" str(calculo_digitoX(cpf)) + str(calculo_digitoY(cpf))

