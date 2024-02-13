#!/usr/bin/node

exports.esrever = function (list) {
  const max = list.length;
  const lst = [];
  for (let i = 0; i < max; i++) {
    lst.push(list[max - i - 1]);
  }
  return lst;
};
