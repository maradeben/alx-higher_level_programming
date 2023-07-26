#!/usr/bin/node
// display title of Star Wars episode

const request = require('request');

const options = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2],
  method: 'GET'
};

request(options, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
