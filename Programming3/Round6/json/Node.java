import java.lang.*;

public abstract class Node {
  public boolean isValue() {
    return this instanceof ValueNode;
  }

  public boolean isArray() {
    return this instanceof ArrayNode;
  }

  public boolean isObject() {
    return this instanceof ObjectNode;
  }
  
  public void printSimple() {
    StringBuilder sb = new StringBuilder();
    printSimple(this, sb);
    System.out.print(sb.toString());
  }
  
  public void printJson() {
      int indent = 0;
      boolean isArray = false;
      StringBuilder sb = new StringBuilder();
      printJson(this, sb, indent, isArray);
      System.out.print(sb.toString());
  }
  
  public void printJson(Node node, StringBuilder sb, int indent, boolean isArray) {
    //throw new UnsupportedOperationException("printJson has not been implemented!");

    if(node.isObject()) {
        if(sb.toString().endsWith(NL)){
            sb.append("  ".repeat(indent));
        }
        sb.append("{");

        ObjectNode objNode = (ObjectNode) node;
        
        if(objNode.size() > 0) {
            sb.append(NL);
        }
        
        for (String name : objNode) {
            sb.append("  ".repeat(indent+1)).append("\"").append(name).append("\"").append(": ");
            printJson(objNode.get(name), sb, indent+1, false);
        }
        
        if (objNode.size() > 0) {
            sb.setLength(sb.length() - 2);
            sb.append(NL).append("  ".repeat(indent));
        }
        sb.append("}");
        
        if(indent > 0) {
            sb.append(",").append(NL);
        }
    }
    
    else if(node.isArray()) {
        sb.append("[");
        ArrayNode arrNode = (ArrayNode) node;
        
        if (arrNode.size() > 0) {
            sb.append(NL);
        }
        for(Node aNode : arrNode) {
            printJson(aNode, sb, indent+1, true);
        }
        if (arrNode.size() > 0) {
            sb.setLength(sb.length() - 2);
            sb.append(NL).append("  ".repeat(indent));
        }
        sb.append("]");
        
        if(indent > 0) {
            sb.append(",").append(NL);
        }
    }
    
    else if (node.isValue()) {
        ValueNode valNode = (ValueNode) node;
        
        String valStr = "null";
        
        if (isArray) {
            sb.append("  ".repeat(indent));
        }
        
        if(valNode.isNumber()) {
          valStr = numberToString(valNode.getNumber());
        }
        
        else if(valNode.isBoolean()) {
          valStr = Boolean.toString(valNode.getBoolean());
        }
        
        else if(valNode.isString()) {
          valStr = "\"" + valNode.getString() + "\"";
        }
        
        sb.append(String.format("%s,%n", valStr));
    } 
 }

  private static final String NL = System.lineSeparator();

  private static String numberToString(Double d) {
    String str = Double.toString(d);
    if(str.endsWith(".0")) {
      str = str.substring(0, str.length() - 2);
    }
    return str;
  }

  private void printSimple(Node node, StringBuilder sb) {
    if(node.isObject()) {
      sb.append("ObjectNode").append(NL);
      ObjectNode objNode = (ObjectNode) node;
      for(String name : objNode) {
        sb.append(name).append(": ");
        printSimple(objNode.get(name), sb);
      }
    }
    else if(node.isArray()) {
      sb.append("ArrayNode").append(NL);
      ArrayNode arrNode = (ArrayNode) node;
      for(Node aNode : arrNode) {
        printSimple(aNode, sb);
      }
    }
    else if(node.isValue()) {
      ValueNode valNode = (ValueNode) node;
      String typeStr = "NullValue";
      String valStr = "null";
      if(valNode.isNumber()) {
        typeStr = "NumberValue";
        valStr = numberToString(valNode.getNumber());
      }
      else if(valNode.isBoolean()) {
        typeStr = "BooleanValue";
        valStr = Boolean.toString(valNode.getBoolean());
      }
      else if(valNode.isString()) {
        typeStr = "StringValue";
        valStr = "\"" + valNode.getString() + "\"";
      }
      sb.append(String.format("%s(%s)%n", typeStr, valStr));
    }
  }
}
