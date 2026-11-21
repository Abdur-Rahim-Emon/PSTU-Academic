import java.net.*;
import java.io.*;

public class MyServer {
    public static void main(String[] args) throws IOException {
        // 1. Server কে একটা port এ বসিয়ে দিলাম, client এর জন্য অপেক্ষা করবে
        ServerSocket serverSocket = new ServerSocket(5000);
        System.out.println("Server চালু, client এর জন্য অপেক্ষা করছি...");

        // 2. যখনই কোনো client connect করবে, এই লাইন থামিয়ে দিবে (wait করবে)
        Socket clientSocket = serverSocket.accept();
        System.out.println("Client connect হয়ে গেছে!");

        // 3. Client কে বন্ধ ঘোষণা করে দিলাম
        clientSocket.close();
        serverSocket.close();
    }
}