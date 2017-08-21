//#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;


class Solution {
public:
    /**
     * @param n, m: positive integer (1 <= n ,m <= 100)
     * @return an integer
     */
    int uniquePaths(int m, int n) {
        // wirte your code here
        if(m <= 0 || n <= 0) {
            return 0;
        }
        
        vector<vector<int> > dp(m, vector<int>(n, INT_MAX));
        for(int i=0; i<m; i++) {
            for(int j=0; j<n; j++) {
                if(i == 0 && j == 0) {
                    dp[i][j] = 1;
                }
                else if(i == 0 && j > 0) {
                    dp[i][j] = dp[i][j-1];
                }
                else if(i > 0 && j == 0) {
                    dp[i][j] = dp[i-1][j];
                }
                else if(i > 0 && j > 0) {
                    dp[i][j] = dp[i][j-1] + dp[i-1][j];
                }
            }
        }
        
        return dp[m-1][n-1];
    }
};

int main() {
    Solution Solution1;

}