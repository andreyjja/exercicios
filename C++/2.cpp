#include <stdio.h>
#include <conio.h>

int main(){
float a, b, c;

printf("entre com as dimensoes dos lados de m tringulo:\n\n");
printf("lado a: ?");
scanf("%f", &a);
printf("lado b");
scanf("%f", &b);
printf("lado c");
scanf("%f", &c);

if ((a<(b+c))&&(b<(a+c))&&(c<(a+b)))

    if ((a==b)&&(b==c))
        printf("o triangulo e equilatero");
    
    else
        if ((a==b)&&(a==c)&&(c==b))
        printf("o triangulo e isosceles");
        
            
        else
        printf("tringulo qualqr");
                
       

else
printf("n é um triangulo");

getch();

}
