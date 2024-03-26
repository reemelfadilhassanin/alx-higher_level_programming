#!/usr/bin/node
// Write a script that display the status code of a GET request.
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
	error && console.log(error);
	response && console.log('code:', response.statusCode);
});
