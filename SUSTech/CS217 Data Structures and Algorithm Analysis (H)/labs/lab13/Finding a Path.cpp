#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class GraphSolver {
private:
    int n;
    int s, t;

    vector<vector<int> > adj;
    vector<vector<int> > rev_adj;

    vector<bool> can_reach_t; // 标记哪些点可以到达终点 t
    vector<bool> is_valid; // 标记哪些点满足题目的"所有出边指向的点都能到达t"条件

public:
    GraphSolver(int nodes) : n(nodes) {
        adj.resize(n + 1);
        rev_adj.resize(n + 1);
        can_reach_t.assign(n + 1, false);
        is_valid.assign(n + 1, false);
    }

    void addEdge(int u, int v) {
        adj[u].push_back(v);
        rev_adj[v].push_back(u);
    }

    void setStartEnd(int startNode, int endNode) {
        s = startNode;
        t = endNode;
    }

    void preprocess() {
        // 一：反向 BFS
        queue<int> q;
        q.push(t);
        can_reach_t[t] = true; // 1. 必须先标记终点本身是"可达的"

        while (!q.empty()) {
            int u = q.front();
            q.pop();

            // 遍历所有"能走到 u"的点 (反向图的邻居)
            for (int v : rev_adj[u]) {
                // 2. 关键检查：如果 v 还没被访问过，才处理
                // 如果没有这个 if，有环的图会导致死循环！
                if (!can_reach_t[v]) {
                    can_reach_t[v] = true;
                    q.push(v);
                }
            }
        }

        // 二：筛选逻辑
        for (int i = 1; i <= n; i++) { // 建议下标从 1 循环到 n
            if (can_reach_t[i]) {
                bool valid = true;
                for (int v : adj[i]) {
                    if (!can_reach_t[v]) {
                        valid = false;
                        break;
                    }
                }
                is_valid[i] = valid;
            }
        }
    }

    int solve() {
        // 特判：如果起点本身就不合法，直接返回 -1
        if (!is_valid[s]) return -1;

        vector<int> dist(n+1, -1);
        queue<int> q;
        dist[s] = 0;
        q.push(s);
        while (!q.empty()) {
            int u = q.front();
            q.pop();

            if (u == t) return dist[t];

            for (int v : adj[u]) {
                if (!is_valid[v]) continue;

                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.push(v);
                }
            }
        }

        return -1; // 如果无法到达
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    GraphSolver solver(n);

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        solver.addEdge(u, v);
    }

    int s, t;
    cin >> s >> t;
    solver.setStartEnd(s, t);

    solver.preprocess();
    cout << solver.solve() << endl;

    return 0;
}
