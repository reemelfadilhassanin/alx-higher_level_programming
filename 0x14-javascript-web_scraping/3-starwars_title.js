#!/usr/bin/node
const request = require('request');
const [, , movieId] = process.argv;
request(`https://swapi-api.hbtn.io/api/films/${movieId}/`, (error, response, body) => console.log(error || JSON.parse(body).title));
