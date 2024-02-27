/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */
package fi.tuni.prog3.round8.xmlcountries;

/**
 *
 * @author vanik
 */
import java.io.*;
import java.util.*;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.jdom2.*;
import org.jdom2.input.*;
import org.jdom2.output.*;

public class CountryData {

    public static List<Country> readFromXmls(String areaFile, String populationFile, String gdpFile) {
               
        HashMap<String, ArrayList<String>> data = new HashMap<>();
        
        String[] files = {areaFile, populationFile, gdpFile};
        
        for (String file : files) {
            try {
                SAXBuilder sax = new SAXBuilder();
                Document doc = sax.build(new File(file));
                Element rootNode = doc.getRootElement();
                Element dataE = rootNode.getChild("data");
                List<Element> list = dataE.getChildren("record");
                
                for (Element record : list) {
                    List<Element> info = record.getChildren();
                    
                    String name = info.get(0).getText();
                    String value = info.get(2).getText();
                    
                    if (!data.containsKey(name)) {
                        data.put(name, new ArrayList<>());
                    }
                    data.get(name).add(value);
                    
                }
            }
            
            catch(IOException | JDOMException e) {
                System.out.println("ReadError");
            }
        }
        
        List<Country> countries = new ArrayList<>();
        
        for (var entry : data.entrySet()) {
            countries.add(new Country(entry.getKey(),
                Double.parseDouble(entry.getValue().get(0)),
                Long.parseLong(entry.getValue().get(1)),
                Double.parseDouble(entry.getValue().get(2))));
        }
            
        return countries;
    }
    
    public static void writeToXml(List<Country> countries, String countryFile) {
        
        
        StringBuilder s = new StringBuilder();

        s.append("<countries>");

        for (Country country : countries) {

            s.append("<country>");

            s.append("<name>");
            s.append(country.getName());
            s.append("</name>");

            s.append("<area>");
            s.append(country.getArea());
            s.append("</area>");

            s.append("<population>");
            s.append(country.getPopulation());
            s.append("</population>");

            s.append("<gdp>");
            s.append(country.getGdp());
            s.append("</gdp>");

            s.append("</country>");
        }

        s.append("</countries>");
        
        String text = s.toString();

        SAXBuilder sb = new SAXBuilder();
        Document doc = null; 
        
        try {

            doc = sb.build(new StringReader(text));

            XMLOutputter xmlOutputter = new XMLOutputter(Format.getPrettyFormat());
            xmlOutputter.output(doc, new FileOutputStream(countryFile));
            
        } catch (JDOMException ex) {
            Logger.getLogger(CountryData.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(CountryData.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
