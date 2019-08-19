package JsonTrans;

import java.io.IOException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import logging.logging;
import rsnp.StateXMLNotificationMain;


public class JsonTrans {
	
	public static String array_ac_id[] = new String[5];
	public static String array_ac[] = new String[5];
	public static String array_re_id[] = new String[5];
	public static String array_re[] = new String[5];
	public static String array_co[] = new String[5];
	
	public static void run() {
		
		int i=0;
		
		//String sample_data = "{\"data\":[{\"ac_id\":\"1\",\"ac\":\"test\",\"re_id\":\"1\",\"re\":\"100\",\"co\":\"test\"}]}";
		ObjectMapper mapper = new ObjectMapper();
        
		try {
        	
        	String recv_data = StateXMLNotificationMain.send_data;
        	
        	if(recv_data == null) {
        		System.out.println("no data");
        	} else { 
            JsonNode data_json = mapper.readTree(recv_data);
            
            for (JsonNode n : data_json.get("data")) {
            	array_ac_id[i] = n.get("ac_id").asText();
            	array_ac[i] = n.get("ac").asText();
                array_re_id[i] = n.get("re_id").asText();
                array_re[i] = n.get("re").asText();
                array_co[i] = n.get("co").asText();
           
                i += 1;
            }
   
            logging.run();
        	}
     
        } catch (IOException e) {
            e.printStackTrace();
        }
	}
}
