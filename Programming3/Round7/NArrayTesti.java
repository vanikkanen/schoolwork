/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */

/**
 *
 * @author vanik
 */
import java.util.*;

public class NArrayTesti {

    /**
     * @param args the command line arguments
     */
    private ArrayList<Integer> dimensions;
    
    public void main(String args[]) {
        int offset;
        dimensions = new ArrayList<>();
        dimensions.add(2);
        dimensions.add(4);
        dimensions.add(4);
        int[] test = {1, 2, 3};
        
        offset = arrayOffset(test, 1);
        
        System.out.println(offset);
        
    }
    
    
     private int arrayOffset(int[] indices, int index) {

        if (index == 0) {
            int offset = indices[index];
            return offset;
        }
        //System.out.print(indices[index] + " ");
        
        int offset = indices[index - 1] + dimensions.get(index)*arrayOffset(indices, index-1);
        
        //System.out.println(offset);
        
        return offset;     
    }
}
