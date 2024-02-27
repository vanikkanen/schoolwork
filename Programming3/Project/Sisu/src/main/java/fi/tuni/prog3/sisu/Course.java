package fi.tuni.prog3.sisu;

/**
 * A class for representing a course
 */
public class Course {

    private String code;
    private String name;
    private int credits;
    private int id;
    private String info = "Ei kurssi kuvausta / No course info";
    
    /**
     * Constructs a new course.
     * @param code the new courses code.
     * @param name the new courses name.
     * @param credits the new courses credits.
     * @param info the new courses information.
     */
    public Course(String code, String name, int credits, String info) {
        this.code = code;
        this.name = name;
        this.credits = credits;
        if (info != "") {
            this.info = info;
        }
    }
    
    /**
     * Returns a String of courses code.
     * @return a String of courses code.
     */
    public String getCode() {
        return code;
    }
    
    /**
     * Returns a String of courses name.
     * @return a String of courses name.
     */
    public String getName() {
        return name;
    }
    
    /**
     * Returns integer of courses credits.
     * @return integer of courses credits.
     */
    public int getCredits() {
        return credits;
    }
    
    /**
     * Returns a String of course information.
     * @return a String of course information.
     */
    public String getInfo() {
        return info;
    }
    
    /**

     * Returns an int that is the courses id.
     * @return an int that is the courses id.
     */
    public int getId() {
        return id;
    }
    
    /**
     * Sets an int that is the courses id.
     * @param id an int that is the courses id.
     */
    public void setId(int id) {
        this.id = id;
    } 
}