#!/usr/bin/node

const argv = process.argv[2]; // Retrieve the first argument
const num = parseInt(argv); // Convert the argument to an integer

if (isNaN(num)) {
	console.log('Not a number');
} else {
	console.log(`My number: ${num}`);
}
