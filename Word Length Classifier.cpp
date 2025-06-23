#include <iostream>
using namespace std;

int main()
{
    string word;
    cin>>word;
    int counter=0;
    for (int i=0;i<word.length();++i)
        {
            counter++;
        }
    if (counter>6)
        {
            cout<<"Long"<<endl;
        }
    else
        {
            cout<<"Short"<<endl;
        }

    return 0;
}