package rsnp.notification;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;

@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = { "action_id", "action", "result_id", "result", "comment" })
@XmlRootElement(name = "data", namespace = "")

/**
 * 初期セットアップデータ
 */
public class StateData {

	@XmlElement(name = "action_id")
	private String action_id;

	@XmlElement(name = "action")
	private String action;

	@XmlElement(name = "result_id")
	private String result_id;

	@XmlElement(name = "result")
	private String result;

	@XmlElement(name = "comment")
	private String comment;

	public String getAction_id() {
		return action_id;
	}

	public String getAction() {
		return action;
	}

	public String getResult_id() {
		return result_id;
	}

	public String getResult() {
		return result;
	}

	public String getComment() {
		return comment;
	}

	public void setAction_id(String action_id) {
		this.action_id = action_id;
	}

	public void setAction(String action) {
		this.action = action;
	}

	public void setResult_id(String result_id) {
		this.result_id = result_id;
	}

	public void setResult(String result) {
		this.result = result;
	}

	public void setComment(String comment) {
		this.comment = comment;
	}

	@Override
	public String toString() {
		return "States [action_id=" + action_id + ", action=" + action + ", result_id=" + ", result=" + ", comment="
				+ "]";
	}
}
