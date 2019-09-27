
#include <iostream>
#include "Calculator.h"
using namespace std;

int main()
{
	double x, y, result = 0.0;
	char oper = '+';
	
	cout << "Calculator Console Application\n" << endl;
	cout << "Please enter the operation to perform. Format a+b | a*b | a-b | a/b\n";
	
	Calculator c;
	while (true) {
		cin >> x >> oper >> y;
		if ((y == 0) && (oper == '/')){
			cout << "Cannot divide by Zero\n";
			continue;
		}

		else {
			result = c.Calculate(x, oper, y);
		}
		
		cout << "The result is: " << result << endl;
	}
	return 0;
}
