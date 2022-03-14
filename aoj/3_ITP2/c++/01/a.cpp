#include <iostream>
#include <vector>
using namespace std;

int main() {
	int q;
	cin >> q;
	vector<int> vec;

	for (int i = 0; i < q; i++) {
		int t;
		cin >> t;

		switch (t) {
		case 0:
		    cin >> t;
			vec.push_back(t);
			break;
		case 1:
			cin >> t;
			cout << vec[t] << "\n";
			break;
		default:
			vec.pop_back();
		}
	}

    return 0;
}