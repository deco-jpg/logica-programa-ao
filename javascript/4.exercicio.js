const readline = require ('readline-sync')

Negativos = [];
Positivos = [];
soma = 0
for (let i = 1; i <= 5; i++){
    num = readline.questionFloat("Digite um numero: ");
    if (num > 0 ){
        soma += num
        Positivos.push(num)
    } else{
        Negativos.push (num)
}}
console.log (`Quantidade de negativos: ${Negativos.length}`)
console.log (`Soma de positivos: ${soma}`)
