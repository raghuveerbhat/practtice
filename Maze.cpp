#include <iostream>
#include<iomanip>
using namespace std;

const int D = 10;


void printPath(int path[D][D], int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cout<<setw(3)<<path[i][j]<<" ";
        }
        cout<<endl;
    }
}

bool solve(int board[D][D], int n, int x, int y, int path[D][D]){
    
    if(x<0 || x>=n || y<0 || y>=n || board[x][y] == 0 || path[x][y] == 1)
        return false;
    path[x][y]=1;
    if(x==n-1 && y==n-1)
        return true;
    //left
    if(solve(board,n,x-1,y,path)){
        //path[x][y]=0;
        return true;
    }
    //right
    if(solve(board,n,x+1,y,path)){
        //path[x][y]=0;
        return true;
    }
    //top
    if(solve(board,n,x,y-1,path)){
       // path[x][y]=0;
        return true;}
    //bottom
    if(solve(board,n,x,y+1,path)){
        //path[x][y]=0;
        return true;
    }
    path[x][y]=0;
    return false;
        
}

int main() {
    int board[D][D] = {{1,1,1},{1,0,0},{1,1,1}};
    int path[D][D] = {0};
    int n=3;
    bool ans = solve(board,n,0,0,path);
    printPath(board,n);
    cout<<endl<<endl;
    if(ans == true)
        printPath(path,n);
    else
        cout<<"Not possible!";
    return 0;
}
