#include <stdio.h>
#include <conio.h>

int main(){
    float idade;

    printf("Entre com a idade da pessoa: ? ");
    scanf("%f", &idade);
    
    if (idade <= 2)
        printf("e um bebe\n");
    else
        if (idade <= 12)
            printf("e uma crianca\n");
        else
            if (idade <= 23)
                printf("e um adolescesente\n ");
            else
                if (idade <= 70)
                    printf("e um adulto\n");
                else
                    printf("e um idoso\n");



getch();
}