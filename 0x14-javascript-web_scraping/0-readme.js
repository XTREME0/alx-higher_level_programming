#!/usr/bin/node

const { argv } = require('process');
const fs = require('fs');

try {
  const contant = fs.readFileSync(argv[2], 'utf8');
  console.log(contant);
} catch (error) {
  console.log(error);
}
