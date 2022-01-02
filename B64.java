import java.util.Base64;
import java.nio.charset.StandardCharsets;

public class B64
{
   public static String encode(String text){
       try{
           return Base64.getEncoder().encodeToString(text.getBytes(StandardCharsets.UTF_8.toString()));
        }
        catch(Exception e){
            System.out.println("Error during encoding: "+e);
            return "";
        }
   }
   
   public static String decode(String text){
       return new String(Base64.getDecoder().decode(text));
    }
}
