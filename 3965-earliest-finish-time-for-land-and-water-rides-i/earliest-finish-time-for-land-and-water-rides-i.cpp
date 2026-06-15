class Solution {
public:
    int earliestFinishTime(vector<int>& landStartTime, vector<int>& landDuration, vector<int>& waterStartTime, vector<int>& waterDuration) {

        int n = landStartTime.size();
        int m = waterStartTime.size();

        int bestLandFinish = INT_MAX, bestWaterFinish = INT_MAX;
        for (int i = 0; i < n; i++)
            bestLandFinish = min(bestLandFinish, landStartTime[i] + landDuration[i]);
        for (int j = 0; j < m; j++)
            bestWaterFinish = min(bestWaterFinish, waterStartTime[j] + waterDuration[j]);

        int ans = INT_MAX;

        // land first then water
        for (int j = 0; j < m; j++)
            ans = min(ans, max(bestLandFinish, waterStartTime[j]) + waterDuration[j]);

        // water first then land
        for (int i = 0; i < n; i++)
            ans = min(ans, max(bestWaterFinish, landStartTime[i]) + landDuration[i]);

        return ans;
    }
};
