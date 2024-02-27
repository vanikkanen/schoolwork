/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */
package fi.tuni.prog3.round8.jsoncountries;

/**
 *
 * @author vanik
 */
import com.google.gson.*;
import java.io.*;
import java.nio.file.*;
import java.nio.charset.*;
import java.util.*;

public class CountryData {

    public static List<Country> readFromJsons(String areaFile, String populationFile, String gdpFile) {

        HashMap<String, ArrayList<String>> data = new HashMap<>();

        String[] files = {areaFile, populationFile, gdpFile};

        for (var file : files) {
            try {

                Path path = Paths.get(file);
                Reader reader = Files.newBufferedReader(path, StandardCharsets.UTF_8);

                JsonParser parser = new JsonParser();
                JsonElement element = parser.parse(reader);
                JsonObject jobject = element.getAsJsonObject();
                jobject = jobject.getAsJsonObject("Root");
                jobject = jobject.getAsJsonObject("data");
                JsonArray fields = jobject.getAsJsonArray("record");

                for (var field : fields) {
                    JsonArray values = field.getAsJsonObject().getAsJsonArray("field");
                    String name = values.get(0).getAsJsonObject().getAsJsonPrimitive("value").toString();
                    String info = values.get(2).getAsJsonObject().getAsJsonPrimitive("value").toString();

                    name = name.substring(1, name.length() - 1);
                    info = info.substring(1, info.length() - 1);

                    if (!data.containsKey(name)) {
                        data.put(name, new ArrayList<>());
                    }
                    data.get(name).add(info);
                }
            } catch (Exception e) {
                System.out.println(e);
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

    public static void writeToJson(List<Country> countries, String countryFile) {
        
        try {
            Writer writer = new FileWriter(countryFile);
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            gson.toJson(countries, writer);
            writer.close();
        }
        catch (Exception e){
            System.out.println(e);
        }
        
        
    }
    
}
