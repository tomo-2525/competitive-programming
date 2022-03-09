# include <iostream>
# include <vector>
using namespace std;

int main(){
    int n,q;
    cin >> n >> q; 
    vector<int>  v2[n];

    int cmd,t,x;

    for(int i=0 ; i<q; i++){
        cin >> cmd;
        switch (cmd)
        {
        case 0:
            cin >> t >> x;
            v2[t].push_back(x);
            break;

        case 1:
            cin >> t;
            for(vector<int>::iterator it = v2[t].begin(); it != v2[t].end(); it++){
                if(it != v2[t].end()-1) cout << *it << " " ;
                else cout << *it;
            }
            cout << endl;
            break;
        
        case 2:
            cin >> t;
            v2[t].clear();
            break;
        }
    }
    return 0;
}