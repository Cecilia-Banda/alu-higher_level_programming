#!/usr/bin/node
const args = process.argv;
const conA = Number(args[2]);
const conB = Number(args[3]);
let bigNow = conA;
let secondlargest = conB;
if (args.length <= 3) {
  console.log(0);
} else {
  for (let i = 3; i < args.length; i++) {
    if (Number(args[i]) > bigNow) {
      secondlargest = bigNow;
      bigNow = Number(args[i]);
    }
    if (Number(args[i]) > secondlargest && Number(args[i]) < bigNow) {
      secondlargest = Number(args[i]);
    }
  }
  console.log(secondlargest);
}
