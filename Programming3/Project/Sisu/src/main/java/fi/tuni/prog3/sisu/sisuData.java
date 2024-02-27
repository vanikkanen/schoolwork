package fi.tuni.prog3.sisu;

import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.Scanner;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.google.gson.JsonSyntaxException;
import java.util.ArrayList;
import java.util.List;
import java.util.TreeMap;
import javafx.util.Pair;
import org.jsoup.Jsoup;


/**
 * A class for storing data from sisu API.
 * @author Lauri
 */

public class sisuData {
    
    private String filler = "XXXXXXX";
    
    private String degreesAddress = "https://sis-tuni.funidata.fi/kori/api/"
            + "module-search?curriculumPeriodId=uta-lvv-2021&universityId=tuni-"
            + "university-root-id&moduleType=DegreeProgramme&limit=1000";
    
    private String moduleByGId = "https://sis-tuni.funidata.fi/kori/api/"
            + "modules/v1/by-group-id?groupId="
            + filler
            + "&universityId"
            + "=tuni-university-root-id&curriculumPeriodId=uta-lvv-2021"
            + "&preferByState=true";
    
    private String courseByGId = "https://sis-tuni.funidata.fi/kori/api/course-"
            + "units/v1/by-group-id?groupId="
            + filler
            + "&universityId=tuni-university-root-id&"
            + "curriculumPeriodId=uta-lvv-2021&preferByState=true";
    
    
    private JsonObject degreesJson;
    private TreeMap<String, Module> modules = new TreeMap<>();
    private int courseId = 0;
    private boolean dataFound = true;
    
    
    /**
     * Constructor for sisuData.
     */
    sisuData(){
        
        try{
            URL url = new URL(degreesAddress);
            Scanner scanner = new Scanner(url.openStream(), "UTF-8");
            String response = scanner.useDelimiter("\\Z").next();
            degreesJson = new JsonParser().parse(response).getAsJsonObject();
            scanner.close();
            fetchData();
        } catch(IOException e){
            dataFound = false;
        }
    }

    /**
     * Returns a list of degrees available.
     * @return a list of degrees available.
     */
    public List<String> getDegrees() {

        ArrayList<String> list = new ArrayList<>();

        JsonArray searchResults = degreesJson.getAsJsonArray("searchResults");

        for (var x : searchResults) {
            String n = x.getAsJsonObject().getAsJsonPrimitive("name")
                    .toString();
            n = n.substring(1, n.length() - 1);
            list.add(n);
        }
        return list;
    }
    
    /**
     * Private method called by constructor, creates module objects for all
     * degree's and places them in a TreeMap.
     */
    private void fetchData(){
        
        JsonArray searchResults = degreesJson.getAsJsonArray("searchResults");

        for (var x : searchResults) {

            String n = x.getAsJsonObject().getAsJsonPrimitive("name")
                    .toString();
            n = n.substring(1, n.length() - 1);

            String g = x.getAsJsonObject().getAsJsonPrimitive("groupId")
                    .toString();
            g = g.substring(1, g.length() - 1);

            JsonObject DegreeProgramme;
            try{
                URL url = new URL(moduleByGId.replace(filler, g));

                Scanner scanner = new Scanner(url.openStream(), "UTF-8");
                String response = scanner.useDelimiter("\\Z").next();
                JsonArray DegreeProgrammeArray = new JsonParser()
                        .parse(response).getAsJsonArray();
                DegreeProgramme = DegreeProgrammeArray.get(0)
                        .getAsJsonObject();
                scanner.close();
            } catch(JsonSyntaxException | IOException e){
                continue;
            }

            int credits = Integer.parseInt(DegreeProgramme
                    .getAsJsonObject("targetCredits").getAsJsonPrimitive("min").
                    toString());

            modules.put(n, new Module(n, credits));
            Module module = modules.get(n);
            module.addGroupId(g);

            String info = "No info provided";

            if (DegreeProgramme.has("learningOutcomes")
                    && !DegreeProgramme.get("learningOutcomes").isJsonNull()) {

                if (DegreeProgramme.getAsJsonObject("learningOutcomes")
                        .has("fi")) {

                    info = DegreeProgramme.getAsJsonObject("learningOutcomes")
                            .getAsJsonPrimitive("fi").toString();
                } else if (DegreeProgramme.getAsJsonObject("learningOutcomes")
                        .has("en")) {

                    info = DegreeProgramme.getAsJsonObject("learningOutcomes")
                            .getAsJsonPrimitive("en").toString();
                }
                info = info.substring(1, info.length() - 1);
                info = formatHtmlString(info);
                module.addInfo(info);
            }
        }
    }
    
