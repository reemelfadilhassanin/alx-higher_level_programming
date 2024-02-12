#!/usr/bin/node
// print args

let x;
const args = process.argv.length;
if (args < 3) {
	x = 'No argument';
} else if (args === 3) {
	x = 'Argument found';
} else {
	x = 'Arguments found';
}
console.log(x);
