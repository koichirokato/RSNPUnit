package main;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Properties;


public class SocketSample {
	public static void main(String[] args) throws IOException {

		String ipaddress;
		String port;
		int count;

		//read parameter
		Properties properties = new Properties();
		String pass_str = "Config.properties";
		InputStream istream = new FileInputStream(pass_str);
		properties.load(istream);

		ipaddress = properties.getProperty("IPaddress");
		port = properties.getProperty("Port");
		int port_int = Integer.valueOf(port).intValue();

		try {
			//make socket
			Socket csocket = new Socket(ipaddress, port_int);
			System.out.print("IPaddress: "+ipaddress);
			System.out.print("Port: "+ port);
			count = 0;

			PrintWriter writer = new PrintWriter(csocket.getOutputStream(), true);

			while (true) {
				count += 1;
				String sample_data= "{\"data\": [{\"ac_id\": \"1\", \"ac\": \"robot_state\", \"re_id\": \"1\", \"re\": "+count+", \"co\": \"\"}]}";

				writer.println(sample_data);
				System.out.println(sample_data);

				try {
					Thread.sleep(5000);
				} catch (InterruptedException e) {
				}

		        }
			} catch (Exception e) {
		      e.printStackTrace();
		    }


	}

}
