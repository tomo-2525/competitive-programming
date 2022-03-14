#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    int a, b, r;
    cin >> a >> b;
    cout << a / b << " " << a % b << " ";
    cout << fixed << setprecision(6)<< (double)a / b << endl;
    return 0;
}