    /**
     * Returns a module for a degree.
     * @param DegreeProgrammeName the name of the degree which module will be
     * returned.
     * @return the degrees module. 
     */
    
    public Module getModule(String DegreeProgrammeName){
        
        
        Module module = modules.get(DegreeProgrammeName);
        
        if(module.getModules().isEmpty()){
        
            try{
                URL url = new URL(moduleByGId.replace(filler,
                        module.getGroupId()));

                Scanner scanner = new Scanner(url.openStream(), "UTF-8");
                String response = scanner.useDelimiter("\\Z").next();
                JsonArray DegreeProgrammeArray = new JsonParser()
                        .parse(response).getAsJsonArray();
                JsonObject DegreeProgramme = DegreeProgrammeArray.get(0)
                        .getAsJsonObject();
                scanner.close();
                fillModule(module,DegreeProgramme);
            }
            catch(JsonSyntaxException | IOException e){
                return null;
            }

            

        }
        return module;
    }
    
    /**
     * Private method called by getModule, finds all the sub-modules for the
     * module given as parameter.
     * @param m Module to fill with sub-modules.
     * @param json the jsonObjcet of the module. 
     */
    
    private void fillModule(Module m, JsonObject json){

        if (json.has("rules")) {
            for (var x : json.getAsJsonArray("rules")) {

                // Contains is used instead of equals because the type names
                // have parentheses around them. Therefore this first if is used
                // to deal with type names that contain other type names.
                if (x.getAsJsonObject().getAsJsonPrimitive("type")
                        .toString().contains("AnyCourseUnitRule")
                        || x.getAsJsonObject().getAsJsonPrimitive("type")
                                .toString().contains("AnyModuleRule")) {

                    continue;
                } else if (x.getAsJsonObject().getAsJsonPrimitive("type")
                        .toString().contains("ModuleRule")) {

                    Pair<Module, JsonObject> result = handleModuleRule(x);
                    if(result != null){
                        fillModule(result.getKey(), result.getValue());
                        m.addModule(result.getKey().getName(), result.getKey());
                    }

                } else if (x.getAsJsonObject().getAsJsonPrimitive("type")
                        .toString().contains("CourseUnitRule")) {

                    Course course = handleCourseUnitRule(x);
                    if(course != null){
                        m.addCourse(course.getName(), course);
                    }
                } else if (x.getAsJsonObject().getAsJsonPrimitive("type")
                        .toString().contains("CompositeRule") || 
                        x.getAsJsonObject().getAsJsonPrimitive("type")
                        .toString().contains("CreditsRule")) {

                    fillModule(m, x.getAsJsonObject());
                }
                
            }
        } else if (json.has("rule")) {
            json = json.getAsJsonObject("rule");
            fillModule(m, json);
        }

    }

    /**
     * Private function used by fillModule to handle moduleRule modules.
     * @param x JsonElement of the moduleRule.
     * @return pair containing the newly created module and JsonObject
     */

