#!/usr/bin/node

const argv = process.argv.slice(2);

if (!(argv.length > 1)) {
  console.log(0);
} else {
  console.log(numbers.sort().reverse()[1]);
}
