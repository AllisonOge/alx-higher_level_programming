#!/usr/bin/node
const argv = [];
for (let idx = 2; process.argv[idx] !== undefined; idx++) {
  argv.push(process.argv[idx]);
}
if (argv.length === 0) {
  argv.push('undefined');
  argv.push('undefined');
} else if (argv.length === 1) {
  argv.push('undefined');
}
console.log(argv.join(' is '));
