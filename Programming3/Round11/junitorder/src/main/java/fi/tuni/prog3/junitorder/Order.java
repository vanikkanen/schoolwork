/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */
package fi.tuni.prog3.junitorder;

/**
 *
 * @author vanik
 */
import java.util.*;

public class Order {

    private HashMap<String,Entry> order;
    
    public Order() {
        order = new HashMap<>();
    }
    
    public boolean addItems(Item item, int count) throws IllegalArgumentException {
        
    }
    
    public boolean addItems(String name, int count) throws IllegalArgumentException, NoSuchElementException {
        
    }
    
    public List<Entry> getEntries() {
        
    }
    
    public int getEntryCount() {
        
    }
    
    public int getItemCount() {
    
    }
    
    public double getTotalPrice() {
        
    }
    
    public boolean isEmpty() {
        
    }
    
    public boolean removeItems(String name, int count) throws IllegalArgumentException, NoSuchElementException {
        
    }
    
    
    public static class Item extends Object {
        
        private String name;
        private double price;
        
        public Item(String name, double price) throws IllegalArgumentException {
            
            if (name == null || price < 0) {
                throw new IllegalArgumentException();
            }
            
            this.name = name;
            this.price = price;
        }
        
        public String getName() {
            return name;
        }
        
        public double getPrice() {
            return price;
        }
        
        @Override
        public String toString() {
            return(String.format("Item(%s,%.2f)", name, price));
        }
        
        public boolean equals(Item other) {
            return(other.getName().equals(name));
        }       
    }
    
    public static class Entry extends Object {
        
        private Item item;
        private int count;
        
        public Entry(Item item, int count) throws IllegalArgumentException {
            
            if (count < 0) {
                throw new IllegalArgumentException();
            }
            
            this.item = item;
            this.count = count;
            
        }
        
        public String getItemName() {
            return item.getName();
        }
        
        public double getUnitPrice() {
            return item.getPrice();
        }
        
        public Item getItem() {
            return item;
        }
        
        public int getCount() {
            return count;
        }
        
        @Override
        public String toString() {
            return(String.format("%d units of %s", count, item.getName()));
        }
    } 
}
