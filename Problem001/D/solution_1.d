import std.stdio;

int main()
{
    int i, total = 0;

    for (i = 0; i < 1000; i++)
    {
        if (i % 3 == 0 || i % 5 == 0)
            total += i;
    }
    writeln(total);
    return 0;
}
