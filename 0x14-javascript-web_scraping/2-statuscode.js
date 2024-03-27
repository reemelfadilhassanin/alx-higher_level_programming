#!/usr/bin/node
const request = require('request');
request(process.argv[2], (_, r) => console.log(`code: ${r.statusCode}`));
