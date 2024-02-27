/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */

/**
 *
 * @author vanik
 */
public class ValueNode extends Node {
    
    private Object value;

    ValueNode(double value) {
        this.value = value;
    }
    ValueNode(String value) {
        this.value = value;
    }
    ValueNode(boolean value) {
        this.value = value;
    }

    public boolean isNumber() {
        return value instanceof Double;
        }
    
    public boolean isBoolean() {
        return value instanceof Boolean;
        }
    
    public boolean isString() {
        return value instanceof String;
        }
    
    public boolean isNull() {
        return (value == null);
        }
    
    public double getNumber() {
        return (Double) value;
    }
    
    public boolean getBoolean() {
        return (Boolean) value;
    }
    
    public String getString() {
        return (String) value;
    }
    
}
