#!/usr/bin/node
const s = process.argv[2];
if (isNaN(s)) {
	console.log('Missing size');
} else {
	for (let x = 0; x < s; x++) {
		console.log('X'.repeat(s));
	}
}
