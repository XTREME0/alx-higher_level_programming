#!/usr/bin/node

exports.callMeMoby = function (i, fnc) {
  for (let x = 0; x < i; x++) {
    fnc();
  }
};
