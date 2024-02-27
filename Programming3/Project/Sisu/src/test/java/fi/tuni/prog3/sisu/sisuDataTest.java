/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/UnitTests/JUnit5TestClass.java to edit this template
 */
package fi.tuni.prog3.sisu;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 *
 * @author Lauri
 */
public class sisuDataTest {
    
    /**
     * Test of sisuData constructor, of class sisuData. Tests that the sisuData
     * object created is not null.
     * @throws IOException 
     */
    @Test
    public void sisuDataTest() throws IOException {
        
        System.out.println("sisuData");
        sisuData result = new sisuData();
        
        sisuData expResult = null;
        
        assertNotEquals(expResult, result);
    }
    
    /**
     * Test of getDegrees method, of class sisuData.
     */
    @Test
    public void testGetDegrees() throws IOException {
        
        sisuData SD = new sisuData();
        
        System.out.println("getDegrees");
        
        List<String> expResult = Arrays.asList(
                "Akuuttilääketieteen erikoislääkärikoulutus (55/2020)", 
                "Biolääketieteen tekniikan tohtoriohjelma",
                "Ympäristö- ja energiatekniikan DI-ohjelma");
        List<String> result = SD.getDegrees();
        result = Arrays.asList(
                result.get(0),
                result.get(10),
                result.get(result.size()-1));
        assertEquals(expResult, result);
    }
    /**
     * Test of fetchData method, of class sisuData. Tests if fetchData finds
     * available degrees.
     */
    @Test
    public void testFetchData() throws IOException{
    
         System.out.println("fetchData");
         
         sisuData instance = new sisuData();
         
         List<String> degreesFound = instance.getDegrees();
        
         int result = degreesFound.size();
         
         int expResult = 0;
         
         assertTrue(expResult < result);
         
    }

    /**
     * Test of getModule method, of class sisuData. Tests if modules are found 
     * correctly.
     */
    @Test
    public void testGetModuleModules() throws Exception {
        
        System.out.println("getModule: modules");
        String DegreeProgrammeName = "Automaatiotekniikan DI-ohjelma";
        sisuData instance = new sisuData();
        Module module = instance.getModule(DegreeProgrammeName);
        
        ArrayList<String> expResult = new ArrayList<>(
        Arrays.asList("Automaation tietotekniikka",
                "Factory Automation and Industrial Informatics",
                "Robotics",
                "Systeemien hallinta",
                "Älykkäät työkoneet",
                "Älykäs automaatio"));
        ArrayList<Module> modules =
                new ArrayList<>(module.getModules().values());
        
        ArrayList<String> result = new ArrayList<>();
        
        for(Module x : modules){
            
            result.add(x.getName());
        }

        assertEquals(expResult, result);
        
    }
    /**
     * Test of getModule method, of class sisuData. Tests if courses are found
     * correctly.
     */
    @Test
    public void testGetModuleCourses() throws Exception {
        
        System.out.println("getModule: courses");
        String DegreeProgrammeName = "Automaatiotekniikan DI-ohjelma";
        sisuData instance = new sisuData();
        Module module = instance.getModule(DegreeProgrammeName);
        
        ArrayList<String> expResult = new ArrayList<>(
        Arrays.asList(
                "Automaation ohjelmistot ja verkot",
                "Johdanto hahmontunnistukseen ja koneoppimiseen",
                "Web Development 2 - Architecting"));
        
        module = module.getModules().get("Automaation tietotekniikka");
        module = module.getModules()
                .get("Automaation tietotekniikan syventävät opinnot");
        ArrayList<Course> courses = 
                new ArrayList<>(module.getCourses().values());

        ArrayList<String> result = new ArrayList<>();
        
        result.add(courses.get(0).getName());
        result.add(courses.get(10).getName());
        result.add(courses.get(courses.size() - 1).getName());
        
        
        assertEquals(expResult, result);
        
    }
}
