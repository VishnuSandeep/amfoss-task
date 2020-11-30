include <stdio.h>
#include <math.h>

int main()
{
    int cents_owed;

     do
   {
    float dollars = scanf("%f", &dollars);
    cents_owed = round(dollars * 100);
   }

   while(cents_owed <=0);


    int quarters = cents_owed / 25;
    int dimes = (cents_owed % 25) / 10;
    int nickels = ((cents_owed % 25) % 10) / 5;
    int pennies = ((cents_owed % 25) % 10) % 5;

   printf("%d\n", quarters + dimes + nickels + pennies);
}
