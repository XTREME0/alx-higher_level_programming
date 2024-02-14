#!/usr/bin/node

exports.addMeMaybe = function (n, fnc) {
  n++;
  fnc(n);
};
