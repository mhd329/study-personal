package ch07.sec08.exam02;

public class DriverExample {

	public static void main(String[] args) {
		Driver d = new Driver();
		
		Bus b = new Bus();
		d.drive(b);
		Taxi t = new Taxi();
		d.drive(t);

	}

}
