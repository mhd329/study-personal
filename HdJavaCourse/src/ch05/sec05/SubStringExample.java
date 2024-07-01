package ch05.sec05;

public class SubStringExample {

	public static void main(String[] args) {
		String ssn = "880815-1234567";
		
		String fNum = ssn.substring(0, 6);
		String sNum = ssn.substring(7);
		
		System.out.println(fNum);
		System.out.println(sNum);

	}

}
