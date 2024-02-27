package fi.tuni.prog3.sisu;

import java.util.HashSet;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;


/**
 * Checks that the get-methods work correctly
 * @author vanik
 */
public class CourseTest {

    /**
     * Test of getCode method, of class Course.
     */
    @Test
    public void testGetCode() {
        System.out.println("getCode");
        Course instance = new Course("Testi_koodi", "Testi_nimi", 5, "Testi_info");
        String expResult = "Testi_koodi";
        String result = instance.getCode();
        assertEquals(expResult, result);
    }

    /**
     * Test of getName method, of class Course.
     */
    @Test
    public void testGetName() {
        System.out.println("getName");
        Course instance = new Course("Testi_koodi", "Testi_nimi", 5, "Testi_info");
        String expResult = "Testi_nimi";
        String result = instance.getName();
        assertEquals(expResult, result);
    }

    /**
     * Test of getCredits method, of class Course.
     */
    @Test
    public void testGetCredits() {
        System.out.println("getCredits");
        Course instance = new Course("Testi_koodi", "Testi_nimi", 5, "Testi_info");
        int expResult = 5;
        int result = instance.getCredits();
        assertEquals(expResult, result);
    }

//    /**
//     * Test of getPeriod method, of class Course.
//     */
//    @Test
//    public void testGetPeriod() {
//        System.out.println("getPeriod");
//        Course instance = new Course("Testi_koodi", "Testi_nimi", 5, "Testi_info");
//        int expResult = 1;
//        int result = instance.getPeriod();
//        assertEquals(expResult, result);
//    }

    /**
     * Test of getInfo method, of class Course.
     */
    @Test
    public void testGetInfo() {
        System.out.println("getInfo");
        Course instance = new Course("Testi_koodi", "Testi_nimi", 5, "Testi_info");
        String expResult = "Testi_info";
        String result = instance.getInfo();
        assertEquals(expResult, result);
    }
    
    @Test
    public void testGetId(){
        
        System.out.println("getId");
        Course instance = new Course("Testi_koodi", "Testi_nimi", 5, "Testi_info");
        instance.setId(2245);
        int expResult = 2245;
        int result = instance.getId();
        assertEquals(expResult, result);
        
    }
}
