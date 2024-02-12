#!/usr/bin/node

const factorial = n => isNaN(n) || n < 2 ? 1 : n * factorial(n - 1);

console.log(factorial(process.argv[2]));
