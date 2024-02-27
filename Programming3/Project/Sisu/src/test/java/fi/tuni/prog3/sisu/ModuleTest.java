/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/UnitTests/JUnit5TestClass.java to edit this template
 */
package fi.tuni.prog3.sisu;

import java.util.TreeMap;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 *
 * @author vanik
 */
public class ModuleTest {
    
    /**
     * Test of addCourse method, of class Module.
     */
    @Test
    public void testAddGetCourse() {
        System.out.println("addCourse");
        String name = "Testi_moduuli_nimi";
        Course course = new Course("Testi_kurssi_koodi", "Testi_kurssi_nimi", 5, "Testi_kurssi_info");
        String courseName = course.getName();
        Module instance = new Module(name, 20);
        instance.addCourse(courseName, course);
        
        assertEquals(course.getClass(),instance.getCourses().get(courseName).getClass());
        
    }

    /**
     * Test of addModule method, of class Module.
     */
    @Test
    public void testAddGetModule() {
        System.out.println("addModule");
        String name = "Testi_moduuli_nimi";
        Module module = new Module(name, 20);
        Module instance = new Module(name, 20);
        instance.addModule(name, module);
        
        assertEquals(module.getClass(), instance.getModules().get(name).getClass());
        
    }

    /**
     * Test of addInfo method, of class Module.
     */
    @Test
    public void testAddGetInfo() {
        System.out.println("addInfo");
        String info = "Testi_info";
        String name = "Testi_moduuli_nimi";
        Module instance = new Module(name, 20);
        instance.addInfo(info);
        
        String expResult = "Testi_info";
        String result = instance.getInfo();
        assertEquals(expResult, result);

    }

    /**
     * Test of getName method, of class Module.
     */
    @Test
    public void testGetName() {
        System.out.println("getName");
        String name = "Testi_moduuli_nimi";
        Module instance = new Module(name, 20);
        String expResult = name;
        String result = instance.getName();
        assertEquals(expResult, result);
    }

    /**
     * Test of getCredits method, of class Module.
     */
    @Test
    public void testGetCredits() {
        System.out.println("getCredits");
        String name = "Testi_moduuli_nimi";
        Module instance = new Module(name, 20);
        int expResult = 20;
        int result = instance.getCredits();
        assertEquals(expResult, result);
    }
    
}
