#import <Foundation/Foundation.h>

int main (int argc, const char * argv[])
{
   NSAutoreleasePool * pool = [[NSAutoreleasePool alloc] init];
   NSInteger sum = 0;
   NSInteger i;
   for (i = 0; i < 1000; i++)
      if (i % 5 == 0 || i % 3 == 0)
        sum += i;
   
   NSLog (@"%lu", sum);
   [pool drain];
   return 0;
}
