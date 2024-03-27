#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
	if (error) {
		console.error(error);
		return;
	}

	if (response.statusCode !== 200) {
		console.error(`Error: Status code ${response.statusCode}`);
		return;
	}

	const movieData = JSON.parse(body);
	const charactersUrls = movieData.characters;

	charactersUrls.forEach((characterUrl) => {
		request(characterUrl, (error, response, body) => {
			if (error) {
				console.error(error);
				return;
			}

			if (response.statusCode !== 200) {
				console.error(`Error: Status code ${response.statusCode}`);
				return;
			}

			const characterData = JSON.parse(body);
			console.log(characterData.name);
		});
	});
});
