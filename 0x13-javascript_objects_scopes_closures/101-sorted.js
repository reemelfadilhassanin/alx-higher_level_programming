#!/usr/bin/node
const dict = require('./101-data').dict;

const usersOccur = Object.entries(dict).reduce((accumulator, [userId, occurrence]) => {
	accumulator[occurrence] = (accumulator[occurrence] || []).concat(userId);
	return accumulator;
}, {});

console.log(usersOccur);
