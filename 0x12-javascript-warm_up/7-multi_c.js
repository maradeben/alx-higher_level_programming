#!/usr/bin/node

const freq = process.argv[2];
if (isNaN(freq)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(freq); i++) {
    console.log('C is fun');
  }
}
