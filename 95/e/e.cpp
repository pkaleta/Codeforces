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

map<int, vector<int> > dh;
map<int, vector<int> > dv;
map<int, vector<int> > ddl;
map<int, vector<int> > ddr;
int cnt[10];

int main() {
  int n, m;
  int r, c;
  vector<int> R;
  vector<int> C;

  cin >> n >> m;
  for (int i = 0; i < m; ++i) {
    cin >> r >> c;
    R.push_back(r);
    C.push_back(c);
    dv[r].push_back(c);
    dh[c].push_back(r);
    ddl[r+c].push_back(c);
    ddr[r-c].push_back(c);
  }

  map<int, vector<int> >::iterator it;

  for (it = dh.begin(); it != dh.end(); ++it) {
    sort(it->second.begin(), it->second.end());
  }

  for (it = dv.begin(); it != dv.end(); ++it) {
    sort(it->second.begin(), it->second.end());
  }

  for (it = ddl.begin(); it != ddl.end(); ++it) {
    sort(it->second.begin(), it->second.end());
  }

  for (it = ddr.begin(); it != ddr.end(); ++it) {
    sort(it->second.begin(), it->second.end());
  }


  for (int i = 0; i < m; ++i) {
    int c = 0;

    int p = lower_bound(dh[C[i]].begin(), dh[C[i]].end(), R[i])-dh[C[i]].begin();
    if (dh[C[i]].size() == 2) c += 1;
    else if (dh[C[i]].size() > 2) {
      if (p == 0) c += 1;
      else if (p == dh[C[i]].size()-1) c += 1;
      else c += 2;
    }

    p = lower_bound(dv[R[i]].begin(), dv[R[i]].end(), C[i])-dv[R[i]].begin();
    if (dv[R[i]].size() == 2) c += 1;
    else if (dv[R[i]].size() > 2) {
      if (p == 0) c += 1;
      else if (p == dv[R[i]].size()-1) c += 1;
      else c += 2;
    }

    p = lower_bound(ddl[R[i]+C[i]].begin(), ddl[R[i]+C[i]].end(), C[i])-ddl[R[i]+C[i]].begin();
    if (ddl[R[i]+C[i]].size() == 2) c += 1;
    else if (ddl[R[i]+C[i]].size() > 2) {
      if (p == 0) c += 1;
      else if (p == ddl[R[i]+C[i]].size()-1) c += 1;
      else c += 2;
    }

    p = lower_bound(ddr[R[i]-C[i]].begin(), ddr[R[i]-C[i]].end(), C[i])-ddr[R[i]-C[i]].begin();
    if (ddr[R[i]-C[i]].size() == 2) c += 1;
    else if (ddr[R[i]-C[i]].size() > 2) {
      if (p == 0) c += 1;
      else if (p == ddr[R[i]-C[i]].size()-1) c += 1;
      else c += 2;
    }
    cnt[c] += 1;
  }

  for (int i = 0; i <=8; ++i)
    cout << cnt[i] << " ";
  cout << endl;
  return 0;
}
