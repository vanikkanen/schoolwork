/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */

/**
 *
 * @author vanik
 */
import java.util.*;

public class Sudoku {
    
    private final HashMap<Integer, HashMap<Integer, Character>> sudoku_grid = new HashMap();
    private final HashSet<Character> legal = new HashSet();
    
    public Sudoku() {
        legal.addAll((Arrays.asList
        (' ', '1', '2', '3', '4', '5', '6', '7', '8', '9')));
        for (int i = 0; i < 9; i++) {
            // Making the grid a row at a time
            HashMap column = new HashMap();
            for (int j = 0; j < 9; j++) {
                // Making the columns to the row
                column.put(j, ' ');
            }
            sudoku_grid.put(i, column);
        }
    }
    
    public void set(int i, int j, char c) {
       
        if (i >= 0 && i < 9 && j >= 0 && j < 9) {
            if (legal.contains(c)){
                sudoku_grid.get(i).put(j, c);
            }
            else {
                System.out.format("Trying to set illegal character "+ c +" to ("+ i+ ", " +j + ")!%n");
            }
        }
        else {
            System.out.format("Trying to access illegal cell (" + i +", "+ j +")!%n");
        }
    }
    
    public void print() {
        int count_y = 1;
        int count_x = 1;
        System.out.format("#####################################%n");
        for (int i = 0; i < 9; i++) {
            System.out.format("#");
            
            for (int j = 0; j < 9; j++) {
                char c = sudoku_grid.get(i).get(j);
                
                char mark = '|';
                if (count_y == 3){
                    mark = '#';
                    count_y = 0;
                }
                count_y++;
                System.out.format(" %s %s", c, mark);
            }
            System.out.format("%n");
            
            String separator = "#---+---+---#---+---+---#---+---+---#%n";
            if (count_x == 3){
                separator = "#####################################%n";
                count_x = 0;
            }
            count_x++;
            System.out.format(separator);
        }
    }
    
    public boolean check() {
        
        HashSet<Character> check = new HashSet<>();
        
        // Row check

        for (int i = 0; i < 9; i++) {
            check.clear();

            for (int j = 0; j < 9; j++) {
                
                char c;
                c = sudoku_grid.get(i).get(j);

                if (!check.contains(c)) {
                    if (c != ' ') {
                        check.add(c);
                    }
                }
                else {
                    System.out.println("Row " + i + " has multiple " + c + "'s!");
                    return false;
                }
            }
        }
        // Column check
        
            for (int j = 0; j < 9; j++) {
                check.clear();
                for (int i = 0; i < 9; i++) {
                    char c = sudoku_grid.get(i).get(j);
                    if (check.contains(c)) {
                        System.out.println("Column " + j + " has multiple " + c + "'s!");
                        return false;
                    }
                    else if (c != ' ') {
                        check.add(c);
                    }
                }
            }
        // Box check
        
            for (int Y = 0; Y < 9; Y += 3) {
                for (int X = 0; X < 9; X += 3) {
                    check.clear();
                    
                    for (int i = X; i < X+3; i++) {
                        for (int j = Y; j < Y+3; j++) {
                            
                            char c = sudoku_grid.get(i).get(j);
                            
                            if (check.contains(c)) {
                                System.out.println("Block at (" + X + ", " + Y + ") has multiple " + c + "'s!");
                                return false;
                            }
                            
                            else if (c != ' ') {
                                check.add(c);
                            }
                            
                        }
                    }
                }
            }
        return true;
    }
}

    
