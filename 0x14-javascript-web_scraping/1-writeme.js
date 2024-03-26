#!/usr/bin/node
// a script that writes a string to a file.
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], (err) => {
	if (err) {
		console.error(err);
		return;
	}
	console.log(`Content has been written to ${process.argv[2]}`);
});
