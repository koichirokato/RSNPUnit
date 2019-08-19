package logging;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import rsnp.Socket_communication;


public class logging {
	
	public static void run() {
		
		LocalDateTime date = LocalDateTime.now();
		DateTimeFormatter dateFormat = DateTimeFormatter.ofPattern("yyyy-MM-dd");
		DateTimeFormatter timeFormat = DateTimeFormatter.ofPattern("HH:mm:ss");
		String date_format_str = date.format(dateFormat);
		String time_format_str = date.format(timeFormat);
		File log_file = new File("NotifiSendSystemLog/datalog" + date_format_str + ".json");
		
		try {
			if(log_file.exists()) {  //ファイルが存在しているかどうか
				
				FileWriter file_out = new FileWriter(log_file, true);
				file_out.write("{\"time\":\""+time_format_str+"\","+Socket_communication.Socket_recieve_data.substring(1)+"\n");
				file_out.close();
				}
			else {
				log_file.createNewFile();
				}
		
		} catch (IOException e1) {
			// TODO 自動生成された catch ブロック
			e1.printStackTrace();
		}
	
	}

}
