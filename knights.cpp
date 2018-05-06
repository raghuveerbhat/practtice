#include <iostream>
#include<iomanip>
using namespace std;

const int D = 8;

bool canPlace(int board[D][D], int n, int r, int c){
    return (r>=0 && r<n && c>=0 && c<n && board[r][c]==0);
}

void printBoard(int board[D][D], int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cout<<setw(3)<<board[i][j]<<" ";
        }
        cout<<endl;
    }
}

bool solve(int board[D][D], int n, int moves, int cr, int cc){
    if(moves == n*n)
        return true;
    int rowDir[] = {+2,+2,+1,+1,-2,-2,-1,-1};
    int colDir[] = {+1,-1,+2,-2,+1,-1,+2,-2};
    for(int i=0;i<8;i++){
        int nr = cr + rowDir[i];
        int nc = cc + colDir[i];
        if(canPlace(board,n,nr,nc)==true){
            board[nr][nc]=moves+1;
            bool isans = solve(board,n,moves+1,nr,nc);
            if(isans==true)return true;
            board[nr][nc]=0;
        }
    }
    return false;
}

int main() {
    int board[D][D] = {0};
    int n;
    cin>>n;
    board[0][0]=1;
    bool ans = solve(board,n,1,0,0);
    if(ans == true)
        printBoard(board,n);
    else
        cout<<"Not possible!";
    return 0;
}
