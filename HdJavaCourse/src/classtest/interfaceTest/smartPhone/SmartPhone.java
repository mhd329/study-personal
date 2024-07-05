package classtest.interfaceTest.smartPhone;

public class SmartPhone extends SmartDisplay {
	@Override
	public void roll() {
		System.out.println("SmartPhone.roll()");
	}
	@Override
	public void flex() {
		System.out.println("SmartPhone.flex()");
	}
}
