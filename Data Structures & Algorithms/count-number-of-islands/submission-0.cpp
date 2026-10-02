class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int count= 0;
        for (int i = 0; i < grid.size(); i++ ){
            for (int j =0; j <grid[i].size(); j++){
                if (grid[i][j] == '1'){
                    destroyIsland(grid, i,j);
                    count++;
                }
            }
        }
        return count;
    }
    void destroyIsland(vector<vector<char>>& grid, int row, int col){
        if (row < 0 || row >= grid.size() ||
            col < 0 || col >= grid[0].size() ||
            grid[row][col] == '0') {
         return;
        }else{
            grid[row][col] = '0';

            destroyIsland(grid, row+1, col);
            destroyIsland(grid, row-1, col);
            destroyIsland(grid, row, col+1);
            destroyIsland(grid, row, col-1);
        }

    }
};
