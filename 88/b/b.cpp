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


int main() {
    long long a, b, m;
    cin >> a >> b >> m;

    if (b >= m) {
        printf("2\n");
        return 0;
    }
    for (int i = 0; i < m && i <= a; ++i) {
        long long x = (i * 1000000000LL) % m;
        if (x > 0 && b < m-x) {
            printf("1 %09d\n", i);
            return 0;
        }
    }
    printf("2\n");
    return 0;
}
