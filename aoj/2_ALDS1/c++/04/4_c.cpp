#include <iostream>
using namespace std;

int main()
{

    string num1, op, num2;

    while (true)
    {
        cin >> num1 >> op >> num2;
        int a = stoi(num1);
        int b = stoi(num2);
        if (op == "?")
            break;
        if (op == "+")
            cout << a + b << endl;
        if (op == "-")
            cout << a - b << endl;
        if (op == "*")
            cout << a * b << endl;
        if (op == "/")
            cout << a / b << endl;
    }
    return 0;
}