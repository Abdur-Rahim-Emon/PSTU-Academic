import java.net.*;
import java.io.*;

class dr{
    public static void main(String[] args){
        try{
            int MAX_LEN = 60;

            int localPortNum =
                Integer.parseInt(args[0]);

            DatagramSocket mySocket =
                new DatagramSocket(localPortNum);

            byte[] recvBuffer = new byte[MAX_LEN];

            DatagramPacket packet =
                new DatagramPacket(recvBuffer, MAX_LEN);

            mySocket.receive(packet);

            String message =
                new String(recvBuffer);

            System.out.println(message);

            InetAddress senderAddress =
                packet.getAddress();

            int senderPort =
                packet.getPort();

            String messageToSend =
                args[1];

            byte[] sendBuffer =
                messageToSend.getBytes();

            DatagramPacket datagram =
                new DatagramPacket(sendBuffer,
                                   sendBuffer.length,
                                   senderAddress,
                                   senderPort);

            mySocket.send(datagram);

            mySocket.close();
        }
        catch(Exception e){
            e.printStackTrace();
        }
    }
}