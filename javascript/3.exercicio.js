const readline = require ('readline-sync')


listnumber = []

for (let i = 1; i <= 6; i++){
    let num = readline.questionInt("Digite um numero: ")
    listnumber.push(num)
}
// const pares = listnumber.filter(n => n % 2 == 0)
// console.log(pares)
// const impares = listnumber.filter (n => n % 2 == 1)
const pares = listnumber.filter(n => n % 2 == 0)
const impares = listnumber.filter(n => n % 2 !== 0)

console.log (`Numeros pares: ${pares}`)
console.log (`Numeros impares: ${impares}`)
console.log(`\nQuantidade de pares: ${pares.length} `)
console.log(`Quantidade de impares: ${impares.length} `)
