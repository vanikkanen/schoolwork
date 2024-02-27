/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/UnitTests/JUnit5TestClass.java to edit this template
 */
package fi.tuni.prog3.junitorder;

import java.util.*;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 *
 * @author vanik
 */
public class OrderTest {
    
    @Test
    public void testOrderConstructor() {
        Order instance = new Order();
        assertTrue(instance.isEmpty());
    }
    
    
    /**
     * Test of addItems method, of class Order.
     */
    @Test
    public void testAddItems_OrderItem_int() {
        System.out.println("addItems");
        Order.Item item = new Order.Item("Testi", 1.00);
        int count = 1;
        Order instance = new Order();
        boolean expResult = true;
        boolean result = instance.addItems(item, count);
        assertEquals(expResult, result);
        
        instance.addItems(item, 4);
        int expResult2 = 5;
        int result2 = instance.getItemCount();
        assertEquals(expResult2, result2);
        
        Order.Item item2 = new Order.Item("Testi2", 1.00);
        instance.addItems(item2, 5);
        int expResult3 = 2;
        int result3 = instance.getEntryCount();
        assertEquals(expResult3,result3);
        
    }
    
    @Test
    public void testAddItems_OrderItem_Throws() {
        System.out.println("addItemsThrows");
        Order.Item item = new Order.Item("Testi", 1.00);
        int count = -1;
        Order instance = new Order();
        Exception expResult = new IllegalArgumentException();
        Exception result = assertThrows(IllegalArgumentException.class, () -> {
            instance.addItems(item, count);
        });
        assertEquals(expResult.getClass(), result.getClass());
        
        Order.Item item1 = new Order.Item("Testi", 1.00);
        Order.Item item2 = new Order.Item("Testi", 2.00);
        Order instance1 = new Order();
        
        Exception expResult1 = new IllegalStateException();
        instance1.addItems(item1, 1);
        
        Exception result1 = assertThrows(IllegalStateException.class, () -> {
           instance1.addItems(item2, 1);
        });
        assertEquals(expResult1.getClass(), result1.getClass());   
    }

    /**
     * Test of addItems method, of class Order.
     */
    @Test
    public void testAddItems_String_int() {
        System.out.println("addItems");
        
        Order.Item item = new Order.Item("Testi", 1.00);
        Order instance = new Order();
        instance.addItems(item, 1); 
        boolean expResult = true;
        boolean result = instance.addItems("Testi", 1);
        assertEquals(expResult, result);
        int expResult2 = 2;
        int result2 = instance.getItemCount();
        assertEquals(expResult2, result2);
        
        Order instance2 = new Order();
        instance2.addItems(item, 0);
        assertTrue(instance2.isEmpty());
    }
    
    @Test
    public void testAddItems_String_Throws() {
        System.out.println("addItemsThrows");
        Order.Item item = new Order.Item("Testi", 1.00);
        int count = -1;
        Order instance = new Order();
        Exception expResult = new IllegalArgumentException();
        Exception result = assertThrows(IllegalArgumentException.class, () -> {
            instance.addItems("Testi", count);
        });
        assertEquals(expResult.getClass(), result.getClass());
        
        Order instance1 = new Order();
        Exception expResult1 = new NoSuchElementException();
        Exception result1 = assertThrows(NoSuchElementException.class, () -> {
            instance1.addItems("Testi", 1);
        });
        assertEquals(expResult1.getClass(), result1.getClass());
        
        Order.Item item2 = new Order.Item("Testi", 1.00);
        Order instance2 = new Order();
        instance2.addItems(item2, 1);
        Exception expResult2 = new NoSuchElementException();
        Exception result2 = assertThrows(NoSuchElementException.class, () -> {
            instance1.addItems("Testi1", 1);
        });
        assertEquals(expResult2.getClass(), result2.getClass());
    }

    /**
     * Test of getEntriies method, of class Order.
     */
    @Test
    public void testGetEntries() {
        System.out.println("getEntries");
        Order instance = new Order();
        List<Order.Entry> expResult = new ArrayList<>();
        List<Order.Entry> result = instance.getEntries();
        assertEquals(expResult, result);
        
        Order.Item item = new Order.Item("Testi", 1.00);
        instance.addItems(item, 1);
        List<Order.Entry> expResult1 = new ArrayList<>();
        expResult1.add(new Order.Entry(item, 1));
        List<Order.Entry> result1 = instance.getEntries();
        assertEquals(expResult1.get(0).getCount(), result1.get(0).getCount());
        assertEquals(expResult1.get(0).getItem(), result1.get(0).getItem());
    }

