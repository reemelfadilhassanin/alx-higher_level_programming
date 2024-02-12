#!/usr/bin/node

console.log(isNaN(Math.floor(Number(process.argv[2]))) ? 'Not a number' : `My number: ${Math.floor(Number(process.argv[2]))}`);
