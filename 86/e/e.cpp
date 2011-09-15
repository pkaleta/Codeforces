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

const int MAX = 3 * 100000001;
bool isPrime[MAX];
vector<int> primes;

int main() {
    int l, r;
    cin >> l >> r;
    set<int> a;
    set<int> b;

    memset(isPrime, 1, sizeof(isPrime));
    isPrime[0] = isPrime[1] = false;
    for (int i = 2; i < MAX; ++i) {
        if (isPrime[i]) {
            primes.push_back(i);
            int j = i+i;
            while (j < MAX) {
                isPrime[j] = false;
                j += i;
            }
        }
    }

//    for (int i = 0; i < primes.size(); ++i) {
//        cout << primes[i] << ", ";
//    }
    cout << primes.size() << endl;


//    for (int i = 0; i <= 17321; ++i) {
//        int j = 1;
//        while (i*i+j*j <= MAX) {
//            cout << i*i+j*j << endl;
//            a.insert(i*i+j*j);
//            ++j;
//        }
//    }


    return 0;
}
