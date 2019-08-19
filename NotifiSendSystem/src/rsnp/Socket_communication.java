package rsnp;

import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.InputStream;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Properties;

import JsonTrans.JsonTrans;

public class Socket_communication extends Thread{

	public static String Socket_recieve_data = null;

	public void run(){

		ServerSocket sSocket = null;
		Socket socket = null;

		byte[] buf = new byte[1024];

		try{
			Properties properties = new Properties();
			String pass_str = "DataLog/Config.properties";
			InputStream istream = new FileInputStream(pass_str);
			properties.load(istream);
			String port_str = properties.getProperty("port");
			int port_int = Integer.valueOf(port_str).intValue();
			InetAddress addr = InetAddress.getLocalHost();
			//IPアドレスとポート番号を指定してサーバー側のソケットを作成
			sSocket = new ServerSocket();
			sSocket.bind(new InetSocketAddress(addr.getHostAddress(),port_int));

			System.out.println("set host IPaddress : " + addr.getHostAddress());

			System.out.println("connecting now");

			socket = sSocket.accept();

			System.out.println("connection success");
		    }catch(Exception e){
				e.printStackTrace();
				System.out.println("connection failed");
			}
            try {

            InputStream is = socket.getInputStream();
            DataInputStream dis = new DataInputStream(is);

			while(true){
				dis.read(buf);

                String str = new String(buf, "UTF-8");
                String strip_str = str.trim();
                System.out.println("recv_data: "+strip_str);
                Socket_recieve_data = strip_str;
                JsonTrans.run();
                StateXMLNotificationMain.recieve_data = str;
                StateXMLNotificationMain.send_data = strip_str;

                if (str == "fin"){
                	is.close();
					socket.close();
					sSocket.close();
					System.out.println("server down");
					break;
					}
    			}
            }catch(Exception e){
			e.printStackTrace();
            }
		}
}