    /**
     * Test of getEntryCount method, of class Order.
     */
    @Test
    public void testGetEntryCount() {
        System.out.println("getEntryCount");
        Order instance = new Order();
        int expResult = 0;
        int result = instance.getEntryCount();
        assertEquals(expResult, result);
        
        Order.Item item = new Order.Item("Testi", 1.00);
        instance.addItems(item, 1);
        int expResult1 = 1;
        int result1 = instance.getEntryCount();
        assertEquals(expResult1, result1);
    }

    /**
     * Test of getItemCount method, of class Order.
     */
    @Test
    public void testGetItemCount() {
        System.out.println("getItemCount");
        Order instance = new Order();
        int expResult = 0;
        int result = instance.getItemCount();
        assertEquals(expResult, result);

        Order.Item item = new Order.Item("Testi", 1.00);
        instance.addItems(item, 1);
        Order.Item item2 = new Order.Item("Testi2", 1.50);
        instance.addItems(item2, 4);
        
        int expResult1 = 5;
        int result1 = instance.getItemCount();
        assertEquals(expResult1, result1);
    }

    /**
     * Test of getTotalPrice method, of class Order.
     */
    @Test
    public void testGetTotalPrice() {
        System.out.println("getTotalPrice");
        Order instance = new Order();
        double expResult = 0.0;
        double result = instance.getTotalPrice();
        assertEquals(expResult, result, 0.0);

        Order.Item item1 = new Order.Item("Testi1", 1.00);
        instance.addItems(item1, 2);
        Order.Item item2 = new Order.Item("Testi2", 3.00);
        instance.addItems(item2, 1);
        double expResult1 = 5.0;
        double result1 = instance.getTotalPrice();
        assertEquals(expResult1, result1);
    }

    /**
     * Test of isEmpty method, of class Order.
     */
    @Test
    public void testIsEmpty() {
        System.out.println("isEmpty");
        Order instance = new Order();
        boolean expResult = true;
        boolean result = instance.isEmpty();
        assertEquals(expResult, result);

        Order.Item item = new Order.Item("Testi", 1.00);
        instance.addItems(item, 1);
        boolean expResult1 = false;
        boolean result1 = instance.isEmpty();
        assertEquals(expResult1, result1);
        
        instance.removeItems("Testi", 1);
        assertTrue(instance.isEmpty());
        
    }

    /**
     * Test of removeItems method, of class Order.
     */
    @Test
    public void testRemoveItems() {

        Order instance1 = new Order();
        Order.Item item = new Order.Item("Testi", 1.00);
        instance1.addItems(item, 1);
        boolean test1 = instance1.removeItems("Testi", 1);
        assertTrue(instance1.isEmpty());
        
        instance1.addItems(item, 3);
        boolean test2 = instance1.removeItems("Testi", 3);
        assertTrue(instance1.isEmpty());
        
        instance1.addItems(item, 5);
        boolean test3 = instance1.removeItems("Testi", 4);
        
        int result = instance1.getItemCount();
        int expResult = 1;
        
        assertEquals(expResult, result);
        assertTrue(test1);
        assertTrue(test2);
        assertTrue(test3);
    }
    
    @Test
    public void testRemoveItems_Throws() {
        System.out.println("removeItemsThrows");
        String name1 = "Testi";
        int count1 = 1;
        Order instance1 = new Order();
        Exception expResult1 = new NoSuchElementException();
        Exception result1 = assertThrows(NoSuchElementException.class, () -> {
            instance1.removeItems(name1, count1);
        });
        assertEquals(expResult1.getClass(), result1.getClass());
        
        Order instance2 = new Order();
        Order.Item item2 = new Order.Item("Testi", 1.00);
        instance2.addItems(item2, 1);
        String name2 = "Testi1";
        int count2 = 1;
        Exception expResult2 = new NoSuchElementException("The item was not found from the order!");
        Exception result2 = assertThrows(NoSuchElementException.class, () -> {
            instance2.removeItems(name2, count2);
        });
        assertEquals(expResult2.getClass(), result2.getClass());
        
        Order instance3 = new Order();
        Order.Item item3 = new Order.Item("Testi", 1.00);
        instance3.addItems(item3, 1);
        String name3 = "Testi";
        int count3 = 2;
        Exception expResult3 = new IllegalArgumentException();
        Exception result3 = assertThrows(IllegalArgumentException.class, () -> {
            instance3.removeItems(name3, count3);
        });
        assertEquals(expResult3.getClass(), result3.getClass());
        
        Order instance4 = new Order();
        Order.Item item4 = new Order.Item("Testi", 1.00);
        instance4.addItems(item2, 1);
        String name4 = "Testi";
        int count4 = -1;
        Exception expResult4 = new IllegalArgumentException();
        Exception result4 = assertThrows(IllegalArgumentException.class, () -> {
            instance4.removeItems(name4, count4);
        });
        assertEquals(expResult4.getClass(), result4.getClass());
    }
    
