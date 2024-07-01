package classtest.data;

public class Data {
	private int myCount;
	private static int staticCount;
	
	public Data() {
		myCount += 1;
		staticCount += 1;
	}
	
	public void printInfo() {
		System.out.println(myCount);
		System.out.println(staticCount);
	}
}
