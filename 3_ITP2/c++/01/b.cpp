#include <iostream>
#include <deque>
using namespace std;

int main(){

    int n;
    cin >> n;
    deque<int> que;


    for(int i = 0; i < n; i++){
        int t, p1, p2;
        cin >> t;
        switch (t)
        {
        case 0:
            cin >> p1 >> p2;

            if(p1 == 0){
                que.push_front(p2);
            }else{
                que.push_back(p2);
            }
            break;
        
        case 1:
            cin >> p1;
            cout << que[p1] << endl;
        break;

        default:
            cin >> p1;
            if(p1 == 1) que.pop_back();
            else que.pop_front();
            break;
        }
    }

    return 0;
}


