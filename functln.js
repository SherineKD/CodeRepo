/*Write a function argumentsLength that returns the count of arguments passed to it.
 

Example 1:

Input: args = [5]
Output: 1
Explanation:
argumentsLength(5); // 1*/

/**
 * @return {number}
 */
var argumentsLength = function(...args) {
    return args.length;
};

// Example
console.log(argumentsLength(5));           
console.log(argumentsLength(5, 10, 15));   
console.log(argumentsLength());            
