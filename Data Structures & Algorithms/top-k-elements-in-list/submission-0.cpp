class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> frequency;
        for (int i : nums) frequency[i]++;

        vector<vector<int>> buckets(nums.size() + 1);
        for (auto& [num, freq] : frequency) buckets[freq].push_back(num);

        vector<int> ans;
        int i = buckets.size() - 1;
        while (ans.size() < k && i > 0) {
            for (int n : buckets[i]) {
                ans.emplace_back(n);
            }
            i--;
        }
        return ans;
    }
};