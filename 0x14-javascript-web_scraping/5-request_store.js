#!/usr/bin/node
// get contents of webpage and store in file

const fs = require('fs');
const request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFileSync(process.argv[3], body, 'utf8');
  }
});
