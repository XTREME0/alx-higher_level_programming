#!/usr/bin/node

const { argv } = require('process');

if (isNaN(parseInt(argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    console.log('x');
  }
}
