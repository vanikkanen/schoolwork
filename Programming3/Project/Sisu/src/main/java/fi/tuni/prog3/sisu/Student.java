package fi.tuni.prog3.sisu;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.util.Arrays;
import java.util.Collections;



/**
 * A class for representing a student.
 * @author Lauri
 */
public class Student {

    // public for objectMapper
    public String name;
    public String degree;
    public ArrayList<Integer> courses = new ArrayList<>();

    /**
     * Empty Student constructor that is never called but cannot be removed
     * because objectMapper needs it.
     */
    public Student() {

    }

    /**
     * Constructs a new student
     * @param name the name of the new student.
     * @param degree the degree of the new student.
     * @param courses the courses completed by the student.
     */
    public Student(String name, String degree, Integer[] courses){
        this.name = name;
        this.degree = degree;
        System.out.println(Arrays.toString(courses));
        Collections.addAll(this.courses, courses);
    }

    /**
     * Saves the student as a json file.
     * @throws IOException
     */
    public void saveStudent() throws IOException{
        ObjectMapper mapper = new ObjectMapper();
        mapper.writeValue(new File("students\\" + name + ".json"), this);
    }
}