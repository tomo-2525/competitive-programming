/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {

    public int[] twoSum(int[] nums, int target) {
        final int result[] = new int[2];
        // num[i] -> i
        // intilize map to store num and its position
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int sec = target - nums[i];
            if (map.containsKey(sec)) {
                result[0] = i;
                result[1] = map.get(sec);
                return result;
            }
            // else
            map.put(nums[i], i);

        }
        return result;
    }
}
// @lc code=end