    // Order.Entry
    
    @Test
    public void EntryConstructorTest() {
        Order.Item item = new Order.Item("Testi", 1.00);
        Order.Entry entry = new Order.Entry(item, 1);
        String expResultName = "Testi";
        String resultName = entry.getItemName();
        assertEquals(expResultName, resultName);
        int expResultCount = 1;
        int resultCount = entry.getCount();
        assertEquals(expResultCount,resultCount);
        Order.Item expResultItem = item;
        Order.Item resultItem = entry.getItem();
        assertEquals(expResultItem, resultItem);
    }
    
    @Test
    public void EntryConstructorTest_Throws() {
        Order.Item item = new Order.Item("Testi", 1.00);
        
        Exception expResult = new IllegalArgumentException();
        Exception result = assertThrows(IllegalArgumentException.class, () -> {
            Order.Entry entry = new Order.Entry(item, -1);
        });
        assertEquals(expResult.getClass(),result.getClass());
    }
    
    @Test
    public void getItemName_Entry_Test() {
        
        Order.Item item = new Order.Item("Testi", 1.00);
        Order.Entry entry = new Order.Entry(item, 1);
        String expResult = "Testi";
        String result = entry.getItemName();
        assertEquals(expResult, result);
        
    }
    
    @Test
    public void getItem_Entry_Test() {
        Order.Item item = new Order.Item("Testi", 1.00);
        Order.Entry entry = new Order.Entry(item, 1);
        Order.Item expResult = item;
        Order.Item result = entry.getItem();
        assertEquals(expResult,result);
    }
    
    @Test
    public void getCount_Entry_Test() {
        Order.Item item = new Order.Item("Testi", 1.00);
        Order.Entry entry = new Order.Entry(item, 5);
        int expResult = 5;
        int result = entry.getCount();
        assertEquals(expResult,result);
    }
    @Test
    public void getUnitPrice_Entry_Test() {
        Order.Item item = new Order.Item("Testi", 1.50);
        Order.Entry entry = new Order.Entry(item, 10);
        double expResult = 1.50;
        double result = entry.getUnitPrice();
        assertEquals(expResult,result);
    }
    
    @Test
    public void toString_Entry_Test() {
        Order.Item item = new Order.Item("Testi", 1.50);
        Order.Entry entry = new Order.Entry(item, 5);
        String expResult = "5 units of Item(Testi, 1.50)";
        String result = entry.toString();
        assertEquals(expResult,result);
    }
    
    // Order.Item
    
    @Test
    public void ItemConstructorTest() {
        Order.Item item = new Order.Item("Testi", 1.50);
        String expResultName = "Testi";
        String resultName = item.getName();
        assertEquals(expResultName, resultName);
        double expResultPrice = 1.50;
        double resultPrice = item.getPrice();
        assertEquals(expResultPrice,resultPrice);
    }
    
    @Test
    public void ItemConstructorTest_Throws() {
        
        Exception expResultName = new IllegalArgumentException();
        Exception resultName = assertThrows(IllegalArgumentException.class, () -> {
            new Order.Item(null, 1.00);
        });
        assertEquals(expResultName.getClass(),resultName.getClass());
        
        Exception expResultPrice = new IllegalArgumentException();
        Exception resultPrice = assertThrows(IllegalArgumentException.class, () -> {
            new Order.Item("Testi", -1.00);
        });
        assertEquals(expResultPrice.getClass(),resultPrice.getClass());
    }
    
    @Test
    public void equals_Item_Test() {
        Order.Item item = new Order.Item("Testi", 1.00);
        Order.Item item3 = new Order.Item("Testi", 5.00);
        Order.Item item2 = new Order.Item("Testi2", 1.00);
        assertTrue(item.equals(item3));
        assertFalse(item.equals(item2)); 
    }
    @Test
    public void getName_Item_Test() {
        Order.Item item = new Order.Item("Testi", 1.00);
        String expResult = "Testi";
        String result = item.getName();
        assertEquals(expResult, result);
    }
    @Test
    public void getPrice_Item_Test() {
        Order.Item item = new Order.Item("Testi", 1.50);
        double expResult = 1.50;
        double result = item.getPrice();
        assertEquals(expResult, result);
    }
    @Test
    public void toString_Item_Test() {
        Order.Item item = new Order.Item("Testi", 1.50);
        String expResult = "Item(Testi, 1.50)";
        String result = item.toString();
        assertEquals(expResult,result);
    }
    
}
