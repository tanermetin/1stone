/**
 * Created by tanermetin on 19.06.18.
 */
import java.io.*;
import java.net.*;


class UDPServer{

    public static void main(String args[]) throws Exception
    {

        int portUDP = 9876;

        DatagramSocket serverSocket = new DatagramSocket(portUDP);


        byte[] receiveData = new byte[1024];
        byte[] sendData = new byte[1024];

        System.out.println("LISTENING AT: " +  serverSocket.getLocalSocketAddress());


        while(true)
        {

            DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);

            serverSocket.receive(receivePacket);

            String sentence = new String( receivePacket.getData());

            InetAddress IPAddress = receivePacket.getAddress();

            System.out.println("RECEIVED: " + sentence);
            System.out.println("FROM: " + IPAddress);

            int port = receivePacket.getPort();

            String capitalizedSentence = sentence.toUpperCase();
            sendData = capitalizedSentence.getBytes();

            DatagramPacket sendPacket =
                    new DatagramPacket(sendData, sendData.length, IPAddress, port);
            serverSocket.send(sendPacket);
        }
    }
}
