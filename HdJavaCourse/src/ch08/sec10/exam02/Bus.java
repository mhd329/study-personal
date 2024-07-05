package ch08.sec10.exam02;

public class Bus implements Vehicle {
	@Override
	public void run() {
		System.out.println("버스 run");
	}
	
	public void checkFare() {
		System.out.println("요금 확인");
	}
}
