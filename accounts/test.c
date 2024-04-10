#include<stdio.h>
void solve()
{
    int a=3;
    int res= a++ + ++a + a++ + ++a;
    printf("%d",res); // 3+5+5+7=20
}
void main()
{
    solve();
}