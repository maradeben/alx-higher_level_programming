#!/usr/bin/node
// display status code of a GET request

const request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ', response.statusCode);
  }
});
