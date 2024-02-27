/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/UnitTests/JUnit5TestClass.java to edit this template
 */
package fi.tuni.prog3.junitattainment;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 *
 * @author vanik
 */
public class AttainmentTest {
    
    public AttainmentTest() {
    }
    /*
    @BeforeAll
    public static void setUpClass() {
        
    }
    
    @AfterAll
    public static void tearDownClass() {
    }
    
    @BeforeEach
    public void setUp() {
    }
    
    @AfterEach
    public void tearDown() {
    }
    */
    /**
     * Test of getCourseCode method, of class Attainment.
     */
    @Test
    public void testGetCourseCode() {
        System.out.println("getCourseCode");
        Attainment instance = new Attainment("Koodi", "OpNum", 3);
        String expResult = "Koodi";
        String result = instance.getCourseCode();
        assertEquals(expResult, result);
    }
    
    /**
     * Test of getStudentNumber method, of class Attainment.
     */
    @Test
    public void testGetStudentNumber() {
        System.out.println("getStudentNumber");
        Attainment instance = new Attainment("Koodi", "OpNum", 3);
        String expResult = "OpNum";
        String result = instance.getStudentNumber();
        assertEquals(expResult, result);
    }

    /**
     * Test of getGrade method, of class Attainment.
     */
    @Test
    public void testGetGrade() {
        System.out.println("getGrade");
        Attainment instance = new Attainment("Koodi", "OpNum", 3);
        int expResult = 3;
        int result = instance.getGrade();
        assertEquals(expResult, result);
    }
    
    /**
     * Test if the constructor throws an exception
     */
    @Test
    public void testExceptionThrown() {
        System.out.println("whenExceptionThrown");
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            new Attainment(null, null, 6);
        });
        Exception expException = new IllegalArgumentException();
        assertEquals(expException.getClass(), exception.getClass());
    }

    /**
     * Test of toString method, of class Attainment.
     */
    @Test
    public void testToString() {
        System.out.println("toString");
        Attainment instance = new Attainment("Koodi", "OpNum", 3);
        String expResult = "Koodi OpNum 3";
        String result = instance.toString();
        assertEquals(expResult, result);
    }

    /**
     * Test of compareTo method, of class Attainment.
     */
    @Test
    public void testCompareTo() {
        System.out.println("compareTo");
        Attainment other1 = new Attainment("Koodi", "OpNum", 3);
        Attainment instance1 = new Attainment("Koodi", "OpNum", 3);
        int expResult1 = 0;
        int result1 = instance1.compareTo(other1);
        assertEquals(expResult1, result1);
        
        Attainment other2 = new Attainment("Koodi", "OpNum", 3);
        Attainment instance2 = new Attainment("Koodi", "OpNum1", 3);
        int expResult2 = 1;
        int result2 = instance2.compareTo(other2);
        assertEquals(expResult2, result2);
        
        Attainment other3 = new Attainment("Koodi", "OpNum", 3);
        Attainment instance3 = new Attainment("Koodi1", "OpNum", 3);
        int expResult3 = 1;
        int result3 = instance3.compareTo(other3);
        assertEquals(expResult3, result3);
         
    }
    
}
