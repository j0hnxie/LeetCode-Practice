class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        vector<vector<string>> res;
        for (int i = 0; i < strs.size(); i++)
        {
            string curWord = strs[i];
            sort(strs[i].begin(), strs[i].end());
            map[strs[i]].push_back(curWord);
        }
        for (auto list : map)
        {
            res.push_back(list.second);
        }
        return res;
        
    }
};