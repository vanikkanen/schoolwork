package fi.tuni.prog3.sisu;

import java.util.*;

/**
 * a Class for representing Modules in the degree.
 * @author vanik
 */
public class Module {

    private String name;
    private int credits;
    private String info = "Ei moduuli kuvausta / No module info";
    private String groupId;
    
    private TreeMap<String, Course> courses;
    private TreeMap<String, Module> modules;
    
    /**
     * Constructs a new Module.
     * @param name name of the module.
     * @param credits credits for the module.
     */
    public Module(String name, int credits) {
        this.name = name;
        this.credits = credits;
        courses = new TreeMap<>();
        modules = new TreeMap<>();
    }
    
    /**
     * Adds a course to the module.
     * @param name name of the Course.
     * @param course Course representation of the course.
     */
    public void addCourse(String name, Course course) {     
        courses.put(name, course);  
    }
    
    /**
     * Adds a module to the module.
     * @param name name of the module.
     * @param module Module representation of the module.
     */
    public void addModule(String name, Module module) {
        modules.put(name, module);
    }
    
    /**
     * Adds info text of the module.
     * @param info text giving information about the module.
     */
    public void addInfo(String info) {
        this.info = info;
    }
    
    /**
     * Adds group id to the module.
     * @param groupId the groupId of to module.
     */
    public void addGroupId(String groupId) {
        this.groupId = groupId;
    }
    
    /**
     * Returns a TreeMap of the courses in the module.
     * @return a TreeMap of the courses in the module.
     */
    public TreeMap<String, Course> getCourses() {
        return courses;
    }
    
    /**
     * Returns a TreeMap of the modules in the module.
     * @return a TreeMap of the modules in the module.
     */
    public TreeMap<String, Module> getModules() {
        return modules;
    }
    
    /**
     * Returns the name of the module.
     * @return the name of the module.
     */
    public String getName() {
        return name;
    }
    
    /**
     * Returns the credits of the module.
     * @return the credits of the module.
     */
    public int getCredits() {
        return credits;
    }
    
    /**
     * Returns text giving information about the module.
     * @return text giving information about the module.
     */
    public String getInfo() {
        return info;
    }
    
    /**
     * Returns the group id of the module.
     * @return the group id of the module.
     */
    public String getGroupId() {
        return groupId;
    }
}
