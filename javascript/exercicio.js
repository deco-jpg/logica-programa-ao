// Criando um vetor
// .map() -> Cria um novo array transformando cada item com a função fornecida.
// .filter() -> Cria um novo array apenas com os itens que passam em uma condição (retornam true).
// .reduce() -> Reduz o array a um único valor, acumulando os resultados com base em uma função.

const listaDeNumeros = [1,2,3,4]
console.log ('Listando todos os numeros da lista')
console.log (listaDeNumeros)

console.log ('\nMultiplicando valores por 2: ')
const dobrados = listaDeNumeros.map (n=> n * 2)
console.log(dobrados)

console.log ('\nFiltrando elementos pares')
const pares = listaDeNumeros.filter (n => n % 2 == 0)
console.log (pares) 

console.log ('\Somando todos os numeros da lista: ')
const soma = listaDeNumeros.reduce ((soma, total) => soma + total, 0)
console.log (soma)