#!/usr/bin/node
let argco;
if (process.argv.length < 3) {
	argco = 'No argument';
} else if (process.argv.length === 3) {
	argco = 'Argument found';
} else {
	argco = 'Arguments found';
}
console.log(argco);
