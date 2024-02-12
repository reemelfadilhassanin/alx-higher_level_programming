#!/usr/bin/node
const argsC = process.argv.length;

if (argsC === 2) {
	console.log("No argument");
} else if (argsC === 3) {
	console.log("Argument found");
} else {
	console.log("Arguments found");
}
