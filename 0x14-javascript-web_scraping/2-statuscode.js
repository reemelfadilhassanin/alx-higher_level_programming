#!/usr/bin/node
require('request')(process.argv[2], (_, r) => console.log(`code: ${r.statusCode}`))
