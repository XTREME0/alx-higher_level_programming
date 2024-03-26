#!/usr/bin/node

const { argv } = require('process');
const fs = require('fs');

try {
  fs.writeFileSync(argv[2], argv[3], 'utf8');
} catch (error) {
  console.log(error);
}
