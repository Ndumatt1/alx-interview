#!/usr/bin/node
const request = require('request');

const filmId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

request(url, async (error, response, body) => {
  // If there is an error, print to console and exit
  if (error) {
    console.error(error);
  } else { // Otherwise, print the characters
    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    for (const characterUrl of characters) {
      try {
        // Call the fetch function and await the response
        const characterData = await fetch(characterUrl);
        // Get the name from the response and print to console
        const name = characterData.name;
        console.log(name);
      } catch (error) {
        console.error(error);
      }
    }
  }
});

// Function to make a request to a URL and return the response
function fetch (url) {
  // Return a new promise. The promise will ensure that the request is
  // completed before the function returns
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}
