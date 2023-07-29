#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

#define VERSION "ESP-CF C-EDITION 1.0"
#define PROGRAMS "Calculator, SysInfo, Console"

void calculator();
void desktop();
void sysinfo();
void console();

int main()
{
        int bsel;
        printf("Select where to boot:\n[1] Desktop\n[2] Console\n");
        scanf("%d", &bsel);
        if (bsel == 1)
        {
                system("clear");
                desktop();
        }
        else if (bsel == 2)
        {
                system("clear");
                printf("--Console--\n");
                console();
        }
        else
        {
                system("clear");
                desktop();
        }
        return 0;
}
void calculator()
{
        int a,b,sum,op;
        printf("--Calculator--\n");
        printf("Select operation:\n[1] ADD\n[2] SUB\n[3] MUL\n[4] DIV\n[5] SQRT\n");
        scanf("%d", &op);
        printf("First number: \n");
        scanf("%d", &a);
        if (op == 5)
        {
                double sum = sqrt(a);
                printf("%f", sum);
                goto calagain;
        }
        printf("Second number: \n");
        scanf("%d", &b);
        if (op == 1)
        {
                sum = a+=b;
        }
        else if (op == 2)
        {
                sum = a-=b;
        }
        else if (op == 3)
        {
                sum = a*=b;
        }
        else if (op == 4)
        {
                sum = a/=b;
        }
        else
        {
                printf("Invalid operation");
                return;
        }
        char ca;
        calagain:
                printf("%d\n", sum);
                printf("Would you like to calculate again? y/n:");
                scanf(" %c", &ca);
                if (ca == 'y' || ca == 'Y')
                {
                        a,b,sum = 0;
                        system("clear");
                        calculator();
                }
                else if (ca == 'n' || ca == 'N')
                {
                        desktop();
                }
                else
                {
                        return;
                }
}
void desktop()
{
        int sel;
        printf("--Desktop--\n[1] Calculator\n[2] SysInfo\n[3] Console\n");
        scanf("%d", &sel);
        if (sel == 1)
        {
                system("clear");
                calculator();
        }
        else if (sel == 2)
        {
                system("clear");
                sysinfo();
        }
        else if (sel == 3)
        {
                system("clear");
                printf("--Console--\n");
                console();
        }
}
void sysinfo()
{
        printf("Current version: %s\n", VERSION);
        printf("Programs: %s\n", PROGRAMS);
        desktop();
}
void console()
{
        char command[20];
        scanf("%19s", command);
        if (strcmp(command, "help") == 0)
        {
                printf("Available commands:\nhelp\ndesktop\ncalculator\nsysinfo\nclear\n");
                return console();
        }
        else if (strcmp(command, "desktop") == 0)
        {
                system("clear");
                desktop();
        }
        else if (strcmp(command, "calculator") == 0)
        {
                system("clear");
                calculator();
        }
        else if (strcmp(command, "sysinfo") == 0)
        {
                printf("Current version: %s\n", VERSION);
                printf("Programs: %s\n", PROGRAMS);
                return console();
        }
        else if (strcmp(command, "clear") == 0)
        {
                system("clear");
                return console();
        }
        else
        {
                printf("Unknown command. Type 'help' for available commands");
                return console();
        }
}
