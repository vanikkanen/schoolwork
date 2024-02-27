/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */

/**
 *
 * @author vanik
 */
import java.util.*;
import java.time.*;
import java.time.format.*;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;

public class Dates {

    public static class DateDiff {
        
        private LocalDate start;
        private LocalDate end;
        private int diff = 0;
        
        private DateDiff (LocalDate start, LocalDate end) {
   
            this.start = start;
            this.end = end;
            
            diff = (int)ChronoUnit.DAYS.between(start, end);
        }
        
        public String getStart() {
            return start.toString();
        }
        public String getEnd() {
            return end.toString();
        }
        public int getDiff() {
            return diff;
        }
        public String toString() {
            int start_day = start.getDayOfMonth();
            int start_month = start.getMonthValue();
            int start_year = start.getYear();
            
            int end_day = end.getDayOfMonth();
            int end_month = end.getMonthValue();
            int end_year = end.getYear();
            
            return String.format("%s %02d.%02d.%d --> %s %02d.%02d.%d: %d days", start.getDayOfWeek().name().substring(0,1).toUpperCase() + start.getDayOfWeek().name().substring(1).toLowerCase(), start_day, start_month, start_year, end.getDayOfWeek().name().substring(0,1).toUpperCase() + end.getDayOfWeek().name().substring(1).toLowerCase(), end_day, end_month, end_year, diff);
        }
    }
    
    public static DateDiff[] dateDiffs(String ...dateStrs) throws DateTimeException {
        
        ArrayList<LocalDate> ok_dates = new ArrayList<>();
        
        DateTimeFormatter[] formats = {DateTimeFormatter.ofPattern("d.M.uuuu"), DateTimeFormatter.ofPattern("uuuu-MM-dd")};

        for (String day_string : dateStrs) {
            try {
                LocalDate date = null;
                for (var format : formats) {
                    try {
                        date = LocalDate.parse(day_string, format.withResolverStyle(ResolverStyle.STRICT));
                    } 
                    catch(DateTimeException e) {
                    }
                }
                if(date == null) {
                    throw new DateTimeException("");
                }
                
                int day = date.getDayOfMonth();
                int month = date.getMonthValue();
                int year = date.getYear();
                
                if (year < 1000 || year > 9999 ) {
                        throw new DateTimeException("");
                    }
                 
                LocalDate new_date = LocalDate.of(year, month, day);
                
                ok_dates.add(new_date);
            }
            catch(DateTimeException e) {
                Character sidemark = '"';
                System.out.format("The date %s%s%s is illegal!%n", sidemark, day_string, sidemark);
            }
        }            
        
        Collections.sort(ok_dates);
        
        if (ok_dates.size() < 2) {
            return new DateDiff[0];
        }
        
        else {
            ArrayList<DateDiff> dd = new ArrayList<>();
            
            for (int i = 0; i < ok_dates.size()-1; ++i) {
                DateDiff new_dd = new DateDiff(ok_dates.get(i), ok_dates.get(i+1));
                dd.add(new_dd);
            }
            
            DateDiff[] return_array = new DateDiff[dd.size()];
            return dd.toArray(return_array);
        }
}
    /*
    //Testi varten
    public static void main(String args[]) {
        
    String[] test = {"1.08.2016","07.3.2004","31.05.2022","29.2.2015","2017-11-23","7.04.2019","2000-3-6","2009-05-13","1.01.850"};
    Dates.DateDiff[] diffArray = {};
    if(args.length == 2) {
      diffArray = Dates.dateDiffs(args[0], args[1]);
    }
    else {
      diffArray = Dates.dateDiffs(test);
    }
    for(Dates.DateDiff dd : diffArray) {
      System.out.format("start: %s end: %s diff: %d%n",
              dd.getStart(), dd.getEnd(), dd.getDiff());
      System.out.println("  " + dd);
    }
  }
*/
    
}
