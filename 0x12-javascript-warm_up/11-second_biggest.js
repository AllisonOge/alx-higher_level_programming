#!/usr/bin/node
const argv = [];
for (let i = 2; i < process.argv.length; i++) {
  argv.push(parseInt(process.argv[i]));
}
if (argv.length === 0 || argv.length === 1)  console.log(0);
else {
  console.log(argv.sort()[argv.length - 2]);
}
