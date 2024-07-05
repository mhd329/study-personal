package ch06.sec07.exam02;

public class Korean {
	private String nation = "대한민국";
	private String name;
	private String ssn;
	
	public Korean(String n, String s) {
		this.name = n;
		this.ssn = s;
	}
	
	public String getNation() {
		return this.nation;
	}
	
	public String getName() {
		return this.name;
	}
	
	public String getSsn() {
		return this.ssn;
	}
}
