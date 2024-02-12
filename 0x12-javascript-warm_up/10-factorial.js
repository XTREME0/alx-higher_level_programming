#!/usr/bin/node

const { argv } = require('process');
const num = parseInt(argv[2]);

function factorial (n) {
  if (n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

if (isNaN(num) || num === 0 || num === 1) {
  console.log(1);
} else {
  console.log(factorial(num));
}
