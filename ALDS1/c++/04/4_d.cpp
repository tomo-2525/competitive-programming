#include <iostream>
using namespace std;

int main()
{
    int n, min = 10000005, max = -10000005;
    long long sum = 0;
    cin >> n;
    int num[n];
    for (int i = 0; i < n; i++)
    {
        cin >> num[i];
    }
    for (int i = 0; i < n; i++)
    {
        if (min > num[i])
            min = num[i];
        if (max < num[i])
            max = num[i];
        sum += num[i];
    }
    cout << min << " " << max << " " << sum << endl;

    return 0;
}