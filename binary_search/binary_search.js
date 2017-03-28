/**
 * Non-recursive version of binary serach 
 * 
 * @param {integer} item item to search for
 * @param {integer[]} list list to search in
 * @returns {boolean} is found or not
 */
function binarySearch(item, list) {
    first = 0;
    last = list.length - 1;
    found = false;

    while (first <= last && found === false) {
        midpoint = parseInt((first + last) / 2, 10);
        if (list[midpoint] == item) {
            return true;
        } else {
            if (item < list[midpoint]) {
                last = midpoint-1;
            } else {
                first = midpoint+1;
            }
        }
    }
}

console.assert(binarySearch(9, [1, 3, 5, 7, 9]), true);
console.assert(binarySearch(4, [2, 4, 6, 8, 10, 12]), true);