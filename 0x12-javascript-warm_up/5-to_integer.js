#!/usr/bin/node
const argv = process.argv[2];
const num = parseInt(argv);
if (isNaN(num)) {
	console.log('Not a number');
} else {
	console.log(`My number: ${num}`);
}
