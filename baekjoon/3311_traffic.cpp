#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#include <map>
#include <climits>
#include <cmath>
#include <functional>
using namespace std;

int n, m, A, B;
vector<vector<int>> Ve;
vector<vector<int>> E;
vector<int> LM, RM;

vector<vector<int>> scc(const vector<vector<int>>& edge, int n) {
    vector<bool> grouped(n, false);
    vector<int> level_of(n, 0);
    stack<int> st;
    int level = 0;
    vector<vector<int>> groups;

    function<int(int)> dfs = [&](int u) -> int {
        level++;
        int last_level = level_of[u] = level;

        st.push(u);
        for (int v : edge[u]) {
            if (level_of[v] == 0) {
                last_level = min(last_level, dfs(v));
            } else if (!grouped[v]) {
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
    };

    for (int i = 0; i < n; i++) {
        if (!grouped[i]) {
            dfs(i);
        }
    }

    return groups;
}

vector<int> V_SCC;
vector<vector<int>> SCC_E;
vector<vector<int>> V;
map<int, int> SRMI;
vector<bool> visited_group;

pair<int, int> dfs(int u) {
    if (V[u][0]) {
        return {V[u][1], V[u][2]};
    }
    
    V[u][0] = true;
    visited_group[u] = true;
    for (int v : SCC_E[u]) {
        pair<int, int> result = dfs(v);
        int low = result.first;
        int top = result.second;
        V[u][1] = min(V[u][1], low);
        V[u][2] = max(V[u][2], top);
    }
    return {V[u][1], V[u][2]};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> n >> m >> A >> B;
    
    Ve.resize(n, vector<int>(2));
    for (int i = 0; i < n; i++) {
        cin >> Ve[i][0] >> Ve[i][1];
    }
    
    E.resize(n);
    for (int i = 0; i < m; i++) {
        int c, d, k;
        cin >> c >> d >> k;
        c--; d--;
        E[c].push_back(d);
        if (k == 2) {
            E[d].push_back(c);
        }
    }
    
    for (int i = 0; i < n; i++) {
        if (Ve[i][0] == 0) {
            LM.push_back(i);
        }
        if (Ve[i][0] == A) {
            RM.push_back(i);
        }
    }
    
    auto groups = scc(E, n);
    V_SCC.resize(n);
    
    for (int i = 0; i < groups.size(); i++) {
        for (int j = 0; j < groups[i].size(); j++) {
            V_SCC[groups[i][j]] = i;
        }
    }
    
    vector<vector<int>> groups_edge(groups.size());
    for (int u = 0; u < n; u++) {
        for (int v : E[u]) {
            if (V_SCC[u] != V_SCC[v]) {
                groups_edge[V_SCC[u]].push_back(V_SCC[v]);
            }
        }
    }
    
    SCC_E.resize(groups.size());
    visited_group.resize(groups.size(), false);
    for (int i = 0; i < groups.size(); i++) {
        // 중복 제거
        sort(groups_edge[i].begin(), groups_edge[i].end());
        groups_edge[i].erase(unique(groups_edge[i].begin(), groups_edge[i].end()), groups_edge[i].end());
        SCC_E[i] = groups_edge[i];
    }
    
    V.resize(groups.size(), vector<int>{0, INT_MAX, INT_MIN});
    for (int rm : RM) {
        V[V_SCC[rm]][1] = min(V[V_SCC[rm]][1], Ve[rm][1]);
        V[V_SCC[rm]][2] = max(V[V_SCC[rm]][2], Ve[rm][1]);
    }
    
    vector<pair<int, int>> SLM_pairs, SRM_pairs;
    for (int lm : LM) {
        SLM_pairs.push_back({Ve[lm][1], lm});
    }
    for (int rm : RM) {
        SRM_pairs.push_back({Ve[rm][1], rm});
    }
    
    sort(SLM_pairs.rbegin(), SLM_pairs.rend());
    sort(SRM_pairs.rbegin(), SRM_pairs.rend());
    
    vector<int> SLM, SRM;
    for (auto p : SLM_pairs) SLM.push_back(p.second);
    for (auto p : SRM_pairs) SRM.push_back(p.second);

    vector<vector<int>> ans;
    for (int i = 0; i < SLM.size(); i++) {
        pair<int, int> result = dfs(V_SCC[SLM[i]]);
        int low = result.first;
        int top = result.second;
        ans.push_back({low, top});
    }
    
    vector<int> remain_SRM;
    for (int srm : SRM){
        if (visited_group[V_SCC[srm]]){
            remain_SRM.push_back(srm);
        }
    }

    for (int i = 0; i < remain_SRM.size(); i++) {
        SRMI[Ve[remain_SRM[i]][1]] = remain_SRM.size() - i;
    }

    for (vector<int> result : ans) {
        if (result[1] < result[0]){
            cout << 0 << "\n";
        }
        else{
            cout << SRMI[result[1]] - SRMI[result[0]] + 1 << "\n";
        }
    }
    
    return 0;
}