#include <stdio.h>

typedef unsigned char byte;

typedef enum {
    IP4_CLASS_A,
    IP4_CLASS_B,
    IP4_CLASS_C,
} IPv4_class_t;

typedef union __attribute__((packed))
{
   struct
   {
       byte b0;
       byte b1;
       byte b2;
       byte b3;
   };

   int packed;
} IPv4_t;

IPv4_t subnetmask_machine(IPv4_t network, IPv4_t netmask, int machines)
{

}

int main(int argc, char** argv)
{
    IPv4_t ip = (IPv4_t){{161, 25, 0, 0}};
    IPv4_t mask = (IPv4_t){{255, 255, 0, 0}};
    
    IPv4_t subnet = (IPv4_t){{}};

    int subnet_count = 10; 
}
