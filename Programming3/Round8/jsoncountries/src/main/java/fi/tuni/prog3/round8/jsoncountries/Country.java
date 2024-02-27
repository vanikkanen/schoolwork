/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */
package fi.tuni.prog3.round8.jsoncountries;

/**
 *
 * @author vanik
 */
public class Country implements Comparable<Country> {
    
    private String name;
    private double area;
    private long population;
    private double gdp;
    
    Country (String name, double area, long population, double gdp) {
        this.name = name;
        this.area = area;
        this.population = population;
        this.gdp = gdp;
    }
    
    public String getName() {
        return name;
    }  
    public double getArea() {
        return area;
    }   
    public long getPopulation() {
        return population;
    }
    public double getGdp() {
        return gdp;
    }
    
    public String toString() {
        String s = String.format("%s%n", name);
        s += String.format("  Area: %.1f km2%n", area);
        s += String.format("  Population: %d%n", population);
        s += String.format("  GDP: %.1f (2015 USD)%n", gdp);
        return s;
    }
          
    @Override
    public int compareTo(Country other) {
        int cmp = name.compareTo(other.name);
        return cmp;
    }
    
}
