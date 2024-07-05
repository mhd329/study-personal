package classtest.kartRider;

public class Kart {
	private String name;
	private String color;

	private int myBooster = 0;
	private int maxBooster = 1;
	
	private int mySpeed = 0;
	private int maxSpeed = 150;
	private int speedUp = 40;
	private int speedUpBoost = 100;
	private int speedDown = 80;
	
	private void kartLog(String methodName) {
		System.out.print("["+this.name+"("+this.color+")"+"] "+methodName+" | 속도 : "+this.mySpeed+"(km) | 부스터 : "+this.myBooster+"(개)");
	}
	
	private String getMethodName() {
		String methodName = Thread.currentThread().getStackTrace()[2].getMethodName();
		return methodName;
	}
	
	public void speedUp() {
		this.mySpeed += this.speedUp;
		if (this.mySpeed > this.maxSpeed) {
			this.mySpeed = this.maxSpeed;
		}
		kartLog(this.getMethodName());
		System.out.println();
	}
	
	public void speedDown() {
		this.mySpeed -= this.speedDown;
		if (this.mySpeed < 0) {
			this.mySpeed = 0;
		}
		kartLog(this.getMethodName());
		System.out.println();
	}
	
	public void pickupBooster() {
		if (this.myBooster + 1 > this.maxBooster) {
			kartLog(this.getMethodName());
			System.out.println(" | 부스터를 더 이상 추가할 수 없습니다.");
			return;
		}
		this.myBooster += 1;
		kartLog(this.getMethodName());
		System.out.println();
	}
	
	public void useBooster() {
		if (this.myBooster - 1 < 0) {
			kartLog(this.getMethodName());
			System.out.println(" | 사용 가능한 부스터가 없습니다.");
			return;
		}
		this.myBooster -= 1;
		this.mySpeed += this.speedUpBoost;
		if (this.mySpeed > this.maxSpeed) {
			this.mySpeed = this.maxSpeed;
		}
		kartLog(this.getMethodName());
		System.out.println();
	}
	
	public void printKartInfo() {
		System.out.println("카트명 : " + this.name);
		System.out.println("카트 컬러 : " + this.color);
		System.out.println("속도 Up 호출 시 증가 속도 : " + this.speedUp);
		System.out.println("속도 Down 호출 시 감소 속도 : " + this.speedDown);
		System.out.println("최대 속도 : " + this.maxSpeed);
		System.out.println("부스터 사용시 증가 속도 : " + this.speedUpBoost);
		System.out.println("부스터 최대 보유 개수 : " + this.maxBooster);
	}
	
	Kart(String name, String color) {
		this.name = name;
		this.color = color;
	}
	
}

