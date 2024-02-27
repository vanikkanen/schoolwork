/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */

/**
 *
 * @author vanik
 */
public class Student {

    private String name;
    private String stdntNro;
    
    public Student (String name, String studentNumber) {
     this.name = name;
     this.stdntNro = studentNumber;
    }
    
    public String getName() {
        return name;
    }
    
    public String getStudentNumber() {
        return stdntNro;
    }
}
