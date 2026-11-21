import java.net.*;
import java.io.*;

public class MyClient {
    public static void main(String[] args) throws IOException {
        // Server এর address আর port দিয়ে connect করলাম
        Socket socket = new Socket("localhost", 5000);
        System.out.println("Server er sathe connect ");

        socket.close();
    }
}