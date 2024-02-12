#!/usr/bin/node
function factorial(n) {
	// Base case: factorial of 0 or 1 is 1
	if (n === 0 || n === 1) {
		return 1;
	}
	// Recursive case: compute factorial using recursion
	return n * factorial(n - 1);
}

// Retrieve the first argument passed to the script using process.argv
const arg = parseInt(process.argv[2]);

// Check if the argument is NaN
if (isNaN(arg)) {
	console.log(1); // Factorial of NaN is 1
} else {
	// Compute and print the factorial
	console.log(factorial(arg));
}
