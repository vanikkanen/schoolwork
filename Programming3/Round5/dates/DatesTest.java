/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */

/**
 *
 * @author vanik
 */
public class DatesTest {
  public static void main(String args[]) {
    Dates.DateDiff[] diffArray = {};
    if(args.length == 2) {
      diffArray = Dates.dateDiffs(args[0], args[1]);
    }
    else {
      diffArray = Dates.dateDiffs(args);
    }
    for(Dates.DateDiff dd : diffArray) {
      System.out.format("start: %s end: %s diff: %d%n",
              dd.getStart(), dd.getEnd(), dd.getDiff());
      System.out.println("  " + dd);
    }
  }
}
