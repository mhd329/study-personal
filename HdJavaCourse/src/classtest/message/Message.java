package classtest.message;

public class Message {
	public void printInfo(int args) {
		System.out.println(args);
	}
	public void printInfo(String args) {
		System.out.println(args);
	}
	public void printInfo(String str, int num) {
		System.out.println(str + ", " + num);
	}
	public void printInfo(int num, String str) {
		System.out.println(num + ", " + str);
	}
}
