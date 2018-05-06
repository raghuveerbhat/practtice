#include <iostream>
#include<iomanip>
using namespace std;

const int D = 10;

bool canPlace(int board[D][D], int n, int r, int c, int num){
    if(board[r][c] != 0)return false;
    for(int k=0;k<n;k++){
        if(board[r][k] == num) return false;
        if(board[k][c] == num) return false;
    }
    
    int rowStart = r-r%3;
    int colStart = c-c%3;
    for(int i=rowStart; i<rowStart+3; i++){
        for(int j=colStart; j<colStart+3; j++){
            if(board[i][j] == num) return false;
        }
    }
    return true;
}

void printBoard(int board[D][D], int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cout<<setw(3)<<board[i][j]<<" ";
        }
        cout<<endl;
    }
}

bool solve(int board[D][D], int n, int r, int c){
    
    if(r==n){
        return true;
    }
    
    if(c==n){
        return solve(board,n,r+1,0);
    }
    
    if(board[r][c]!=0)
        return solve(board,n,r,c+1);
    
    for(int i=1;i<=9;i++){
        if(canPlace(board,n,r,c,i)){
            board[r][c]=i;
            bool success = solve(board,n,r,c+1);
            if(success)return true;
            board[r][c]=0;
        }
    }
    return false;
}

int main() {
    int board[D][D] = {{3, 0, 6, 5, 0, 8, 4, 0, 0},
                      {5, 2, 0, 0, 0, 0, 0, 0, 0},
                      {0, 8, 7, 0, 0, 0, 0, 3, 1},
                      {0, 0, 3, 0, 1, 0, 0, 8, 0},
                      {9, 0, 0, 8, 6, 3, 0, 0, 5},
                      {0, 5, 0, 0, 9, 0, 6, 0, 0},
                      {1, 3, 0, 0, 0, 0, 2, 5, 0},
                      {0, 0, 0, 0, 0, 0, 0, 7, 4},
                      {0, 0, 5, 2, 0, 6, 3, 0, 0}};
    int n;cin>>n;
    bool ans = solve(board,n,0,0);
    if(ans == true)
        printBoard(board,n);
    else
        cout<<"Not possible!";
    return 0;
}
