#!/usr/bin/node
/**
 * A script that prints all characters of a Star Wars movie
 * Accepts arguments: first of which is the Movie ID e.g. 3
 * Requirements: Must use the Star Wars API (https://swapi-api.alx-tools.com/api/) and the request module
 */

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/';
// check that the cmdline parameter is provided
if (process.argv.length > 2) {
  request(url + `films/${Number(process.argv[2])}`, async function (error, response, body) {
    if (error) console.log(error);
    // get an object rep of the characters from JSON body
    const characters = JSON.parse(body).characters;
    // console.log('characters: ', characters);
    for (const character of characters) {
      // await resolution of preceding request b4 continuing to the next one - else characters not printed in order
      await new Promise((resolve, reject) => {
        request(character, function (error, response, body) {
          if (error) console.log(error);
          // console.log(JSON.parse(body).name, ' -> ', character);
          console.log(JSON.parse(body).name);
          resolve();
        });
      });
    }
  });
}
