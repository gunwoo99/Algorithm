#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

const int MAX_N = 500001;

int N, M, S, P;
vector<vector<int>> E;
vector<int> H, RN;
vector<int> grouped, level_of;
vector<int> U_SCC, SCC_H, SCC_D;
vector<bool> SCC_C, SCC_V;
vector<vector<int>> SCC_E;
stack<int> st;
int level = 0;
vector<vector<int>> groups;

int dfs(int u) {
    level++;
    int last_level = level_of[u] = level;
    
    st.push(u);
    for (int v : E[u]) {
        if (!level_of[v]) {
            last_level = min(last_level, dfs(v));
        }
        else if (!grouped[v]) {
            last_level = min(last_level, level_of[v]);
        }
    }
    
    if (last_level == level_of[u]) {
        vector<int> group;
        while (!st.empty()) {
            int p = st.top();
            st.pop();
            group.push_back(p);
            grouped[p] = true;
            if (u == p) break;
        }
        groups.push_back(group);
    }
    return last_level;
}

vector<vector<int>> scc(int n) {
    grouped.assign(n, false);
    level_of.assign(n, false);
    level = 0;
    groups.clear();
    
    for (int i = 0; i < n; i++) {
        if (!grouped[i]) {
            dfs(i);
        }
    }
    return groups;
}

void scc_dfs(int u) {
    SCC_V[u] = true;
    
    for (int v : SCC_E[u]) {
        if (SCC_V[v]) continue;
        scc_dfs(v);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> N >> M;
    E.resize(N);
    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        E[u-1].push_back(v-1);
    }
    
    H.resize(N);
    for (int i = 0; i < N; i++) {
        cin >> H[i];
    }
    
    cin >> S >> P;
    RN.resize(P);
    for (int i = 0; i < P; i++) {
        cin >> RN[i];
    }
    
    groups = scc(N);
    int scc_num = groups.size();
    
    U_SCC.resize(N);
    for (int i = 0; i < scc_num; i++) {
        for (int u : groups[i]) {
            U_SCC[u] = i;
        }
    }
    
    SCC_C.assign(scc_num, false);
    for (int i = 0; i < P; i++) {
        SCC_C[U_SCC[RN[i] - 1]] = true;
    }
    
    SCC_E.resize(scc_num);
    SCC_D.assign(scc_num, 0);
    SCC_H.assign(scc_num, 0);
    
    for (int i = 0; i < scc_num; i++) {
        for (int u : groups[i]) {
            SCC_H[i] += H[u];
            for (int v : E[u]) {
                if (U_SCC[u] == U_SCC[v]) continue;
                SCC_E[i].push_back(U_SCC[v]);
            }
        }
        sort(SCC_E[i].begin(), SCC_E[i].end());
        SCC_E[i].erase(unique(SCC_E[i].begin(), SCC_E[i].end()), SCC_E[i].end());
    }
    
    for (const auto& SCC_u : SCC_E) {
        for (int v : SCC_u) {
            SCC_D[v]++;
        }
    }
    
    SCC_V.assign(scc_num, false);
    scc_dfs(U_SCC[S - 1]);
    
    for (int i = 0; i < scc_num; i++) {
        if (SCC_V[i]) continue;
        for (int v : SCC_E[i]) {
            SCC_D[v]--;
        }
    }
    
    queue<int> Q;
    Q.push(U_SCC[S - 1]);
    vector<int> DP = SCC_H;
    
    while (!Q.empty()) {
        int u = Q.front();
        Q.pop();
        
        for (int v : SCC_E[u]) {
            SCC_D[v]--;
            DP[v] = max(DP[v], SCC_H[v] + DP[u]);
            if (SCC_D[v] == 0) {
                Q.push(v);
            }
        }
    }
    
    int max_value = 0;
    for (int i = 0; i < scc_num; i++) {
        if (SCC_C[i] && SCC_V[i]) {
            max_value = max(max_value, DP[i]);
        }
    }
    
    cout << max_value << '\n';
    
    return 0;
}