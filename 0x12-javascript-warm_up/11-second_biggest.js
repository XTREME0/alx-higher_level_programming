#!/usr/bin/node

const { argv } = require('process');
const argc = argv.length;

if (argc < 4) {
  console.log(0);
  process.exit();
}

let tmp = parseInt(argv[2]);

for (let i = 3; i < argc; i++) {
  if (tmp < parseInt(argv[i])) {
    tmp = parseInt(argv[i]);
  }
}

console.log(tmp);
