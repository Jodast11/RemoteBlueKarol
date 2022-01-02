import java.io.*;  
import java.net.*;  
import java.util.concurrent.Callable;
import java.util.Base64;
import java.nio.charset.StandardCharsets;

public class Client implements Runnable
{
    public boolean stayConnected = true;
    DataOutputStream dout;
    ROBOTER r;
    Socket s;
    
    public Client(ROBOTER rNew, Socket sNew){
        r = rNew;
        s = sNew;
    }
    
    public void run(){
        try{
            Executer ex = new Executer();    
            DataInputStream din=new DataInputStream(s.getInputStream());  
            dout=new DataOutputStream(s.getOutputStream());
              
            String recived=""; 
            
            while(stayConnected){  
                recived=din.readLine();  
                if (recived != null){
                    System.out.println("Recived: "+recived);  
                    ex.execute(recived, r, this);
                }
                else{
                    System.out.println("Disconnected");
                    break;
                }
            }  
        }
        catch (Exception e){
            System.out.println("Error in client: "+e);
        }
    }
    
    public  void sendMessage(String message){
        try{
            System.out.println(message);
            System.out.println(B64.encode(message)+"\n");
            dout.writeUTF(B64.encode(message)+"\n");
            dout.flush();
        }
        catch (Exception e){
            System.out.println("Exception occured during sending of message: "+e);
        } 
    }
}
