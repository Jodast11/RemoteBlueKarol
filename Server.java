import java.io.*;  
import java.net.*;  
import java.util.concurrent.Callable;
import java.util.Base64;
import java.nio.charset.StandardCharsets;

public class Server implements Runnable
{
    
    ROBOTER r;
    
    public Server(ROBOTER rNew){
        r = rNew;
    }  
    
    public void run(){  
        try{
            ServerSocket ss= new ServerSocket(3333);  
            while (true){
                Socket s=ss.accept(); 
                Client newClient = new Client(r,s);
                new Thread(newClient).start();
                System.out.println("Client connected");
            }
        }
        catch (Exception e){
            System.out.println(e);
        }
    }
}