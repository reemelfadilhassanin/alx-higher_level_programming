#!/usr/bin/node

let x;
const argsC = process.argv.length;
if (argsC === 2) {
	x = 'No argument';
} else if (argsC === 3) {
	x = 'Argument found';
} else {
	x = 'Arguments found';
}
console.log(x);
