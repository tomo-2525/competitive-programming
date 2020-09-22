#include <iostream>
using namespace std;

int main()
{
    int W, H, x, y, r;
    bool flag = true;
    cin >> W >> H >> x >> y >> r;
    if (x < r || W - r < x)
        flag = false;
    if (y < r || H - r < y)
        flag = false;
    
    if(flag == false)
        cout << "No" << endl;
    else 
        cout << "Yes" << endl;
    return 0;
}