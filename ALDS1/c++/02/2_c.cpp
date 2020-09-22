#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int num[3];
    for (int i = 0; i < 3; i++)
        cin >> num[i];

    sort(num, num + 3);
    for (int i = 0; i < 3; i++)
    {
        if (i == 2)
            cout << num[i];
        if (i != 2)
            cout << num[i] << " ";
    }
    cout << endl;

    return 0;
}