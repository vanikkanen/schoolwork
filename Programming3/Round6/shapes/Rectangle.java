/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */

/**
 *
 * @author vanik
 */
public class Rectangle implements IShapeMetrics{

    private double height;
    private double width;
    
    Rectangle(double height, double width) {
        this.height = height;
        this.width = width;
    }
    
    public String toString() {
       return String.format("Rectangle with height %.2f and width %.2f", height, width);
    }
    
    @Override
    public String name() {
       return "rectangle";
    }
    
    @Override
    public double area() {
       return height*width;
    }
   
    @Override
    public double circumference() {
       return 2*height+2*width;
    }
     
}
