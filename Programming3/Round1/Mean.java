/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */

/**
 *
 * @author vanik
 */
public class Mean {

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        int nums = 0;
        double sum = 0;
        double d;
        
        for (String s: args){
            d = Double.parseDouble(s);
            nums++;
            sum += d;
        }
        double avg = sum/nums;
        System.out.print("Mean: " + avg);
        // TODO code application logic here
    }
}
