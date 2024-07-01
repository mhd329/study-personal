package classtest.pay;

public class Pay {
	private int dPay;
	private int wPay;
	private int yPay;
	
	public void setDPay(int hP) {
		this.dPay = hP * 8;
	}
	
	public void setWPay(int hP) {
		this.wPay = hP * 8 * 5;
	}
	
	public void setYPay(int hP) {
		this.yPay = hP * 8 * 5 * 52;
	}
	
	public int getDPay(int hP) {
		this.setDPay(hP);
		return this.dPay;
	}
	
	public int getWPay(int hP) {
		this.setWPay(hP);
		return this.wPay;
	}
	
	public int getYPay(int hP) {
		this.setYPay(hP);
		return this.yPay;
	}
}
