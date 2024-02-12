#!/usr/bin/node
let x;
if (process.argv.length === 2) {
    x = 'No argument';
} else if (process.argv.length === 3) {
    x = 'Argument found';
} else {
    x = 'Arguments found';
}
console.log(x);
