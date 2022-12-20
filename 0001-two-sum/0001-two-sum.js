/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
        // instantiate dictionary:L
    let dict = {};
    // iterate through nums
    for (let i=0; i<nums.length; i++) {
      // declare difference in var
      let diff = target - nums[i];
      // if difference exists in dict:
      if (diff in dict) {
        // return the index of the difference and the current index
        return [dict[diff], i];
    } else {
      // else add the current number value to dict with the index as the key
      dict[nums[i]] = i;
    }
  }
};