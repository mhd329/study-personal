package classtest.pay;

public class Pay2 {
	private int hPay;
	private int dPay;
	private int wPay;
	private int yPay;
	
	public Pay2(int hPay) {
		this.hPay = hPay;
	}
	
	public void setDPay() {
		this.dPay = this.hPay * 8;
	}
	
	public void setWPay() {
		this.wPay = this.hPay * 8 * 5;
	}
	
	public void setYPay() {
		this.yPay = this.hPay * 8 * 5 * 52;
	}
	
	public int getDPay() {
		this.setDPay();
		return this.dPay;
	}
	
	public int getWPay() {
		this.setWPay();
		return this.wPay;
	}
	
	public int getYPay() {
		this.setYPay();
		return this.yPay;
	}
}
