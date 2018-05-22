#include <iostream>
#include<fstream>
#include<stdlib.h>
#include<stdio.h>
#include<time.h>
#define UNASSIGNED 0
#define size 9
using namespace std;
int sum=0;
bool fault[9][9]={false};


class Sudoku
{
    int grid[size][size];
    bool isSafe(int row, int col, int num); //To check whether the element is inserted in the right place
    bool InRow(int row, int num);//To check whether element to be inserted is already present in the row or not
    bool InBox(int boxStartRow, int boxStartCol, int num);//To check whether element to be inserted is already present in the box or not
    bool InCol(int col, int num);//To check whether element to be inserted is already present in the column or not
    public:
        void clear_fault();
        Sudoku(int b[9][9]); //To initialize the grid
        bool FindUnassignedLocation(int &row, int &col); //Find a location in grid which is empty
        bool SolveSudoku();//To solve the Sudoku
        void replace_ele(int,int,int);//To replace the empty space by the number entered by user
        void printGrid();//To print the required grid
};

void Sudoku::clear_fault()
{
    for (int i = 0; i < size; i++)
        for ( int j= 0; j <size; j++)
            if (fault[i][j])
                grid[i][j]=0;
}

void Sudoku::replace_ele(int a,int b,int num)
{
    if(fault[a-1][b-1]==true)
        grid[a-1][b-1]=num;
    if(!isSafe(a-1,b-1,num) && grid[a-1][b-1]==0)
        fault[a-1][b-1]=true;
    else fault[a-1][b-1]=false;
    if(grid[a-1][b-1]==0)
        grid[a-1][b-1]=num;
}

Sudoku::Sudoku(int b[9][9])
{
    for(int i=0;i<9;i++)
        for(int j=0;j<9;j++)
            grid[i][j]=b[i][j];
}

bool Sudoku::SolveSudoku()
{
    int row, col;
    if (!FindUnassignedLocation(row, col))
        return true;
    for (int num = 1; num <= 9; num++)
    {
        if (isSafe(row, col, num))
        {
            grid[row][col] = num;
            if (SolveSudoku())
                return true;
            grid[row][col] = UNASSIGNED;
        }
    }
    return false;
}

bool Sudoku::FindUnassignedLocation(int &row, int &col)
{
    for (row = 0; row < size; row++)
        for (col = 0; col <size; col++)
            if (grid[row][col] == UNASSIGNED )
                return true;
    return false;
}

bool Sudoku::InRow(int row, int num)
{
    for (int col = 0; col < size; col++)
        if (grid[row][col] == num)
            return true;
    return false;
}

bool Sudoku::InCol(int col, int num)
{
    for (int row = 0; row < size; row++)
        if (grid[row][col] == num)
            return true;
    return false;
}

bool Sudoku::InBox(int boxStartRow, int boxStartCol, int num)
{
    for (int row = 0; row < 3; row++)
        for (int col = 0; col < 3; col++)
            if (grid[row+boxStartRow][col+boxStartCol] == num)
                return true;
    return false;
}

bool Sudoku::isSafe(int row, int col, int num)
{
    return !InRow(row, num) && !InCol(col, num) && !InBox(row - row % 3 , col - col % 3, num);
}

void clean()
{
    system("clear");
}
void Sudoku::printGrid()
{
    sum+=(grid[0][0]*100 + grid[0][1]*10 + grid[0][2]);
}


int main()
{
    fstream ifile;
    int t=50;
    int x=0,y=0,choose;
    ifile.open("sudo.txt",ios::in);
    int a[9][9],n,posx,posy;
    srand(time(NULL));
    if(!ifile)
    {
        cout<<"File not found !!";
    }
    else
    while(t--){
        char ch;
        string line;
        getline(ifile,line);
        for(int i=0;i<9;++i){
            for(int j=0;j<9;j++){
                    ifile.get(ch);
                    a[i][j]=(int)ch - 48;
            }
            ifile.get(ch);
        }
        Sudoku b(a);
        if (b.SolveSudoku() == true)
            b.printGrid();
        else
            printf("No solution exists");
    }
    cout<<sum;
    return 0;
}
