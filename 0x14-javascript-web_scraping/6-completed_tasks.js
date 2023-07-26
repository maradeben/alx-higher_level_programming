#!/usr/bin/node
// compute number of tasks completed by user id

const request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    let dash = {};
    for (let i = 0; i < todos.length; i++) {
      let key = todos[i]['userId'].toString();
      if (todos[i]['completed']) {
        if (dash[key]) {
          dash[key]++;
        } else {
          dash[key] = 1;
        }
      }
    }
    console.log(dash);
  }
});
