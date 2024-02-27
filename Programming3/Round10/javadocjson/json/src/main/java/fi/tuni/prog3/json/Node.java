
package fi.tuni.prog3.json;

/**
 * An abstract super class for different types of JSON nodes.
 */
public abstract class Node {
    
    /**
     * The only constructor. Will be invoked, usually implicitly, by subclass constructors.
     */
    protected Node() {
    }
    
    /**
     * Checks whether this node represents a JSON object.
     * @return true if this node represent a JSON object, otherwise false.
     */
    public boolean isObject() {
      return this instanceof ObjectNode;
    }
    
    /**
     * Checks whether this node represents a JSON array.
     * @return true if this node represent a JSON array, otherwise false.
     */
    public boolean isArray() {
      return this instanceof ArrayNode;
      }
    
    /**
     * Checks whether this node represents a JSON value.
     * @return true if this node represent a JSON value, otherwise false.
     */
    public boolean isValue() {
      return this instanceof ValueNode;
    }




  
}
