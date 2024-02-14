#!/usr/bin/node

const { argv } = require('process');
const argc = argv.length;

if (argc < 4) {
  console.log(0);
  process.exit();
}

argv.sort();
console.log(parseInt(argv[argc - 2]));
