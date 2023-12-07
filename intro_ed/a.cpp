#include <bits/stdc++.h>
using namespace std;
#define int long long int
#define endl '\n'



void solve(){
    int n; cin >> n; 
    n+=2;
    vector<int> v(n+1); 
    for (int i=1; i<=n; i++){
        cin >> v[i];
    }
    sort(v.begin()+1; v.end());
    int sm=0;
    for(int i=1; i<=n-2; i++) sm+= v[i];
    if (sm==v[n-1] or sm==v[n-2]){
        for (int i=1; i<n-2; i++) cout << v[i]<< " ";
        cout << endl
    }

    for (int i=1;  i<n-2; i++){
        int aux = v[i];
        if(v[])
    }

}

int32_t main(){
    int t; cin >> t; 
    while(t--) solve();
}