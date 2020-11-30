#include <stdio.h>

int main(void)
{
   int height;

    do
    {
        printf("height of the pyramid: ");
        scanf("%d", &height);
    }
    while (height < 0 || height > 23);

    for (int row = 0; row < height; row++)
    {
        for (int spaces = height - row; spaces > 1; spaces--)
        {
            printf(" ");
        }
        for (int hashes = 0; hashes < row + 2; hashes++)
        {
            printf("#");
        }
        printf("\n");
    }
}
