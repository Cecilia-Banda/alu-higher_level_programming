#!/usr/bin/node
exports.esrever = function (list) {
  const temp = [];
  let count = 0;
  for (let i = (list.length - 1); i >= 0; i--) {
    temp[i] = list[count];
    count++;
  }
  return temp;
};
