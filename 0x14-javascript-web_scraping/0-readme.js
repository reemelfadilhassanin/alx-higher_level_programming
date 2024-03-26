#!/usr/bin/node

const fs = require('fs');
const fName = process.argv[2];

if (!fName) {
	console.log('Usage: node script.js <file_path>');
	process.exit(1);
}

fs.readFile(fName, 'utf-8', function (err, data) {
	if (err) {
		console.log(err);
	} else {
		console.log(data);
	}
});
