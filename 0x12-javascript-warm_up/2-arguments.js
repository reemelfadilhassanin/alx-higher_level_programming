#!/usr/bin/node

const x = process.argv.length;
const message = x === 2 ? 'No argument' : x === 3 ? 'Argument found' : 'Arguments found';

console.log(message);
