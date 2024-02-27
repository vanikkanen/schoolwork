/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */

/**
 *
 * @author vanik
 */
public class Circle implements IShapeMetrics {

   private double radius;
   
   Circle(double radius) {
       this.radius = radius;
   }
   
   public String toString() {
       return String.format("Circle with radius: %.2f", radius);
   }
   
   @Override
   public String name() {
       return "circle";
   }
   
   @Override
   public double area() {
       return PI*radius*radius;
   }
   
   @Override
   public double circumference() {
       return 2*PI*radius;
   }
   
}
