/*
 * $Id: StateNotificator.java 117 2010-04-12 09:27:58Z mitsuki $
 *
 * Copyright 2009-2010 Fujitsu Limited.
 * FUJITSU CONFIDENTIAL.
 */
package rsnp.info;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Properties;
import java.util.Timer;
import java.util.TimerTask;

import org.robotservices.custom_profile.lib.common.util.XMLUtil;
import org.robotservices.v02.exception.RSiException;
import org.robotservices.v02.profile.invoker.IInformation_profile;

import JsonTrans.JsonTrans;
import rsnp.notification.NotificationData;
import rsnp.notification.StateData;

public class StateNotificator extends TimerTask {

	private long conv_id;
	private IInformation_profile inp;
	private Timer timer;

	/**
	 * コンストラクタ。
	 *
	 * @param conv_id
	 * @param inp
	 */
	public StateNotificator(long conv_id, IInformation_profile inp) {
		this.conv_id = conv_id;
		this.inp = inp;
	}

	public void startNotify() throws IOException {

		if(timer == null) {
			Properties properties = new Properties();
			String pass_str = "DataLog/Config.properties";
			InputStream istream= new FileInputStream(pass_str);
			properties.load(istream);

			String interval_str = properties.getProperty("send_interval");
			int interval_int = Integer.valueOf(interval_str).intValue();

			timer = new Timer();
			timer.schedule(this, 0, interval_int);
		}
	}

	/**
	 * 状態通知を停止します。
	 */
	public void stopNotify() {

		if (timer != null) {
			timer.cancel();
			timer = null;
		}
	}

	@Override
	public void run() {

		//String recv_data = StateXMLNotificationMain.send_data;

		NotificationData notificationData = new NotificationData();

		ArrayList<StateData> stateList = new ArrayList<StateData>();

		StateData stateDataActionId1 = new StateData();
		StateData stateDataActionId2 = new StateData();
		StateData stateDataActionId3 = new StateData();
		StateData stateDataActionId4 = new StateData();
		StateData stateDataActionId5 = new StateData();

		if(JsonTrans.array_ac_id[0] != null) {
			stateDataActionId1.setAction_id(JsonTrans.array_ac_id[0]);
			stateDataActionId1.setAction(JsonTrans.array_ac[0]);
			stateDataActionId1.setResult_id(JsonTrans.array_re_id[0]);
			stateDataActionId1.setResult(JsonTrans.array_re[0]);
			stateDataActionId1.setComment(JsonTrans.array_co[0]);
			stateList.add(stateDataActionId1);
		}
		if(JsonTrans.array_ac_id[1] != null) {
			stateDataActionId2.setAction_id(JsonTrans.array_ac_id[1]);
			stateDataActionId2.setAction(JsonTrans.array_ac[1]);
			stateDataActionId2.setResult_id(JsonTrans.array_re_id[1]);
			stateDataActionId2.setResult(JsonTrans.array_re[1]);
			stateDataActionId2.setComment(JsonTrans.array_co[1]);
			stateList.add(stateDataActionId2);
		}
		if(JsonTrans.array_ac_id[2] != null) {
			stateDataActionId3.setAction_id(JsonTrans.array_ac_id[2]);
			stateDataActionId3.setAction(JsonTrans.array_ac[2]);
			stateDataActionId3.setResult_id(JsonTrans.array_re_id[2]);
			stateDataActionId3.setResult(JsonTrans.array_re[2]);
			stateDataActionId3.setComment(JsonTrans.array_co[2]);
			stateList.add(stateDataActionId3);
		}
		if(JsonTrans.array_ac_id[3] != null) {
			stateDataActionId4.setAction_id(JsonTrans.array_ac_id[3]);
			stateDataActionId4.setAction(JsonTrans.array_ac[3]);
			stateDataActionId4.setResult_id(JsonTrans.array_re_id[3]);
			stateDataActionId4.setResult(JsonTrans.array_re[3]);
			stateDataActionId4.setComment(JsonTrans.array_co[3]);
			stateList.add(stateDataActionId4);
		}
		if(JsonTrans.array_ac_id[4] != null) {
			stateDataActionId5.setAction_id(JsonTrans.array_ac_id[4]);
			stateDataActionId5.setAction(JsonTrans.array_ac[4]);
			stateDataActionId5.setResult_id(JsonTrans.array_re_id[4]);
			stateDataActionId5.setResult(JsonTrans.array_re[4]);
			stateDataActionId5.setComment(JsonTrans.array_co[4]);
			stateList.add(stateDataActionId5);
		}
		/*for(int i=0;i<1;i++) {
		stateDataActionId[i].setAction_id(JsonTrans.array_ac_id[i]);
		stateDataActionId[i].setAction(JsonTrans.array_ac[i]);
		stateDataActionId[i].setResult_id(JsonTrans.array_re_id[i]);
		stateDataActionId[i].setResult(JsonTrans.array_re[i]);
		stateDataActionId[i].setComment(JsonTrans.array_co[i]);
		stateList.add(stateDataActionId[i]);
		}*/

		notificationData.setStates(stateList);

		SimpleDateFormat sdf = new SimpleDateFormat("yyyyMMddHHmmss");
		String time = sdf.format(Calendar.getInstance().getTime());

		notificationData.setTime(time);

		String xml = XMLUtil.marshalJAXB(notificationData);


		try {
			inp.notify_state(conv_id, xml, null);

			System.out.println("run notify_state");
			System.out.println(xml);

		} catch (RSiException e) {
			e.printStackTrace();
			// 通知を停止する
			stopNotify();
		}
	}
}
