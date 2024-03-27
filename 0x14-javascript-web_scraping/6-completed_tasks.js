#!/usr/bin/node

// Complete the task
const request = require('request');

request(process.argv[2], (error, response, body) => {
	if (!error) {
		console.log(JSON.parse(body).reduce(function (all, curr) {
			if (curr.completed) {
				all[curr.userId] = (all[curr.userId] || 0) + 1;
			}
			return all;
		}, {}));
	}
});
