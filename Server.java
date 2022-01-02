import java.io.*;  
import java.net.*;  
import java.util.concurrent.Callable;
import java.util.Base64;
import java.nio.charset.StandardCharsets;

public class Server implements Runnable
{
    static Boolean stayConnected = true;
    DataOutputStream dout;
    
    
    ROBOTER r;
    
    public Server(ROBOTER rNew){
        r = rNew;
    }
    
    public void run(){  
        try{
            Executer ex = new Executer();
            ServerSocket ss= new ServerSocket(3333);  
            Socket s=ss.accept();  
            System.out.println("Client connected");
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
                //dout.writeUTF(str2);  
                //dout.flush();  
            }  
        }
        catch (Exception e){
            System.out.println(e);
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
    
    public static void disconnect(){
        stayConnected = false;
    }
}