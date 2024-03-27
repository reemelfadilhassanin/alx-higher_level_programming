#!/usr/bin/node
require('request')(process.argv[2], (_, r, b) => console.log(JSON.parse(b).title))
