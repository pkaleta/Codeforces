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

string s;
string pre;
string suf;
set<string> cnt;
bool preMatch[2005];
bool sufMatch[2005];


int main() {
    cin >> s >> pre >> suf;

    string cur;
//    for (int i = 0; i < s.size(); ++i)
//        cout << (int)preMatch[i] << " ";
//    cout << endl;
//    for (int i = 0; i < s.size(); ++i)
//        cout << (int)sufMatch[i] << " ";
//    cout << endl;

    int minSize = max(suf.size(), pre.size());
    if (minSize > s.size()) {
        cout << 0 << endl;
    } else {
        for (int i = 0; i <= s.size()-pre.size(); ++i) {
            cur = s.substr(i, pre.size());
            if (cur == pre) {
                preMatch[i] = true;
            }
        }

        for (int i = 0; i <= s.size()-suf.size(); ++i) {
            cur = s.substr(i, suf.size());
            if (cur == suf) {
                sufMatch[i+suf.size()-1] = true;
            }
        }

        for (int i = 0; i < s.size(); ++i) {
            for (int j = i; j < s.size(); ++j) {
                if (j-i+1 >= minSize && preMatch[i] && sufMatch[j]) {
                    cnt.insert(s.substr(i, j-i+1));
                }
            }
        }
        cout << cnt.size() << endl;
    }
    return 0;
}
