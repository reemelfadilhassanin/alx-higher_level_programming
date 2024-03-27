#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
	console.error('Usage: ./101-starwars_characters.js <movie_ID>');
	process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a GET request to the Star Wars API
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

	// Fetch data for each character
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
