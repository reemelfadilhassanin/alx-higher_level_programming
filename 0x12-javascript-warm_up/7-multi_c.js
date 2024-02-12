#!/usr/bin/node
let l = parseInt(process.argv[2]);
if (!isNaN(l)) {
	for (l--; l >= 0; l--) {
		console.log('C is fun');
	}
} else {
	console.log('Missing number of occurrences');
}
