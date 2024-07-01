package classtest.suncream;

public class SunCream {
	// int type parameters
	private int capacity;
	private int spf;
	
	// str
	private String company;
	private String name;
	private String pa;
	
	// char
	private char skinType;
	
	// boolean
	private boolean stickiness;
	
	/////////////////////////////
	
	// str getters
	public String getCompany() {
		return this.company;
	}
	
	public String getName() {
		return this.name;
	}
		
	public String getPa() {
		return this.pa;
	}
	
	// char getters
	public char getSkinType() {
		return this.skinType;
	}
	
	// boolean getters
	public boolean isStickiness() {
		return this.stickiness;
	}
	
	// int getters
	public int getCapacity() {
		return this.capacity;
	}
	
	public String getSpf() {
		return this.company;
	}
	
	////////////////////////
	
	// str setters
	public void setCompany(String company) {
		this.company = company;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public void setPa(String pa) {
		this.pa = pa;
	}
	
	// char setters
	
	public void setSkinType(char skinType) {
		this.skinType = skinType;
	}
	
	// int setters
	
	public void setCapacity(int capacity) {
		if (capacity < 1) {
			System.out.println("용량은 0보다 커야합니다.");
			return;
		}
		this.capacity = capacity;
	}
	
	public void setSpf(int spf) {
		if (spf < 1) {
			System.out.println("차단도는 0보다 커야합니다.");
			return;
		}
		this.spf = spf;
	}
	
	// boolean setters
	
	public void setStickiness(boolean stickiness) {
		this.stickiness = stickiness;
	}
	
	public void printInfo() {
		System.out.println(this.company);
		System.out.println(this.name);
		
		if (this.isStickiness()) {
			System.out.println("끈적거림.");
		} else {
			System.out.println("끈적임 없음.");
		}
		
		switch (this.skinType) {
		case 's' -> {
				System.out.println("민감성");
			}
		case 'o' -> {
				System.out.println("지성");
			}
		case 'n' -> {
				System.out.println("중성");
			}
		case 'd' -> {
				System.out.println("건성");
			}
		}
		
		System.out.println(this.capacity);
		System.out.println(this.spf);
		
		System.out.println(this.pa);
	}
	
}
