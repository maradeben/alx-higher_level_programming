#!/usr/bin/node
// read and print contents of file

const fs = require('fs');
const data = fs.readFileSync(process.argv[2], 'utf8');
console.log(data);
