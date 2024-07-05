package ch06.sec08.exam03;

public class Car {
	int gas;
	
	void setGas(int gas) {
		this.gas = gas;
	}
	
	boolean isLeftGas() {
		if (this.gas == 0) {
			System.out.println("가스 없음.");
			return false;
		}
		System.out.println("현재 가스 잔량 : " + this.gas);
		return true;
	}
	
	void run() {
		while (true) {
			if (this.isLeftGas()) {
				System.out.println("달립니다.");
			} else {
				System.out.println("멈춥니다.");
				return;
			}
			this.gas -= 1;
		}
	
	}
	
}
