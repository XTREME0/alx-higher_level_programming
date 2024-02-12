#!/usr/bin/node

const { argv } = require('process');
const argc = argv.length - 2;

if (argc === 1) {
  console.log('Argument found');
} else if (argc > 1) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
