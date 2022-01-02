import org.json.simple.JSONObject;
import org.json.simple.JSONValue;

public class Json {
    public static JSONObject decodeJSON(String Json) {
        Object o1 = JSONValue.parse(Json);
        JSONObject jsonObj = (JSONObject) o1;
        return jsonObj;
    }
}