# include <iostream>
# include <list>
using namespace std;

int main(){
    list<int> L;
    int n,t,x;

    list<int>::iterator it;
    it = L.end();

    cin >> n;

    for(int i=0; i<n; i++){
        cin >> t;
        switch (t)
        {
        case 0:
            cin >> x;
            it = L.insert(it, x);
            break;

        case 1:
            cin >> x;
            it = next(it, x);
            break;
        
        default:
            it = L.erase(it);
            break;
        }
    }

    for (list<int>::iterator it = L.begin(); it != L.end(); it++){
        cout << *it << endl;
    }

    return 0;
}