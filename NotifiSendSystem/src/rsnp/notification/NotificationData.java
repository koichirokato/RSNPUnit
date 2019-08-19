package rsnp.notification;

import java.util.List;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlElementWrapper;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;

@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = { "states","time" })
@XmlRootElement(name = "notification", namespace = "")

/**
 * 初期セットアップデータ
 */
public class NotificationData {

	@XmlElementWrapper(name = "states")
	@XmlElement(name = "status")
	private List<StateData> states;

	@XmlElement(name = "time")
	private String time;

	public List<StateData> getStates() {
		return states;
	}

	public String getTime() {
		return time;
	}

	public void setStates(List<StateData> states) {
		this.states = states;
	}


	public void setTime(String time) {
		this.time = time;
	}

	@Override
	public String toString() {
		return "Notification [states=" + states + ", time=" + time
				+ "]";
	}
}
