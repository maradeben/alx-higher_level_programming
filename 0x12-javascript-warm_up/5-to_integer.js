#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const arg = argv[2];

if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log('My number: ', parseInt(arg));
}
