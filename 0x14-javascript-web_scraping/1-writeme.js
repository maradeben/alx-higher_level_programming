#!/usr/bin/node
// write to a file

const fs = require('fs');
try {
  fs.writeFileSync(process.argv[2], process.argv[3], 'utf8');
} catch (err) {
  console.log(err);
}
