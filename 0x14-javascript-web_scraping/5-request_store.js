#!/usr/bin/node

const { argv } = require('process');
const fs = require('fs');
const r = require('request');

r(argv[2]).pipe(fs.createWriteStream(argv[3]));
