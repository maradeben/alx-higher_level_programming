#!/usr/bin/node
// count how many movies with character "Wedge Antilles"

const request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].endsWith('18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
