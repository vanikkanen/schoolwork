/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */

/**
 *
 * @author vanik
 */
import java.util.*;

public class StudentRegister {

    private ArrayList<Student> students = new ArrayList<>();
    private ArrayList<Course> courses = new ArrayList<>();
    private TreeMap<String, ArrayList<Attainment>> register = new TreeMap<>();
    
    public StudentRegister() {
        
    }
    
    public ArrayList<Student> getStudents() {
        students.sort(Comparator.comparing(Student::getName));
        return students;
    }
    
    public ArrayList<Course> getCourses() {
        courses.sort(Comparator.comparing(Course::getName));
        return courses;
    }
    
    public void addStudent(Student student) {
        students.add(student);
    }
    
    public void addCourse(Course course) {
        courses.add(course);
    }
    
    public void addAttainment(Attainment att) {
        
        String studentNumber = att.getStudentNumber();
        
        if (register.containsKey(studentNumber)) {
            register.get(studentNumber).add(att);
        }
        else {
            ArrayList<Attainment> attainments = new ArrayList<>();
            attainments.add(att);
            register.put(studentNumber, attainments);
        }
    }

    public void printStudentAttainments(String studentNumber, String order) {
        
        if (!register.containsKey(studentNumber)) {
            System.out.print("Unknown student number: " + studentNumber);
        }
        else {
            String name = "";
            for (Student student : students) {
                if(student.getStudentNumber() == studentNumber) {
                    name = student.getName();
                }
            }

            System.out.println(name + " (" + studentNumber + "):");
            ArrayList<Attainment> to_print = new ArrayList<>(register.get(studentNumber));
            
                if ("by name".equals(order)) {
                    
                    ArrayList<Course> byName = new ArrayList<>(courses);
                    byName.sort(Comparator.comparing(Course::getName));
                    ArrayList<String> sortedCoursesCodes = new ArrayList<>();
                    for (Course c : byName) {
                        sortedCoursesCodes.add(c.getCode());
                    }
                    
                   to_print.sort(Comparator.comparing((Attainment a) -> sortedCoursesCodes.indexOf(a.getCourseCode()))); 
                }
                
                else if ("by code".equals(order)) {
                    to_print.sort(Comparator.comparing(Attainment::getCourseCode));
                }
                
            String courseCode;
            String courseName = "";
            for (Attainment next : to_print) {
                courseCode = next.getCourseCode(); 
                for (Course course : courses) {
                   if (courseCode.equals(course.getCode())) {
                       courseName = course.getName();
                   }
               }
               System.out.println("  " + courseCode + " " + courseName + ": " + next.getGrade());
            }
                
        } 
    }

    public void printStudentAttainments(String studentNumber){
        
        if (!register.containsKey(studentNumber)) {
            System.out.println("Unknown student number: " + studentNumber);
        }
        else {
            String name = "";
            for (Student student : students) {
                if(student.getStudentNumber() == studentNumber) {
                    name = student.getName();
                }
            }
            
            System.out.println(name + " (" + studentNumber + "):");
            ArrayList<Attainment> to_print = register.get(studentNumber);
            
            String courseCode;
            String courseName = "";
            
            for (Attainment next : to_print) {
                courseCode = next.getCourseCode(); 
                for (Course course : courses) {
                   if (courseCode.equals(course.getCode())) {
                       courseName = course.getName();
                   }
               }
               System.out.println("  " + courseCode + " " + courseName + ": " + next.getGrade());
            }
        }
    }
}
