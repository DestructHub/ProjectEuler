import std.stdio : writeln;

void main() 
{
    int total;

    foreach (n; 1..1000) {
        if (n % 3 == 0 || n % 5 == 0)
            total+=n;
    }

    writeln(total);
}
