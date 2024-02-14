#!/usr/bin/node

const { argv } = require('process');
const argc = argv.length;

if (argc < 4) {
  console.log(0);
  process.exit();
}

argv.sort();
let j = argc - 1;
for (; argv[j - 1] === argv[j]; j--) {
  // hh
}

console.log(parseInt(argv[j - 1]));
