package rsnp;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Properties;
import java.util.logging.Logger;

import org.robotservices.v02.profile.common.Ret_value;
import org.robotservices.v02.profile.invoker.IBasic_profile;
import org.robotservices.v02.profile.invoker.IInformation_profile;
import org.robotservices.v02.profile.invoker.InvokerProfileFactory;
import org.robotservices.v02.util.ConnectionInfo;

import com.fujitsu.rsi.helper.BasicProfileHelper;
import com.fujitsu.rsi.util.RESULT;

import rsnp.info.StateNotificator;

/**
 * Notification StateXML　サンプル<br>
 * ロボットアプリメイン
 */
public class StateXMLNotificationMain {

	public static String send_data = null;

	public static String recieve_data = null;

	private static Logger log = Logger.getLogger(StateXMLNotificationMain.class.getName());

	//private static String targetEPR = "http://robots.aiit.ac.jp:8080/UpdateNotificationState/services";

	public static void main(String[] args) throws IOException {

		Properties properties = new Properties();
		String pass_str = "DataLog/Config.properties";
		InputStream istream = new FileInputStream(pass_str);
		properties.load(istream);

		ServerSocket serversock = new ServerSocket(9002);
		Socket sock = null;

		Socket_communication st = new Socket_communication();
		st.start();

		String user_id = properties.getProperty("robot_id");

		String password ="8073";


		ConnectionInfo ci = new ConnectionInfo();

		String targetEPR = properties.getProperty("end_point");

		ci.set_endpointname(targetEPR);

		InvokerProfileFactory factory = null;

		try {
			factory = InvokerProfileFactory.newInstance(ci);

			factory.connect();

			// Basic_profileによる認証
			IBasic_profile bp = factory.getBasic_profile();
			Ret_value ret = bp.open(user_id, password);
			BasicProfileHelper bphlp = new BasicProfileHelper(ret);
			if (bphlp.getResult() != RESULT.SUCCESS.getResult()) {
				log.severe("Basic_profile#open()エラー[" + bphlp.getDetailCode()
						+ "]：" + bphlp.getDetail());
				bp = null;
				return;
			}

			long conv_id = bphlp.getConv_id();
			log.info("conv_id:" + conv_id);

			// Information_profileでロボットの状態通知
			IInformation_profile inp = factory.getInformation_profile();

			StateNotificator sn = new StateNotificator(conv_id, inp);
			sn.startNotify();

			// Socketに接続があるまで停止
			System.out.println("localhost の9002番ポートに接続すると終了します。");
		    sock = serversock.accept();



			if (sn != null) {
				sn.stopNotify();
			}


			if (bp != null) {
				bp.close(conv_id);
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			try {

				if (factory != null) {
					factory.disconnect();
				}
			} catch (Exception e) {
				e.printStackTrace();
			}
			if (sock != null) {
				sock.close();
			}
			serversock.close();
		}

		log.info("exit");
		System.exit(0);
	}

}


