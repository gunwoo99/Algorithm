#include <iostream>
#include <vector>
#include <cmath>
#include <string>

typedef long long ll;
using namespace std;

const ll mod = 998244353;
const ll w = 3;

ll power(ll a, ll b) {
    long long ret = 1;
    while (b) {
        if (b & 1) 
            ret = (ret * a) % mod;
        a = (1LL * a * a) % mod;
        b /= 2;
    }
    return ret;
}

vector<ll> NTT(vector<ll>& A, bool inv=false) {
    int n = A.size();
    
    vector<ll> rev(n);
    for (int i = 0; i < n; ++i) {
        rev[i] = rev[i >> 1] >> 1;
        if (i & 1) 
            rev[i] |= n >> 1;
        if (i < rev[i]) 
            swap(A[i], A[rev[i]]);
    }
    
    ll x = power(w, (mod - 1) / n);
    if (inv) {
        x = power(x, mod - 2);
    }
    
    vector<ll> root(n, 1);
    for (int i = 1; i < n; ++i) {
        root[i] = (root[i-1] * x) % mod;
    }
    
    for (int i = 2; i <= n; i <<= 1) {
        ll step = n / i;
        for (int j = 0; j < n; j += i) {
            for (int k = 0; k < (i >> 1); ++k) {
                ll u = A[j|k];
                ll v = (A[j|k|(i >> 1)] * root[step*k]) % mod;
                A[j|k] = (u + v) % mod;
                A[j|k|(i >> 1)] = (u - v) % mod;
                if (A[j|k|(i >> 1)] < 0) 
                    A[j|k|(i >> 1)] += mod;
            }
        }
    }
    
    if (inv) {
        ll t = power(n, mod - 2);
        for (int i = 0; i < n; ++i) 
            A[i] = (A[i] * t) % mod;
    }
    return A;
}

vector<ll> multiply(vector<ll>& a, vector<ll>& b) {
    int n = max(a.size(), b.size());
    n = 2 * pow(2, ceil(log2(n)));
    a.resize(n);
    b.resize(n);
    vector<ll> A = NTT(a, false);
    vector<ll> B = NTT(b, false);
    vector<ll> result(n);
    for (int i = 0; i < n; ++i){
        result[i] = (A[i] * B[i]) % mod;
    }
    return NTT(result, true);
}

int main() {
    string a;
    string b;
    cin >> a >> b;
    int n = max(a.size(), b.size());
    vector<ll> A(n);
    vector<ll> B(n);

    for (int i = 0; i < a.size(); i++){
        A[i] = stoll(a.substr(a.size()-i-1, 1));
    }
    for (int i = 0; i < b.size(); i++){
        B[i] = stoll(b.substr(b.size()-i-1, 1));
    }
    vector<ll> result = multiply(A, B);
    for(int i = 0; i < result.size(); i++){
        ll cur = result[i];
        result[i] %= 10;
        int j = 1;
        while (cur / 10 > 0){
            result[i + j] += (cur / 10) % 10;
            cur /= 10;
            j += 1;
        }
    }
    int i = result.size() - 1;
    while (result[i] == 0){
        i -= 1;
    }
    if (i < 0){
        cout << 0;
    }
    for (int j = i; j > -1; j--){
        cout << result[j];
    }
}
