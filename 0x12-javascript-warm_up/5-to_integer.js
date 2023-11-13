#!/usr/bin/node
const number = process.argv[2];
if (isNaN(parseInt(number))) {
    console.log("Not a number");
} else console.log(`My number: ${parseInt(number)}`);
