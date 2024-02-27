/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */

/**
 *
 * @author vanik
 */
import java.util.*;

public class Attainment implements Comparable<Attainment>{
    
    private String courseCode;
    private String studentNumber;
    private int grade;
    
    Attainment(String courseCode, String studentNumber, int grade) {
              
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
    
    @Override
    public String toString() {
       return String.format("%s %s %d%n", courseCode, studentNumber, grade);
    }
    
    @Override
    public int compareTo(Attainment other) {
        int cmp = studentNumber.compareTo(other.studentNumber);
        if (cmp == 0) {
            cmp = courseCode.compareTo(other.courseCode);
        }
        return cmp;
    }
    
    public static final Comparator<Attainment> CODE_STUDENT_CMP = new Comparator<Attainment>() {
        @Override
        public int compare(Attainment a, Attainment b) {
            int cmp = a.getCourseCode().compareTo(b.getCourseCode());
                if (cmp == 0) {
                    cmp = a.getStudentNumber().compareTo(b.getStudentNumber());
                }
            return cmp;
        }
    };
    
    public static final Comparator<Attainment> CODE_GRADE_CMP = new Comparator<Attainment>() {
        @Override
        public int compare(Attainment a, Attainment b) {
            int cmp = a.getCourseCode().compareTo(b.getCourseCode());
                if (cmp == 0) {
                    cmp = -Integer.compare(a.getGrade(), b.getGrade());
                }
            return cmp;
        }
    };
    
}
