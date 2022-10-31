class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
      //        loop over the matrix
        for (int i = 0; i < matrix.length-1; ++i)
//            loop over nested arrays
            for (int j = 0; j < matrix[i].length-1; ++j)
//                check if the current element is equal to the element in the next row and next column
                if (matrix[i][j] != matrix[i+1][j+1])
                    return false;
        return true; 
    }
}