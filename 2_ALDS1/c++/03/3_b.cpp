#include<iostream>
using namespace std;

int main(){
    int count=1,num;
    while (true)
    {
        cin >> num;
        if(num == 0)
            break;
        cout << "Case " << count << ": " << num << endl;
        count++;
    }
    return 0;
}