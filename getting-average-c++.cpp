#include <iostream>
using namespace std;

int main(){
  str aNumber, c1, c2, c3, c4, c5;
  int g1, g2, g3, g4, g5, average;

  cout << "Input A#" << endl;
  cin >> aNumber >> endl;
  cout << "Enter 5 of your courses separated by space" << endl;
  cin >> c1 >> c2 >> c3 >> c4 >> c5 >> endl;
  cout << "Enter the grades of each course in the same order separated by space"
   << endl;
  cin >> g1 >> g2 >> g3 >> g4 >> g5 >> endl;

  average = (g1 + g2 + g3 + g4 + g5) / 5;

  cout << "A# " << aNumber << endl;
  cout << "Your grades are " << c1, g1 << c2, g2 << c3, g3 << c4, g4 << c5, g5 
  << endl;
  cout << "Your average grade is " << average << endl;

  return 0
}
