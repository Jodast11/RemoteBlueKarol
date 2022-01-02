
/**
 * Write a description of class Main here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Main
{
    public  Main(){
        WELT w = new WELT(10, 10, 10);
        ROBOTER r = new ROBOTER(1,1,'S',w);
        Server server = new Server(r);
        new Thread(server).start();
    }
}
