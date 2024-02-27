/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */

/**
 *
 * @author vanik
 */
public class Attainment {

    private String courseCode;
    private String studentNumber;
    private int grade;
    
   public Attainment(String courseCode, String studentNumber, int grade) {
       this.courseCode = courseCode;
       this.studentNumber = studentNumber;
       this.grade = grade;
   }
   
   public String getCourseCode() {
       return courseCode;
   }
   
    public String getStudentNumber() {
        return studentNumber;
   }
    
    public int getGrade() {
        return grade;
    }
    
}
