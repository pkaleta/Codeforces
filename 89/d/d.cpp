#include <cstdio>
#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cstring>

using namespace std;

const int MOD = 100000000;
int n1, n2, k1, k2;

map<vector<int>, int> dp;

int calc(int al, int bl, int ac, int bc) {
  if (ac > k1 || bc > k2)
    return 0;
  if (al < 0 || bl < 0)
    return 0;
  if (al == 0 && bl == 0)
    return 1;

  vector<int> v;
  v.push_back(al); v.push_back(bl); v.push_back(ac); v.push_back(bc);
  if (dp.find(v) == dp.end())
    dp[v] = (calc(al-1, bl, ac+1, 0) + calc(al, bl-1, 0, bc+1)) % MOD;

  return dp[v];
}


int main() {
  cin >> n1 >> n2 >> k1 >> k2;

  cout << calc(n1, n2, 0, 0) << endl;
  return 0;
}
