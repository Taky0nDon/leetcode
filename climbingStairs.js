/**
    This was a fun one. First I spent a lot of time treating the problem
as a matter of combinatorics. I tried applying a formula I found online for
permutations (n! / (n - r)!), but it didn't work. Finally, I asked Claude for a
hint. When it said 'Try working out a few small examples by hand (n=1, n=2,
n=3, n=4) and look for a pattern in the numbers. You might recognize this
sequence from mathematics!' I realized I was dealing with the fibonacci sequence!
    The recursive solution was too slow, and I decided to implement an iterative
approach instead.
    * @param {number} n
 * @return {number}
 //*/
//const factorial = (arr) => {
//    return arr.reduce((acc, curr) => acc * curr, 1);
//}
//const makeRangeArr = (start, stop, step) => {
//    let res = new Array;
//    for (i=start; i<stop; i+=step){
//        res.push(i);
//    }
//    return res;
//}
memo = new Map();
memo.set(1,1);
memo.set(2,2);
var climbStairs = function(n) {
    if (memo.has(n)){
        return memo.get(n);
    }
    for (i=3; i<n; i++){
        memo.set(i, memo.get(i-1) + memo.get(i-2));
    }
    return memo.get(n - 1) + memo.get(n - 2);
};
