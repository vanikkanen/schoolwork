/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */
package com.mycompany.sevenzipsearch;

/**
 *
 * @author vanik
 */
import java.util.*;
import java.io.*;
import org.apache.commons.compress.archivers.sevenz.*;

public class ZipSearch {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException {

        String filename = args[0];
        String keyWord = args[1];
        
        SevenZFile sevenZFile = new SevenZFile(new File(filename));
        SevenZArchiveEntry entry;
             
        while((entry = sevenZFile.getNextEntry()) != null) {
            String name = entry.getName();
            
            if(name.endsWith(".txt")) {
                System.out.println(name);
                
                byte[] content = new byte[(int) entry.getSize()];
                int readBytes;
                
                while((readBytes = sevenZFile.read(content)) != -1) {
                    ByteArrayOutputStream data = new ByteArrayOutputStream();
                    data.write(content, 0, readBytes);
                    String file = data.toString("UTF-8");
                    
                    String[] lines = file.split("\\n");
                    int index = 1;
                    for(var line : lines) {
                        if(line.toUpperCase().contains(keyWord.toUpperCase())) {
                            var words = line.split(" ");
                            
                            System.out.print(index + ":");
                            for(String word : words) {
                                if(!word.toUpperCase().contains(keyWord.toUpperCase())) {
                                    System.out.print(" " + word);
                                }
                                else {
                                    int startIndex = word.toUpperCase().indexOf(keyWord.toUpperCase());
                                    int endIndex = startIndex + keyWord.length()-1;
                                    String printWord = "";
                                    for(int i = 0; i < word.length(); ++i) {
                                        if(i < startIndex || i > endIndex) {
                                            printWord += word.charAt(i);
                                        }
                                        else {
                                            printWord += word.toUpperCase().charAt(i);
                                        }
                                    }
                                    System.out.print(" " + printWord);

                                }
                                
                            }
                            System.out.print("\n");
                        }
                        ++index;
                    }
                }
                System.out.println("");
            }
        }
        sevenZFile.close();
    }
}
