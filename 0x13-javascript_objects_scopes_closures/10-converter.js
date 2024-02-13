#!/usr/bin/node

exports.converter = function (base) {
  return function cv (num) {
    return num.toString(base);
  };
};
