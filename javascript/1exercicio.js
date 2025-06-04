const notas = [7.5, 8.0, 6.3]

const soma = notas.reduce ((soma, total) => soma + total, 0)
const media = soma / notas.length;
console.log (`Soma das notas: ${soma}`)
console.log (`A sua média é: ${media.toFixed(2)}`) // Mostra com 2 casas decimais

