/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */

/**
 *
 * @author vanik
 */
import java.util.*;

public class NdArray<E> extends AbstractCollection<E>{
    
    private ArrayList<Integer> dimensions;
    private int N;
    private int size = 1;
    private Object[] nArray;
    
    
    NdArray(Integer firstDimLen, Integer ...furtherDimLens) {
             
        if (firstDimLen < 0) {
            throw new NegativeArraySizeException("Illegal dimension size "+ firstDimLen +".");
        }
        dimensions = new ArrayList<>();
        dimensions.add(firstDimLen);
        size = firstDimLen;
        
        for (var dim : furtherDimLens) {
            if (dim < 0) {
                throw new NegativeArraySizeException("Illegal dimension size "+ dim +".");
            }
            dimensions.add(dim);
            size = size*dim;
        }
        N = dimensions.size();
        nArray = new Object[size];
    }

    private int arrayOffset( int index, int... indices) {
        if (index == 0) {
            int offset = indices[index];
            return offset;
        }

        int offset = indices[index] + dimensions.get(index)*arrayOffset(index-1, indices);
          
        return offset;     
    }
 
    
    @Override
    public int size() {
         return size;
    }
    
    @SuppressWarnings("unchecked")
    public E get(int... indices) {
        
        if (indices.length != N) {
            throw new IllegalArgumentException("The array has " + N + " dimensions but " + indices.length + " indices were given.");
        }
        
        for(int i = 0; i < indices.length; ++i) {
            if (indices[i] < 0 || indices[i] > dimensions.get(i)) {
                throw new IndexOutOfBoundsException("Illegal index " +  indices[i]  + " for dimension " + i + " of length " + dimensions.get(i) + ".");
            }
        }
        
        int offset = arrayOffset(N-1, indices);
        return (E) nArray[offset];  
    }
    
    @SuppressWarnings("unchecked")
    public void set(E item, int... indices) {
        
        if (indices.length != N) {
            throw new IllegalArgumentException("The array has " + N + " dimensions but " + indices.length + " indices were given.");
        }
        
        for(int i = 0; i < indices.length; ++i) {
            if (indices[i] < 0 || indices[i] >= dimensions.get(i)) {
                throw new IndexOutOfBoundsException("Illegal index " +  indices[i]  + " for dimension " + (i+1) + " of length " + dimensions.get(i) + ".");
            }
        }

        int offset = arrayOffset(N-1, indices);
        nArray[offset] = item;
    }
     
    public int[] getDimensions() {
        int[] dims = dimensions.stream().mapToInt(i -> i).toArray();
        return dims;
    }
    
    @Override
    public Iterator<E> iterator(){
        return new NAIterator();
    }

    private class NAIterator implements Iterator<E> {
        
       private int pos = 0;
       
       @Override
       public boolean hasNext() {
           return pos < size;
       }
       
       @Override
       @SuppressWarnings("unchecked")
       public E next() {
          if (pos >= size) {
             throw new NoSuchElementException("No more values in the array!"); 
          }
          return (E) nArray[pos++];
       }

    }
    
}
