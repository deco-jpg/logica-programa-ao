// solicite 3 notas e calcule a média.
// npm install readline-sync
const readline = require ('readline-sync')
listadenotas = []
for (let i = 1; i <= 3; i++) {
    nota = readline.questionFloat(`Digite a ${i}° nota: `)
    listadenotas.push (nota)

}

console.log ("\nSoma das notas")
soma = listadenotas.reduce((soma, total) => soma + total , 0)
console.log (soma)

console.log ("\nQuantidade de notas: ")
quantidadenotas = listadenotas.length
console.log (quantidadenotas)

media = soma / quantidadenotas
console.log (`Sua média é: ${media}`)