import java.net.*; 
import java.io.*; 
class dr{ 
 public static void main(String[ ] args){ 
 try{ 
 InetAddress acceptorHost = InetAddress.getByName(args[0]); 
 int serverPortNum = Integer.parseInt(args[1]); 
 Socket clientSocket = new Socket(acceptorHost, serverPortNum); 
 BufferedReader br = new BufferedReader(new 
 InputStreamReader(clientSocket.getInputStream( ))); 
 System.out.println(br.readLine( )); 
 PrintStream ps = new PrintStream(clientSocket.getOutputStream( )); 
 ps.println("received your message.. Thanks"); 
 ps.flush( ); 
 clientSocket.close( ); 
 } 
 catch(Exception e){e.printStackTrace( );} 
 } 
 }