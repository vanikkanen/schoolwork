/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */

/**
 *
 * @author vanik
 */
import java.util.*;

public class ArrayNode extends Node implements Iterable<Node>{
    
    ArrayList<Node> array;
    
    ArrayNode() {
        array  = new ArrayList<>();
    }
    
    public void add(Node node) {
        array.add(node);
    }
    
    public int size() {
        return array.size();
    }
    
    @Override
    public Iterator<Node> iterator() {
        return array.iterator();
    }
}
