#!/usr/bin/node

const argv = process.argv.slice(2);

if (argv.length = <= 3) {
  console.log(0);
} else {
  // convert to numbers
  const numbers = [];
  for (const element of argv) {
    numbers.push(parseInt(element));
  }
  console.log(numbers.sort().reverse()[1]);
}
