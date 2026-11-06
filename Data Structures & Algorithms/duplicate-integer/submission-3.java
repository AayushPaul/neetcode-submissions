class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> setNums = new HashSet<Integer>(); 
        boolean result = false; 

        for (int i = 0; i < nums.length; i++) {
            if (setNums.contains(nums[i])) {
                result = true; 
            }

            setNums.add(nums[i]); 
        }

        return result; 
    }
}
