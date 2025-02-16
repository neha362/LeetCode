//Apply Transform Over Each Element in Array, solved Feb 16 2025
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let x = Array(arr.length);
    for (let y = 0; y < x.length; y++) {
        x[y] = fn(arr[y], y);
    }
    return x;
};
