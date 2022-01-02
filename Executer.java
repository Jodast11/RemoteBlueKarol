import java.util.Base64;
import org.json.simple.JSONObject;
import org.json.simple.JSONValue;

public class Executer
{
    
    public void execute(String commandString, ROBOTER r, Client s){
        JSONObject commandJson;
        try {
            commandJson = Json.decodeJSON(new String(Base64.getDecoder().decode(commandString)));
            //commandJson = Json.decodeJSON(commandString);
            String commandType = (String) commandJson.get("commandType");
            String command = (String) commandJson.get("command");
            if ("do".equals(commandType)){
                executeOpperation(command,r,commandJson);
            }
            else{
                getState(command,r,commandJson,s);
            }
        }
        catch (Exception e){
            System.out.println("Error decoding command '"+commandString+"'"+e);
            return;
        }
    }
    
    public void getState(String command, ROBOTER r, JSONObject commandJson, Client s){
        String data = "";
        if ("IstWand".equals(command)){
            data = String.valueOf(r.IstWand());
        }
        if ("AnzahlZiegelRucksackGeben".equals(command)){
            data = String.valueOf(r.AnzahlZiegelRucksackGeben());
        }
        if ("AnzahlZiegelVorneGeben".equals(command)){
            data = String.valueOf(r.AnzahlZiegelVorneGeben());
        }
        if ("BlickrichtungGeben".equals(command)){
            data = String.valueOf(r.BlickrichtungGeben());
        }
        if ("HatZiegelImRucksack".equals(command)){
            data = String.valueOf(r.HatZiegelImRucksack());
        }
        if ("IstBlickNorden".equals(command)){
            data = String.valueOf(r.IstBlickNorden());
        }
        if ("IstBlickSueden".equals(command)){
            data = String.valueOf(r.IstBlickSueden());
        }
        if ("IstBlickOsten".equals(command)){
            data = String.valueOf(r.IstBlickOsten());
        }
        if ("IstBlickWesten".equals(command)){
            data = String.valueOf(r.IstBlickWesten());
        }
        if ("IstMarke".equals(command)){
            if (commandJson.containsKey("farbe")){
                String farbe = (String) commandJson.get("farbe");
                data = String.valueOf(r.IstMarke(farbe));
            }
            else{
                data = String.valueOf(r.IstMarke()); 
            }
        }
        if ("IstRoboter".equals(command)){
            data = String.valueOf(r.IstRoboter());
        }
        if ("IstRoboterInSicht".equals(command)){
            data = String.valueOf(r.IstRoboterInSicht());
        }
        if ("IstRucksackLeer".equals(command)){
            data = String.valueOf(r.IstRucksackLeer());
        }
        if ("IstRucksackVoll".equals(command)){
            data = String.valueOf(r.IstRucksackVoll());
        }
        if ("IstZiegel".equals(command)){
            if (commandJson.containsKey("farbe")){
                String farbe = (String) commandJson.get("farbe");
                data = String.valueOf(r.IstZiegel(farbe));
            }
            else{
                data = String.valueOf(r.IstZiegel()); 
            }
        }
        if ("IstZiegelLinks".equals(command)){
            data = String.valueOf(r.IstZiegelLinks());
        }
        if ("IstZiegelRechts".equals(command)){
            data = String.valueOf(r.IstZiegelRechts());
        }
        if ("IstZiegelRechts".equals(command)){
            data = String.valueOf(r.IstZiegelRechts());
        }
        if ("KennungGeben".equals(command)){
            data = String.valueOf(r.KennungGeben());
        }
        if ("PositionXGeben".equals(command)){
            data = String.valueOf(r.PositionXGeben());
        }
        if ("PositionYGeben".equals(command)){
            data = String.valueOf(r.PositionYGeben());
        }
        if ("RoboterVorneKennungGeben".equals(command)){
            data = String.valueOf(r.RoboterVorneKennungGeben());
        }
        if ("RucksackPruefungGeben".equals(command)){
            data = String.valueOf(r.RucksackPruefungGeben());
        }
        if ("SichtbarkeitGeben".equals(command)){
            data = String.valueOf(r.SichtbarkeitGeben());
        }
        if ("SprungshoeheGeben".equals(command)){
            data = String.valueOf(r.SprungshoeheGeben());
        }
        if ("VerzoegerungGeben".equals(command)){
            data = String.valueOf(r.VerzoegerungGeben());
        }
        s.sendMessage("{\"messageType\":\"returnRequestedData\",\"data\":\""+B64.encode(data)+"\"}");
    }
    
    public void executeOpperation(String command, ROBOTER r, JSONObject commandJson){
        if ("Schritt".equals(command)){
            r.Schritt();
        }
        if ("LinksDrehen".equals(command)){
            r.LinksDrehen();
        }
        if ("RechtsDrehen".equals(command)){
            r.RechtsDrehen();
        }
        if ("Hinlegen".equals(command)){
            if (commandJson.containsKey("farbe")){
                String farbe = (String) commandJson.get("farbe");
                r.Hinlegen(farbe);
            }
            else{
                r.Hinlegen();  
            }
        }
        if ("Aufheben".equals(command)){
            r.Aufheben();
        }
        if ("MarkeSetzen".equals(command)){
            if (commandJson.containsKey("farbe")){
                String farbe = (String) commandJson.get("farbe");
                r.MarkeSetzen(farbe);
            }
            else{
                r.MarkeSetzen();  
            }
        }
        if ("MarkeLoeschen".equals(command)){
            r.MarkeLoeschen();
        }
        if ("TonErzeugen".equals(command)){
            r.TonErzeugen();
        }
        if ("MeldungAusgeben".equals(command)){
            String meldung = (String) commandJson.get("meldung");
            r.MeldungAusgeben(meldung);
        }
        if ("QuaderAufstellen".equals(command)){
           r.QuaderAufstellen();
        }
        if ("QuaderEntfernen".equals(command)){
           r.QuaderEntfernen();
        }
        if ("RucksackMaximumSetzen".equals(command)){
            int maximum = (int) commandJson.get("meldung");
            r.RucksackMaximumSetzen(maximum);
        }
        if ("SichtbarMachen".equals(command)){
           r.SichtbarMachen();
        }
        if ("SichtbarMachen".equals(command)){
            int hoehe = (int) commandJson.get("hoehe");
           r.SprunghoeheSetzen(hoehe);
        }
        if ("UnsichtbarMachen".equals(command)){
           r.UnsichtbarMachen();
        }
        if ("VerzoegerungSetzen".equals(command)){
            int verzoegerung = (int) commandJson.get("verzoegerung");
           r.VerzoegerungSetzen(verzoegerung);
        }
        if ("Warten".equals(command)){
            float zeit = (float) commandJson.get("zeit");
           r.Warten(zeit);
        }
    }
}
