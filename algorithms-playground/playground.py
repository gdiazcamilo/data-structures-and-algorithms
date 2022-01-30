class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        primal_matrix = mat
        new_matrix_row_count = r
        new_matrix_column_count = c
        
        if not self.__is_legal_transformation(primal_matrix, new_matrix_row_count, new_matrix_column_count):
            return primal_matrix
    
        new_matrix = [[]]
        new_matrix_row_idx = 0
        new_matrix_column_idx = 0
        max_index_per_row = new_matrix_column_count - 1
        for primal_row in primal_matrix:
            for element in primal_row:
                if new_matrix_column_idx > max_index_per_row:
                    new_matrix.append([])
                    new_matrix_column_idx = 0
                    new_matrix_row_idx += 1
    
                new_matrix[new_matrix_row_idx].append(element)
                new_matrix_column_idx += 1
        
        return new_matrix
    
    
    def __is_legal_transformation(self, primal_matrix, new_matrix_row_count, new_matrix_column_count):
        """
            Determines if the transformation is possible.
            
            Transformation is possible when the two matrix have the same number of elements.
        """
        primal_matrix_element_count = len(primal_matrix) * len(primal_matrix[0])
        new_matrix_element_count = new_matrix_row_count * new_matrix_column_count
        is_legal = primal_matrix_element_count == new_matrix_element_count
        return is_legal

s = Solution()
print(s.matrixReshape([[1,2], [3,4]], 4, 1))