    private Pair<Module, JsonObject> handleModuleRule(JsonElement x){

        String g = x.getAsJsonObject().getAsJsonPrimitive("moduleGroupId")
                .toString();

        g = g.substring(1, g.length() - 1);
        try{
            URL url = new URL(moduleByGId.replace(filler, g));
            Scanner scanner = new Scanner(url.openStream(), "UTF-8");
            String response = scanner.useDelimiter("\\Z").next();
            JsonArray arr = new JsonParser().parse(response).getAsJsonArray();

            x = arr.get(0).getAsJsonObject();
            scanner.close();
        } catch(JsonSyntaxException | IOException e) {
            return null;
        } 
        String newName = "  ";

        if (x.getAsJsonObject().getAsJsonObject("name").has("fi")) {

            newName = x.getAsJsonObject().getAsJsonObject("name")
                    .getAsJsonPrimitive("fi").toString();
        } else if (x.getAsJsonObject().getAsJsonObject("name").has("en")) {

            newName = x.getAsJsonObject().getAsJsonObject("name")
                    .getAsJsonPrimitive("en").toString();
        }

        newName = newName.substring(1, newName.length() - 1);

        int credits = 0;

        if (x.getAsJsonObject().has("targetCredits")
                && !x.getAsJsonObject().get("targetCredits").isJsonNull()) {
            credits = Integer
                    .parseInt(x.getAsJsonObject()
                            .getAsJsonObject("targetCredits")
                            .getAsJsonPrimitive("min").toString());
        }

        Module newModule = new Module(newName, credits);

        if (x.getAsJsonObject().has("outcomes")
                && !x.getAsJsonObject().get("outcomes").isJsonNull()) {
            String info = "";
            if (x.getAsJsonObject()
                    .getAsJsonObject("outcomes").has("fi")) {

                info = x.getAsJsonObject().getAsJsonObject("outcomes")
                        .getAsJsonPrimitive("fi").toString();

            } else if (x.getAsJsonObject()
                    .getAsJsonObject("outcomes").has("en")) {

                info = x.getAsJsonObject().getAsJsonObject("outcomes")
                        .getAsJsonPrimitive("en").toString();
            }
            info = info.substring(1, info.length() - 1);
            info = formatHtmlString(info);
            newModule.addInfo(info);
        }
        Pair<Module, JsonObject> result
                = new Pair<>(newModule, x.getAsJsonObject());

        return result;
    }
    
    /**
     * Private function used by fillModule to handle courseUnitRule modules.
     * @param x JsonElement of the courseUnitRule.
     * @return the newly formed course. Returns null if cannot find 
     * courseUnitRule.
     */
    private Course handleCourseUnitRule(JsonElement x){


        String g = x.getAsJsonObject().getAsJsonPrimitive("courseUnitGroupId")
                .toString();
        g = g.substring(1, g.length() - 1);
        
        try {
            URL url = new URL(courseByGId.replace(filler, g));
            Scanner scanner = new Scanner(url.openStream(), "UTF-8");
            String response = scanner.useDelimiter("\\Z").next();
            JsonArray arr = new JsonParser().parse(response).getAsJsonArray();
            x = arr.get(0).getAsJsonObject();
            scanner.close();
            
        } catch(JsonSyntaxException | IOException e) {
            return null;
        } 
        
        String code = "-";

        if (x.getAsJsonObject().has("code")
                && !x.getAsJsonObject().get("code").isJsonNull()) {
            code = x.getAsJsonObject().getAsJsonPrimitive("code").toString();
            code = code.substring(1, code.length() - 1);
        }

        String name = "  ";

        if (x.getAsJsonObject().getAsJsonObject("name").has("fi")) {

            name = x.getAsJsonObject().getAsJsonObject("name")
                    .getAsJsonPrimitive("fi").toString();
        } else if (x.getAsJsonObject().getAsJsonObject("name").has("en")) {

            name = x.getAsJsonObject().getAsJsonObject("name")
                    .getAsJsonPrimitive("en").toString();
        }

        int credits = Integer.parseInt(x.getAsJsonObject()
                .getAsJsonObject("credits").getAsJsonPrimitive("min")
                .toString());
        String info = "";
        if (x.getAsJsonObject().has("outcomes")
                && !x.getAsJsonObject().get("outcomes").isJsonNull()) {
            if (x.getAsJsonObject().getAsJsonObject("outcomes").has("fi")) {

                info = x.getAsJsonObject().getAsJsonObject("outcomes")
                        .getAsJsonPrimitive("fi").toString();
            } else if (x.getAsJsonObject()
                    .getAsJsonObject("outcomes").has("en")) {

                info = x.getAsJsonObject().getAsJsonObject("outcomes")
                        .getAsJsonPrimitive("en").toString();
            }
            info = info.substring(1, info.length() - 1);
        }
        info = formatHtmlString(info);

        name = name.substring(1, name.length() - 1);
        Course course = new Course(code, name, credits, info);
        course.setId(courseId);
        courseId++;
        return course;

    }
    
    /**
     * Private method used to format string with HTML tags to normal text format
     * compatible with our program.
     * @param s string to be reformatted.
     * @return reformatted string.
     */
    private String formatHtmlString(String s){
    
        s = s.replace("\\n","");
        s = s.replace("\\t","");
        s = Jsoup.parse(s).text();
        
        return s;
    }
    
    /**
     * A method for checking if the sisuData object was constructed properly.
     * @return Returns true if sisuData object was constructed properly,
     * otherwise false.
     */
    public Boolean getDataFoundStatus(){
        return dataFound;
    }
}
