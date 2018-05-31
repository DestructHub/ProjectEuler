import std.stdio : writeln;
import std.algorithm : filter, sum;

enum int LIMIT = 50;

ulong[] _fibonacci() 
{
    ulong[] fib;
    fib.reserve(LIMIT);

    fib ~= 1;
    fib ~= 2;

    foreach (n; 2 .. LIMIT) 
        fib ~= fib[n-2] + fib[n-1];
    
    return fib;
}

void main() 
{
    ulong[] fibonacci = _fibonacci;

    ulong answer = sum(fibonacci.filter!(a => a % 2 == 0 && a < 4000000));
    
    writeln(answer);
}
