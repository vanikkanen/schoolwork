/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/UnitTests/JUnit5TestClass.java to edit this template
 */
package fi.tuni.prog3.sisu;

import java.util.ArrayList;
import java.util.Arrays;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 *
 * @author Lauri
 */
public class StudentTest {
    
    /**
     * Test of Student constructor , of class Student. Tests that parameters are
     * stored correctly.
     */
    @Test
    public void StudentTest() {
        Integer[] courses = {1, 2, 3};
        ArrayList<Integer> expCourses = new ArrayList<>(
            Arrays.asList(1,
                          2,
                          3));
        Student result = new Student("matti", "Automaatiotekniikan DI-Ohjelma",
                courses);
        
        assertEquals("matti",result.name);
        assertEquals("Automaatiotekniikan DI-Ohjelma",result.degree);
        assertEquals(expCourses,result.courses);
    }
}
