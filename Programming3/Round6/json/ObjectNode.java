
/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */

/**
 *
 * @author vanik
 */

import java.util.*;

public class ObjectNode extends Node implements Iterable<String> {

    private TreeMap<String, Node> json;
    
    ObjectNode() {
        json  = new TreeMap<>();
    }
    
    public Node get(String key) {
        
        if (json.containsKey(key)) {
            return json.get(key);
        }
        else {
            return null;
        }  
    }
    
    public void set(String key, Node node) {     
        json.put(key, node);   
    }
    
    public int size() {    
        return json.size();    
    }
    
    @Override
    public Iterator<String> iterator() {
        return json.keySet().iterator();
    }
     
}
