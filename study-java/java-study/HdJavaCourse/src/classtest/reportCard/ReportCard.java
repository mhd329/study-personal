package classtest.reportCard;

public class ReportCard {
	
	private String name;
	private int k;
	private int e;
	private int m;
	private int sum;
	private int avg;
	private char hakjum;
	
	public void setName(String name) {
		this.name = name;
	}
	public void setKorean(int k) {
		this.k = k;
	}
	public void setEnglish(int e) {
		this.e = e;
	}
	public void setMath(int m) {
		this.m = m;
	}
	public void sum(int k, int e, int m) {
		this.sum = k + e + m;
	}
	private void average(int sum) {
		this.avg = sum / 3;
	}
	private void hakjum(int avg) {
		switch (avg / 10) {
			case 10, 9 -> {
				this.hakjum = 'A';
			}
			case 8 -> {
				this.hakjum = 'B';
			}
			case 7 -> {
				this.hakjum = 'C';
			}
			case 6 -> {
				this.hakjum = 'D';
			}
			default -> {
				this.hakjum = 'F';
			}
		}
	}
	
	public String getName() {
		return this.name;
	}
	
	public int getKorean() {
		return this.k;
	}
	
	public int getEnglish() {
		return this.e;
	}
	
	public int getMath() {
		return this.m;
	}
	
	public int sum() {
		this.sum(this.k, this.e, this.m);
		return this.sum;
	}
	
	public int average() {
		this.average(this.sum);
		return this.avg;
	}
	
	public char hakjum() {
		this.hakjum(this.avg);
		return this.hakjum;
	}
	
	public void printInfo() {
		System.out.println(this.getName());
		System.out.println(this.getKorean());
		System.out.println(this.getEnglish());
		System.out.println(this.getMath());
		System.out.println(this.sum());
		System.out.println(this.average());
		System.out.println(this.hakjum());
	}
	
	ReportCard(String name) {
		this(name, 0, 0, 0);
	}
	
	ReportCard(String name, int k, int e, int m) {
		this.setName(name);
		this.setKorean(k);
		this.setEnglish(e);
		this.setMath(m);
		
		this.sum(this.k, this.e, this.m);
		this.average(this.sum);
		this.hakjum(this.avg);
	}
}
