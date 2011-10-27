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

const long long MAX_LUCKY = 4444444444LL;

vector<long long> lucky;

void genLucky(long long n) {
  if (n > MAX_LUCKY) return;
  lucky.push_back(n);
  genLucky(n*10+4);
  genLucky(n*10+7);
}

int main() {
  long long l, r;


  genLucky(4);
  genLucky(7);
  sort(lucky.begin(), lucky.end());

  // for (int i = lucky.size()-10; i < lucky.size(); ++i) {
  //   cout << lucky[i] << endl;
  // }

  cin >> l >> r;

  long long ret = 0;
  long long cur = l;
  if (r <= lucky[0]) {
    ret = (r-l+1)*lucky[0];
  } else {
    long long i = lower_bound(lucky.begin(), lucky.end(), l)-lucky.begin();
    if (r <= lucky[i])
      ret = (r-l+1)*lucky[i];
    else {
      while (i < lucky.size() && r >= lucky[i]) {
        ret += (lucky[i]-cur+1)*lucky[i];
        cur = lucky[i++]+1;
      }
      if (r > lucky[i-1])
        ret += (r-lucky[i-1])*lucky[i];
    }
  }
  cout << ret << endl;
  return 0;
}
