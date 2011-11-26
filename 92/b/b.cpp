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

int permute(string& s, vector<int>& perm) {
  string ret = "";
  for (int i = 0; i < perm.size(); ++i) {
    ret += s[perm[i]];
  }
  return atoi(ret.c_str());
}

int main() {
  int n, k;
  cin >> n >> k;

  vector<string> x;
  for (int i = 0; i < n; ++i) {
    string s;
    cin >> s;
    x.push_back(s);
  }

  vector<int> perm;
  for (int i = 0; i < k; ++i)
    perm.push_back(i);

  int ret = 99999999;
  do {
    int xmax = -1;
    int xmin = 99999999;
    for (int i = 0; i < x.size(); ++i) {
      xmax = max(xmax, permute(x[i], perm));
      xmin = min(xmin, permute(x[i], perm));
    }
    ret = min(ret, xmax-xmin);
  } while (next_permutation(perm.begin(), perm.end()));

  cout << ret << endl;
  return 0;
}
